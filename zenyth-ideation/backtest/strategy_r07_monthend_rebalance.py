"""
Round 7: MonthEnd_WMR_Rebalance_PreDrift (Class A)

Last business day of each month.
M = close(eom 09:00 EST) - open(bom 03:00 EST)
If |M| >= 0.5 * ATR(20, daily) -> direction = sign(M), enter at eom 09:01 EST.
Stop:   entry - direction * ATR_daily / 50
Target: eom 11:55 EST close (time-based; capture pre-fix accumulation).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, daily_atr, EST_FIXED  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


def _last_business_day(month_index: pd.DatetimeIndex) -> pd.Timestamp | None:
    """Return the last weekday (Mon-Fri) within the given index."""
    weekdays = month_index[month_index.weekday < 5]
    if len(weekdays) == 0:
        return None
    return weekdays[-1]


def _first_business_day(month_index: pd.DatetimeIndex) -> pd.Timestamp | None:
    weekdays = month_index[month_index.weekday < 5]
    if len(weekdays) == 0:
        return None
    return weekdays[0]


def build_intents(df: pd.DataFrame, atr_n: int = 20, magnitude_k: float = 0.5) -> list[TradeIntent]:
    """Build trade intents for R7 month-end pre-fix accumulation."""
    df = df.copy()
    df["date"] = df.index.normalize()
    df["hhmm"] = df.index.strftime("%H%M").astype(int)
    df["month_yyyymm"] = df.index.strftime("%Y%m").astype(int)
    atr_d = daily_atr(df, atr_n)

    intents: list[TradeIntent] = []
    for month, group in df.groupby("month_yyyymm"):
        unique_dates = pd.DatetimeIndex(group["date"].unique())
        bom_date = _first_business_day(unique_dates)
        eom_date = _last_business_day(unique_dates)
        if bom_date is None or eom_date is None or bom_date == eom_date:
            continue

        bom_0300 = group[(group["date"] == bom_date) & (group["hhmm"] == 300)]
        eom_0900 = group[(group["date"] == eom_date) & (group["hhmm"] == 900)]
        eom_0901 = group[(group["date"] == eom_date) & (group["hhmm"] == 901)]
        eom_1155 = group[(group["date"] == eom_date) & (group["hhmm"] == 1155)]
        if bom_0300.empty or eom_0900.empty or eom_0901.empty or eom_1155.empty:
            continue

        p_bom = float(bom_0300["open"].iloc[0])
        p_eom = float(eom_0900["close"].iloc[0])
        M = p_eom - p_bom

        # Get daily ATR for the day BEFORE eom
        eom_idx = atr_d.index.searchsorted(eom_date)
        if eom_idx <= 0:
            continue
        atr_val = float(atr_d.iat[eom_idx - 1])
        if np.isnan(atr_val) or atr_val <= 0:
            continue
        if abs(M) < magnitude_k * atr_val:
            continue
        direction = int(np.sign(M))
        if direction == 0:
            continue
        entry_open = float(eom_0901["open"].iloc[0])
        stop = entry_open - direction * (atr_val / 50.0)
        ts_entry = eom_date + pd.Timedelta("09:01:00")
        ts_stop = eom_date + pd.Timedelta("11:55:00")
        if ts_entry.tzinfo is None:
            ts_entry = ts_entry.tz_localize(EST_FIXED)
            ts_stop = ts_stop.tz_localize(EST_FIXED)

        intents.append(
            TradeIntent(
                entry_ts=ts_entry,
                direction=direction,
                stop=stop,
                target=None,  # time-stop only
                time_stop_ts=ts_stop,
                tag="R7_MONTHEND",
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

    print("\n--- R7 Month-end pre-fix accumulation (gross) ---")
    for k, v in report(trades, "R7_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R7 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R7_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r07_monthend_rebalance.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
