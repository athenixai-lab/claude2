"""
Round 18: Microstructure_OneBar_OverReaction_Fade (Class B)

For each bar t:
    sigma = std(close diffs over [t-30..t-1])
    if |close[t] - close[t-1]| < 3*sigma: skip
    direction = -sign(close[t] - close[t-1])
    entry  = open[t+1]
    stop   = entry - direction * 0.8 * |ret_t|
    target = entry + direction * 0.5 * |ret_t|
    time_stop = t + 5 bars (i.e., bar t+6 close exits)

Cost-sensitivity is the load-bearing test. Default spread 0.5 pips.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, EST_FIXED  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


def build_intents(df: pd.DataFrame, sigma_lookback: int = 30, sigma_mult: float = 3.0,
                  stop_k: float = 0.8, target_k: float = 0.5, time_bars: int = 5) -> list[TradeIntent]:
    """Build TradeIntents from M1 OHLC."""
    close = df["close"].to_numpy()
    rets = np.diff(close, prepend=np.nan)
    # rolling std of returns
    s = pd.Series(rets).rolling(sigma_lookback, min_periods=sigma_lookback).std(ddof=0)
    sigma = s.to_numpy()

    abs_r = np.abs(rets)
    cond = (abs_r > sigma_mult * sigma)
    idx = df.index
    N = len(df)

    intents: list[TradeIntent] = []
    for t in range(sigma_lookback + 1, N - time_bars - 1):
        if not cond[t]:
            continue
        if rets[t] == 0:
            continue
        # entry at next bar open
        entry_loc = t + 1
        if entry_loc >= N:
            break
        entry_ts = idx[entry_loc]
        time_stop_ts = idx[min(t + time_bars + 1, N - 1)]
        direction = int(-np.sign(rets[t]))
        entry_open = float(df["open"].iat[entry_loc])
        r_abs = abs(rets[t])
        stop = entry_open - direction * stop_k * r_abs
        target = entry_open + direction * target_k * r_abs

        intents.append(
            TradeIntent(
                entry_ts=entry_ts,
                direction=direction,
                stop=stop,
                target=target,
                time_stop_ts=time_stop_ts,
                tag="R18_MICRO",
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

    print("\n--- R18 Micro 1-bar bounce (gross) ---")
    for k, v in report(trades, "R18_gross").items():
        print(f"  {k}: {v}")

    for sp in [0.3, 0.5, 0.8, 1.0, 1.5]:
        trades_c = apply_cost(trades, spread_pips=sp)
        rep = report(trades_c, f"R18_net_{sp}p")
        print(f"\n--- R18 net of {sp} pip spread ---")
        for k, v in rep.items():
            print(f"  {k}: {v}")

    print("\n--- By year (at 0.5 pip cost) ---")
    print(report_by_year(apply_cost(trades, 0.5)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r18_microbounce.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
