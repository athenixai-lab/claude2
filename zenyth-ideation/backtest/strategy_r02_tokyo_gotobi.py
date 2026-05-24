"""
Round 2: Tokyo_Gotobi_Fix_PreDrift (Class A)

Gotobi day = calendar day-of-month in {5,10,15,20,25} OR last business day of month (Tokyo).
On the EST date prior to a Gotobi day (because 09:55 JST = 19:55 EST previous day under
fixed UTC-5), measure pre-fix drift D = close(19:55) - close(19:30) on the EST evening.

If |D| >= 1.3 * mean(|D|) of last 30 valid Gotobi observations AND D < 0 (EURUSD-bear, which
is consistent with JPY-import USD-buy flow → fade by going LONG EURUSD):
    Enter long EURUSD at 19:56 EST open.
    Stop:   min(low) of 19:30..19:55 - 4 pips.
    Target: close(19:30).
    Time stop: 20:30 EST same day.
"""

from __future__ import annotations

import calendar
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, EST_FIXED  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


GOTOBI_DAYS = {5, 10, 15, 20, 25}


def is_gotobi_day_tokyo(d: pd.Timestamp) -> bool:
    """Tokyo calendar test."""
    if d.day in GOTOBI_DAYS:
        return True
    # Last calendar day approximation for end-of-month (use last day of month).
    last_day = calendar.monthrange(d.year, d.month)[1]
    return d.day == last_day


def build_intents(df: pd.DataFrame, mult: float = 1.3, lookback: int = 30) -> list[TradeIntent]:
    """Build intents for R2 Tokyo Gotobi pre-fix fade-long."""
    df = df.copy()
    df["date"] = df.index.normalize()
    df["hhmm"] = df.index.strftime("%H%M").astype(int)

    # We want EST_evening_date d-1 corresponding to Tokyo morning d.
    # Equivalent: any EST evening (~19:30-20:30) where (date(EST) + 1 day) is a Gotobi day in Tokyo.
    # Tokyo time at 19:30 EST = (19:30 + 14h = 09:30 next day). So Tokyo date = EST date + 1.

    intents: list[TradeIntent] = []
    abs_d_history: list[float] = []

    unique_dates = pd.DatetimeIndex(sorted(df["date"].unique()))
    for est_date in unique_dates:
        tokyo_date = est_date + pd.Timedelta(days=1)
        if not is_gotobi_day_tokyo(tokyo_date):
            continue
        if est_date.weekday() >= 5:  # skip Sat/Sun on EST
            continue

        day_bars = df[df["date"] == est_date]
        b_1930 = day_bars[day_bars["hhmm"] == 1930]
        b_1955 = day_bars[day_bars["hhmm"] == 1955]
        b_1956 = day_bars[day_bars["hhmm"] == 1956]
        win_bars = day_bars[(day_bars["hhmm"] >= 1930) & (day_bars["hhmm"] <= 1955)]
        if b_1930.empty or b_1955.empty or b_1956.empty or win_bars.empty:
            continue

        p_1930 = float(b_1930["close"].iloc[0])
        p_1955 = float(b_1955["close"].iloc[0])
        D = p_1955 - p_1930

        # Maintain rolling mean of |D| from PRIOR Gotobi observations (not including current).
        if len(abs_d_history) >= lookback:
            mean_abs = float(np.mean(abs_d_history[-lookback:]))
            if abs(D) >= mult * mean_abs and D < 0:
                entry_open = float(b_1956["open"].iloc[0])
                stop = float(win_bars["low"].min()) - 4 * PIP
                target = p_1930
                ts_entry = est_date + pd.Timedelta("19:56:00")
                ts_stop = est_date + pd.Timedelta("20:30:00")
                if ts_entry.tzinfo is None:
                    ts_entry = ts_entry.tz_localize(EST_FIXED)
                    ts_stop = ts_stop.tz_localize(EST_FIXED)
                intents.append(TradeIntent(
                    entry_ts=ts_entry,
                    direction=+1,
                    stop=stop,
                    target=target,
                    time_stop_ts=ts_stop,
                    tag="R2_GOTOBI",
                ))

        abs_d_history.append(abs(D))

    return intents


def run(path: str, spread_pips: float = 0.5) -> None:
    print(f"Loading data: {path}")
    df = load_eurusd_m1(path)
    print(f"  Rows: {len(df):,}")

    intents = build_intents(df)
    print(f"  Candidate trades: {len(intents):,}")

    trades = simulate(df, intents)
    trades_net = apply_cost(trades, spread_pips=spread_pips)

    print("\n--- R2 Tokyo Gotobi pre-fix fade (gross) ---")
    for k, v in report(trades, "R2_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R2 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R2_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r02_tokyo_gotobi.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
