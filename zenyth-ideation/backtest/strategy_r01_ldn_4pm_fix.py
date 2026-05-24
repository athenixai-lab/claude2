"""
Round 1: LDN_4PM_Fix_Drift_Reversion

Per spec (EST fixed UTC-5):
    11:20 EST = 16:20 London (well before fix)
    11:55 EST = 16:55 London (fix window start)
    12:00 EST = 17:00 London (fix window close)

Rule:
    D = close(11:55) - close(11:20)
    if |D| in top decile (rolling 60-day, computed on weekdays with valid window) AND
       sign(close(12:00) - close(11:55)) == sign(D):
        direction = -sign(D)  [fade]
        entry at open(12:01)
        stop  = (max high if direction<0 else min low) of 11:56..12:00 + 3 pips buffer
        target = close(11:20)
        time stop = 13:00 EST
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, add_helpers, EST_FIXED  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


def build_intents(df: pd.DataFrame, lookback_pct: int = 60, top_decile: float = 0.90) -> list[TradeIntent]:
    """Return list of TradeIntents for R1."""
    # Pre-extract bars at the relevant times.
    df = df.copy()
    df["hhmm"] = df.index.strftime("%H%M").astype(int)
    df["weekday"] = df.index.weekday

    # Resample to per-day rows keyed by date (in EST).
    df["date_est"] = df.index.normalize()
    only_window = df[df["hhmm"].isin([1120, 1155, 1200])]
    # Pivot: rows = date, cols = hhmm, vals = close
    closes = (
        only_window.reset_index()
        .pivot_table(index="date_est", columns="hhmm", values="close", aggfunc="first")
    )

    # high/low during 11:56..12:00
    win = df[(df["hhmm"] >= 1156) & (df["hhmm"] <= 1200)]
    win_extremes = win.groupby("date_est").agg(win_high=("high", "max"), win_low=("low", "min"))

    # opens at 12:01 (entry bar)
    entry = df[df["hhmm"] == 1201].copy()
    entry["date_est"] = entry.index.normalize()
    entry_open = entry.reset_index().set_index("date_est")["open"]

    table = closes.join(win_extremes, how="inner").join(entry_open.rename("entry_open"), how="inner")
    needed = [1120, 1155, 1200]
    table = table.dropna(subset=needed + ["win_high", "win_low", "entry_open"])

    # Only weekdays Mon..Fri (weekday < 5).
    weekday_table = table[pd.to_datetime(table.index).weekday < 5].copy()

    weekday_table["D"] = weekday_table[1155] - weekday_table[1120]
    weekday_table["abs_D"] = weekday_table["D"].abs()
    # rolling top-decile threshold over last lookback_pct valid weekday observations
    weekday_table["thresh"] = (
        weekday_table["abs_D"].rolling(lookback_pct, min_periods=lookback_pct)
        .quantile(top_decile)
    )

    intents: list[TradeIntent] = []
    for date_est, row in weekday_table.iterrows():
        if np.isnan(row["thresh"]):
            continue
        if row["abs_D"] < row["thresh"]:
            continue
        win_dir = np.sign(row[1200] - row[1155])
        d_dir = np.sign(row["D"])
        if win_dir == 0 or d_dir == 0:
            continue
        if win_dir != d_dir:
            continue

        direction = int(-d_dir)
        date_ts = pd.Timestamp(date_est)
        if date_ts.tzinfo is None:
            date_ts = date_ts.tz_localize(EST_FIXED)
        entry_ts = date_ts + pd.Timedelta("12:01:00")
        time_stop_ts = date_ts + pd.Timedelta("13:00:00")

        if direction > 0:
            stop = row["win_low"] - 3 * PIP
        else:
            stop = row["win_high"] + 3 * PIP

        target = row[1120]

        intents.append(
            TradeIntent(
                entry_ts=entry_ts,
                direction=direction,
                stop=stop,
                target=target,
                time_stop_ts=time_stop_ts,
                tag="R1_LDN4PM",
            )
        )

    return intents


def run(path: str, spread_pips: float = 0.5) -> None:
    print(f"Loading data: {path}")
    df = load_eurusd_m1(path)
    print(f"  Rows: {len(df):,}  Span: {df.index[0]} -> {df.index[-1]}")

    intents = build_intents(df)
    print(f"  Candidate trades: {len(intents):,}")

    trades = simulate(df, intents)
    trades_net = apply_cost(trades, spread_pips=spread_pips)

    print("\n--- R1 LDN 4PM Fix Drift Reversion (gross, no cost) ---")
    for k, v in report(trades, "R1_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R1 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R1_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r01_ldn_4pm_fix.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
