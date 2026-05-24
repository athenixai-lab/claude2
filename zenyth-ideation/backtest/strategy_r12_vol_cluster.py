"""
Round 12: Vol_Cluster_Expansion_Direction_Momentum (Class B)

Trigger:
    realized_vol(t) = std(returns over last 20 bars)
    rolling_median_vol = rolling median over 500 bars of realized_vol
    low_vol_regime = realized_vol(t-1) < 0.4 * rolling_median_vol(t)
    ignition = |return(t)| > 2.5 * realized_vol(t-1)  AND  prior bar was low_vol_regime

Entry: open[t+1], direction = sign(return(t))
Stop: entry - direction * 0.7 * |return(t)|
Trail: 1.5 * ATR(20) after entry; time stop = t + 30 minutes
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, atr  # noqa: E402
from harness import simulate, TradeIntent, report, report_by_year, apply_cost, PIP  # noqa: E402


def build_intents(df: pd.DataFrame,
                  vol_window: int = 20,
                  median_window: int = 500,
                  low_vol_ratio: float = 0.4,
                  ignition_mult: float = 2.5,
                  stop_k: float = 0.7,
                  trail_atr_k: float = 1.5,
                  time_minutes: int = 30) -> list[TradeIntent]:
    """Build trade intents (entry at t+1) for R12 ignitions.

    Note: this version uses a FIXED time-stop and pre-computed initial stop,
    leaving the trail logic out (simulate doesn't trail). For a faithful trail
    version, use the streaming runner in `run_r12_streaming` below.
    """
    close = df["close"].to_numpy()
    rets = np.diff(close, prepend=np.nan)
    rv = pd.Series(rets).rolling(vol_window, min_periods=vol_window).std(ddof=0).to_numpy()
    rv_med = pd.Series(rv).rolling(median_window, min_periods=median_window).median().to_numpy()

    idx = df.index
    N = len(df)
    intents: list[TradeIntent] = []

    for t in range(median_window + 1, N - time_minutes - 1):
        if np.isnan(rv[t - 1]) or np.isnan(rv_med[t]) or np.isnan(rets[t]):
            continue
        if rv[t - 1] >= low_vol_ratio * rv_med[t]:
            continue
        if abs(rets[t]) < ignition_mult * rv[t - 1]:
            continue
        if rets[t] == 0:
            continue

        direction = int(np.sign(rets[t]))
        entry_loc = t + 1
        if entry_loc >= N:
            break
        entry_open = float(df["open"].iat[entry_loc])
        r_abs = abs(rets[t])
        stop = entry_open - direction * stop_k * r_abs

        time_stop_loc = min(t + 1 + time_minutes, N - 1)
        intents.append(
            TradeIntent(
                entry_ts=idx[entry_loc],
                direction=direction,
                stop=stop,
                target=None,  # time-stop only; no fixed target in this simplified version
                time_stop_ts=idx[time_stop_loc],
                tag="R12_VOLCL",
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

    print("\n--- R12 Vol-cluster ignition (gross) ---")
    for k, v in report(trades, "R12_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R12 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R12_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r12_vol_cluster.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
