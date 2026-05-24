"""
Round 11: Weekend_Gap_Sunday_Open_Fill (Class A)

Trigger:
    Friday 16:59 EST close -> Sunday 17:05 EST close.
    Gap G = sun_5min_close - fri_close.
    Require |G| > 8 pips.
Entry:
    Sunday 17:06 EST open. Direction = -sign(G) (fade).
Stop:
    Sunday extreme in 17:00..17:05 + 4 pips.
Target:
    Friday close (fully fill the gap).
Time stop:
    Monday 03:00 EST (London open).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, EST_FIXED  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


MIN_GAP = 8 * PIP


def build_intents(df: pd.DataFrame) -> list[TradeIntent]:
    """Build intents for R11 weekend-gap-fade trades."""
    df = df.copy()
    df["hhmm"] = df.index.strftime("%H%M").astype(int)
    df["weekday"] = df.index.weekday

    # Friday 16:59 closes
    fri_close = (
        df[(df["weekday"] == 4) & (df["hhmm"] == 1659)]
        .assign(date=lambda x: x.index.normalize())
        .set_index("date")["close"]
    )
    # Sunday 17:00..17:05 high/low/close
    sun_window = df[(df["weekday"] == 6) & (df["hhmm"].between(1700, 1705))].copy()
    sun_window["date"] = sun_window.index.normalize()
    sun_extremes = sun_window.groupby("date").agg(sun_high=("high", "max"),
                                                  sun_low=("low", "min"),
                                                  sun_close=("close", "last"))
    sun_open_1706 = (
        df[(df["weekday"] == 6) & (df["hhmm"] == 1706)]
        .assign(date=lambda x: x.index.normalize())
        .set_index("date")["open"]
        .rename("open_1706")
    )
    sun_table = sun_extremes.join(sun_open_1706, how="inner")

    intents: list[TradeIntent] = []
    for sun_date, row in sun_table.iterrows():
        # Find the previous Friday
        prev_fri = sun_date - pd.Timedelta(days=2)
        if prev_fri not in fri_close.index:
            continue
        fc = float(fri_close.loc[prev_fri])
        sc = float(row["sun_close"])
        G = sc - fc
        if abs(G) < MIN_GAP:
            continue
        direction = int(-np.sign(G))
        if direction == 0:
            continue
        entry = float(row["open_1706"])
        if direction > 0:
            stop = float(row["sun_low"]) - 4 * PIP
        else:
            stop = float(row["sun_high"]) + 4 * PIP
        target = fc
        ts_entry = sun_date + pd.Timedelta("17:06:00")
        # Monday is sun_date + 1 day
        ts_stop = (sun_date + pd.Timedelta(days=1)) + pd.Timedelta("03:00:00")
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
                tag="R11_GAP",
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

    print("\n--- R11 Weekend Gap Fade (gross) ---")
    for k, v in report(trades, "R11_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R11 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R11_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r11_weekend_gap.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
