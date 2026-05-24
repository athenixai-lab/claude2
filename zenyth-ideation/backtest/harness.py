"""
Common simulation harness for ZENYTH strategy backtests.

Trade lifecycle:
    open at bar t (entry price = open[t])
    exit at first of: stop hit, target hit, time_stop (close of that bar)

Conservative intrabar ordering: when both stop and target are reachable in the
same bar, stop is taken first (worst-case assumption). This is the standard
defensive convention for OHLC-only backtests.

PnL is reported in pips (1 pip = 1e-4 EURUSD). Risk-multiple ("R") is
reported using each trade's per-trade stop distance.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field, asdict
from typing import Iterable

import numpy as np
import pandas as pd


PIP = 1e-4


@dataclass
class TradeIntent:
    entry_ts: pd.Timestamp        # bar AT which we enter (entry price = open[entry_ts])
    direction: int                # +1 long, -1 short
    stop: float                   # price level
    target: float | None          # price level OR None for time-stop-only
    time_stop_ts: pd.Timestamp    # at this bar's close we exit if neither hit
    tag: str = ""                 # arbitrary label for diagnostics


@dataclass
class TradeResult:
    entry_ts: pd.Timestamp
    exit_ts: pd.Timestamp
    direction: int
    entry: float
    exit: float
    stop: float
    target: float | None
    exit_reason: str              # "stop" / "target" / "time"
    pnl_price: float              # exit - entry, signed by direction
    pnl_pips: float
    risk_pips: float
    r_multiple: float
    tag: str = ""


def simulate(df: pd.DataFrame, intents: Iterable[TradeIntent]) -> pd.DataFrame:
    """Run a list of TradeIntent objects against df (M1 OHLC, tz-aware index).

    Returns a DataFrame of TradeResult records.
    """
    results: list[TradeResult] = []

    # Cheap lookup: ensure df index is sorted and has unique timestamps.
    if not df.index.is_monotonic_increasing:
        df = df.sort_index()

    for intent in intents:
        if intent.entry_ts not in df.index:
            continue  # skip trades whose entry bar is not in data (gap)
        entry_loc = df.index.get_loc(intent.entry_ts)
        try:
            ts_loc = df.index.get_loc(intent.time_stop_ts)
        except KeyError:
            # time_stop bar missing — clip to last available bar
            ts_loc = df.index.searchsorted(intent.time_stop_ts) - 1
        if ts_loc < entry_loc:
            continue

        entry_price = float(df["open"].iat[entry_loc])
        d = intent.direction
        stop = float(intent.stop)
        target = float(intent.target) if intent.target is not None else None
        risk_price = abs(entry_price - stop)
        if risk_price <= 0:
            continue

        exit_reason = "time"
        exit_price = float(df["close"].iat[ts_loc])
        exit_loc = ts_loc

        # Walk forward bar-by-bar, including the entry bar itself.
        for j in range(entry_loc, ts_loc + 1):
            high = float(df["high"].iat[j])
            low = float(df["low"].iat[j])

            # Conservative: stop checked before target inside the same bar.
            if d > 0:
                if low <= stop:
                    exit_reason = "stop"
                    exit_price = stop
                    exit_loc = j
                    break
                if target is not None and high >= target:
                    exit_reason = "target"
                    exit_price = target
                    exit_loc = j
                    break
            else:
                if high >= stop:
                    exit_reason = "stop"
                    exit_price = stop
                    exit_loc = j
                    break
                if target is not None and low <= target:
                    exit_reason = "target"
                    exit_price = target
                    exit_loc = j
                    break

        pnl_price = d * (exit_price - entry_price)
        pnl_pips = pnl_price / PIP
        risk_pips = risk_price / PIP
        r_multiple = pnl_pips / risk_pips if risk_pips > 0 else 0.0

        results.append(
            TradeResult(
                entry_ts=intent.entry_ts,
                exit_ts=df.index[exit_loc],
                direction=d,
                entry=entry_price,
                exit=exit_price,
                stop=stop,
                target=target if target is not None else math.nan,
                exit_reason=exit_reason,
                pnl_price=pnl_price,
                pnl_pips=pnl_pips,
                risk_pips=risk_pips,
                r_multiple=r_multiple,
                tag=intent.tag,
            )
        )

    if not results:
        return pd.DataFrame(
            columns=[
                "entry_ts", "exit_ts", "direction", "entry", "exit",
                "stop", "target", "exit_reason", "pnl_price", "pnl_pips",
                "risk_pips", "r_multiple", "tag",
            ]
        )

    return pd.DataFrame([asdict(r) for r in results])


def apply_cost(trades: pd.DataFrame, spread_pips: float) -> pd.DataFrame:
    """Subtract round-trip spread cost from pnl_pips and recompute r_multiple."""
    out = trades.copy()
    out["pnl_pips"] = out["pnl_pips"] - spread_pips
    out["r_multiple"] = np.where(
        out["risk_pips"] > 0,
        out["pnl_pips"] / out["risk_pips"],
        0.0,
    )
    return out


def report(trades: pd.DataFrame, label: str = "strategy") -> dict:
    """Standard stats block: trade count, win rate, mean R, PF, max DD."""
    if trades.empty:
        return {"label": label, "trades": 0}

    pnl = trades["pnl_pips"].to_numpy()
    r = trades["r_multiple"].to_numpy()
    wins = pnl[pnl > 0]
    losses = pnl[pnl <= 0]
    pf = (wins.sum() / -losses.sum()) if losses.sum() < 0 else float("inf")
    equity = pnl.cumsum()
    peak = np.maximum.accumulate(equity) if len(equity) else np.array([0.0])
    dd = (equity - peak)
    max_dd_pips = float(dd.min()) if len(dd) else 0.0

    return {
        "label": label,
        "trades": int(len(trades)),
        "win_rate": float((pnl > 0).mean()),
        "mean_R": float(r.mean()),
        "median_R": float(np.median(r)),
        "total_pips": float(pnl.sum()),
        "mean_pips": float(pnl.mean()),
        "std_pips": float(pnl.std(ddof=0)),
        "profit_factor": float(pf),
        "max_dd_pips": max_dd_pips,
        "stop_rate": float((trades["exit_reason"] == "stop").mean()),
        "target_rate": float((trades["exit_reason"] == "target").mean()),
        "time_rate": float((trades["exit_reason"] == "time").mean()),
        "start": str(trades["entry_ts"].min()),
        "end": str(trades["entry_ts"].max()),
    }


def report_by_year(trades: pd.DataFrame) -> pd.DataFrame:
    if trades.empty:
        return pd.DataFrame()
    t = trades.copy()
    t["year"] = pd.to_datetime(t["entry_ts"]).dt.year
    g = t.groupby("year").agg(
        trades=("pnl_pips", "size"),
        win_rate=("pnl_pips", lambda s: (s > 0).mean()),
        mean_R=("r_multiple", "mean"),
        total_pips=("pnl_pips", "sum"),
        max_dd_pips=("pnl_pips", lambda s: float((s.cumsum() - s.cumsum().cummax()).min())),
    )
    return g
