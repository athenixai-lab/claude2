"""
Round 24: London_AsianRange_StopCluster_Reversion (Class A)

Asian range = max(high), min(low) for 18:00 prev day .. 02:00 EST today.
Watch window 02:00-04:00 EST: find first bar whose high > AH + 3 pips and close < AH
(long sweep — flush of buy stops above), or mirror low sweep.
Enter NEXT bar open in opposite direction; stop at sweep extreme + 4 pips;
target opposite side of Asian range; time-stop 06:00 EST.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, EST_FIXED  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


SWEEP_BUFFER = 3 * PIP
STOP_BUFFER = 4 * PIP
MIN_ASIAN_RANGE = 8 * PIP
MAX_ASIAN_RANGE = 100 * PIP


def build_intents(df: pd.DataFrame) -> list[TradeIntent]:
    df = df.copy()
    df["date"] = df.index.normalize()
    df["hhmm"] = df.index.strftime("%H%M").astype(int)
    df["weekday"] = df.index.weekday

    intents: list[TradeIntent] = []
    unique_dates = pd.DatetimeIndex(sorted(df["date"].unique()))

    for d in unique_dates:
        if d.weekday() not in (0, 1, 2, 3, 4):
            continue
        asian_start = d - pd.Timedelta(days=1) + pd.Timedelta("18:00:00")
        asian_end = d + pd.Timedelta("02:00:00")
        if asian_start.tzinfo is None:
            asian_start = asian_start.tz_localize(EST_FIXED)
            asian_end = asian_end.tz_localize(EST_FIXED)

        asian_bars = df.loc[asian_start:asian_end]
        if len(asian_bars) < 60:
            continue
        AH = float(asian_bars["high"].max())
        AL = float(asian_bars["low"].min())
        asian_range = AH - AL
        if not (MIN_ASIAN_RANGE <= asian_range <= MAX_ASIAN_RANGE):
            continue

        watch_start = d + pd.Timedelta("02:00:00")
        watch_end = d + pd.Timedelta("04:00:00")
        if watch_start.tzinfo is None:
            watch_start = watch_start.tz_localize(EST_FIXED)
            watch_end = watch_end.tz_localize(EST_FIXED)
        watch = df.loc[watch_start:watch_end]
        if watch.empty:
            continue

        sweep_idx = None
        sweep_dir = 0
        sweep_extreme = np.nan
        for ts, bar in watch.iterrows():
            if bar["high"] > AH + SWEEP_BUFFER and bar["close"] < AH:
                sweep_idx = ts
                sweep_dir = -1  # entered short after long-sweep
                sweep_extreme = float(bar["high"])
                break
            if bar["low"] < AL - SWEEP_BUFFER and bar["close"] > AL:
                sweep_idx = ts
                sweep_dir = +1  # entered long after short-sweep
                sweep_extreme = float(bar["low"])
                break

        if sweep_idx is None:
            continue

        # Entry at next minute
        entry_ts = sweep_idx + pd.Timedelta(minutes=1)
        if entry_ts not in df.index:
            continue
        entry_open = float(df.loc[entry_ts, "open"])
        if sweep_dir > 0:
            stop = sweep_extreme - STOP_BUFFER
            target = AH
        else:
            stop = sweep_extreme + STOP_BUFFER
            target = AL
        time_stop = d + pd.Timedelta("06:00:00")
        if time_stop.tzinfo is None:
            time_stop = time_stop.tz_localize(EST_FIXED)

        intents.append(
            TradeIntent(
                entry_ts=entry_ts,
                direction=sweep_dir,
                stop=stop,
                target=target,
                time_stop_ts=time_stop,
                tag="R24_LDN_SWEEP",
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

    print("\n--- R24 London Asian-range stop-sweep reversion (gross) ---")
    for k, v in report(trades, "R24_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R24 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R24_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r24_london_sweep.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
