"""
Round 5: Options_1000NY_Cut_Pin_Magnet (Class A)

Trigger:
    At 09:00 EST, find nearest 50-pip strike K.
    Require 5 <= |entry - K| <= 20 pips.
Entry:
    At 09:01 EST open. Direction toward K.
Stop:
    entry - direction * 2.5 * |delta| (wide; gives pin room).
Target:
    K (touch the strike).
Time stop:
    10:00 EST (NY options cut).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, EST_FIXED  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


def nearest_strike(price: float, grid_pips: float = 50.0) -> float:
    """Snap price to nearest grid (default 50-pip)."""
    grid = grid_pips * PIP
    return round(price / grid) * grid


def build_intents(df: pd.DataFrame,
                  grid_pips: float = 50.0,
                  min_delta_pips: float = 5.0,
                  max_delta_pips: float = 20.0,
                  stop_mult: float = 2.5) -> list[TradeIntent]:
    """Build intents for R5 cut-window pin trades."""
    df = df.copy()
    df["hhmm"] = df.index.strftime("%H%M").astype(int)
    df["date_est"] = df.index.normalize()
    df["weekday"] = df.index.weekday

    # Build a per-date lookup of the 09:01 EST open price.
    open_0901_by_date = (
        df[df["hhmm"] == 901]
        .assign(date=lambda x: x.index.normalize())
        .set_index("date")["open"]
    )
    intents: list[TradeIntent] = []

    for ts0900, row in df[df["hhmm"] == 900].iterrows():
        date_est = ts0900.normalize()
        if date_est not in open_0901_by_date.index:
            continue
        weekday = ts0900.weekday()
        if weekday >= 5:
            continue

        p0 = float(row["close"])
        K = nearest_strike(p0, grid_pips)
        delta = K - p0
        if not (min_delta_pips * PIP <= abs(delta) <= max_delta_pips * PIP):
            continue
        direction = int(np.sign(delta))
        if direction == 0:
            continue
        entry = float(open_0901_by_date.loc[date_est])
        stop = entry - direction * stop_mult * abs(delta)
        target = K
        ts_entry = date_est + pd.Timedelta("09:01:00")
        ts_stop = date_est + pd.Timedelta("10:00:00")
        if ts_entry.tzinfo is None:
            ts_entry = ts_entry.tz_localize(EST_FIXED)
            ts_stop = ts_stop.tz_localize(EST_FIXED)

        intents.append(
            TradeIntent(
                entry_ts=ts_entry,
                direction=direction,
                stop=stop,
                target=target,
                time_stop_ts=ts_stop,
                tag="R5_OPTPIN",
            )
        )

    return intents


def run(path: str, spread_pips: float = 0.5) -> None:
    print(f"Loading data: {path}")
    df = load_eurusd_m1(path)
    print(f"  Rows: {len(df):,}")

    intents = build_intents(df)
    print(f"  Candidate trades: {len(intents):,}")

    trades = simulate(df, intents)
    trades_net = apply_cost(trades, spread_pips=spread_pips)

    print("\n--- R5 Options-Cut Pin Magnet (gross) ---")
    for k, v in report(trades, "R5_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R5 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R5_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r05_options_pin.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
