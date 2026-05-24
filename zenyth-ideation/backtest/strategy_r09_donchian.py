"""
Round 9: HeavyTail_Donchian60_Trend_ATRTrail (Class B)

Always-on trend-following on M1. Single position at a time.
- Long entry: close[t] > rolling60 high of [t-60..t-1] (prior-bar high; no foresight).
- Short entry: close[t] < rolling60 low of [t-60..t-1].
- Initial stop: entry -/+ 1.0 * ATR(60, t)
- Trail: max_close_since_entry -/+ 1.5 * ATR(60, current bar), one-way ratchet.
- No fixed target; no fixed time stop.
- New opposite signal closes current and opens new (but with one-bar gap to avoid same-bar reversal).

We stream bar-by-bar (no vectorized shortcut) for fidelity to the trail logic.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data_loader import load_eurusd_m1, atr  # noqa: E402
from harness import report, report_by_year, apply_cost, PIP  # noqa: E402


def run_donchian(df: pd.DataFrame, n: int = 60, init_atr_k: float = 1.0, trail_atr_k: float = 1.5) -> pd.DataFrame:
    """Run the streaming Donchian breakout strategy.

    Returns a trades DataFrame compatible with harness.report().
    """
    # Pre-compute series.
    high = df["high"].to_numpy()
    low = df["low"].to_numpy()
    close = df["close"].to_numpy()
    open_ = df["open"].to_numpy()
    atr_n = atr(df, n).to_numpy()

    # Rolling prior-bar high/low: shifted to avoid look-ahead.
    rh = df["high"].rolling(n, min_periods=n).max().shift(1).to_numpy()
    rl = df["low"].rolling(n, min_periods=n).min().shift(1).to_numpy()

    idx = df.index
    N = len(df)

    state = 0           # 0 flat, +1 long, -1 short
    entry_i = -1
    entry_price = np.nan
    stop = np.nan
    trail_extreme = np.nan

    trades = []

    for t in range(n + 1, N):
        if np.isnan(rh[t]) or np.isnan(rl[t]) or np.isnan(atr_n[t]):
            continue

        # --- Check exit first (intrabar) if in position ---
        if state != 0:
            # Update trail BEFORE checking stop (trail uses prior-bar info; here we update
            # using the current bar's extreme after the fact — conservative variant below).
            if state == +1:
                if low[t] <= stop:
                    # Stop hit this bar
                    exit_price = stop
                    pnl_price = exit_price - entry_price
                    risk_price = entry_price - (entry_price - init_atr_k * atr_n[entry_i])
                    trades.append({
                        "entry_ts": idx[entry_i],
                        "exit_ts": idx[t],
                        "direction": +1,
                        "entry": entry_price,
                        "exit": exit_price,
                        "stop": entry_price - init_atr_k * atr_n[entry_i],
                        "target": np.nan,
                        "exit_reason": "stop",
                        "pnl_price": pnl_price,
                        "pnl_pips": pnl_price / PIP,
                        "risk_pips": risk_price / PIP,
                        "r_multiple": pnl_price / risk_price if risk_price > 0 else 0.0,
                        "tag": "R9_DON",
                    })
                    state = 0
                else:
                    trail_extreme = max(trail_extreme, high[t])
                    new_trail = trail_extreme - trail_atr_k * atr_n[t]
                    if new_trail > stop:
                        stop = new_trail
            else:  # state == -1
                if high[t] >= stop:
                    exit_price = stop
                    pnl_price = entry_price - exit_price
                    risk_price = (entry_price + init_atr_k * atr_n[entry_i]) - entry_price
                    trades.append({
                        "entry_ts": idx[entry_i],
                        "exit_ts": idx[t],
                        "direction": -1,
                        "entry": entry_price,
                        "exit": exit_price,
                        "stop": entry_price + init_atr_k * atr_n[entry_i],
                        "target": np.nan,
                        "exit_reason": "stop",
                        "pnl_price": pnl_price,
                        "pnl_pips": pnl_price / PIP,
                        "risk_pips": risk_price / PIP,
                        "r_multiple": pnl_price / risk_price if risk_price > 0 else 0.0,
                        "tag": "R9_DON",
                    })
                    state = 0
                else:
                    trail_extreme = min(trail_extreme, low[t])
                    new_trail = trail_extreme + trail_atr_k * atr_n[t]
                    if new_trail < stop:
                        stop = new_trail

        # --- Check entry (if flat after possible exit) ---
        if state == 0:
            if close[t] > rh[t]:
                state = +1
                entry_i = t
                entry_price = close[t]
                stop = entry_price - init_atr_k * atr_n[t]
                trail_extreme = high[t]
            elif close[t] < rl[t]:
                state = -1
                entry_i = t
                entry_price = close[t]
                stop = entry_price + init_atr_k * atr_n[t]
                trail_extreme = low[t]

    # Close any open trade at last bar.
    if state != 0:
        exit_price = close[-1]
        if state == +1:
            pnl_price = exit_price - entry_price
            risk_price = init_atr_k * atr_n[entry_i]
        else:
            pnl_price = entry_price - exit_price
            risk_price = init_atr_k * atr_n[entry_i]
        trades.append({
            "entry_ts": idx[entry_i],
            "exit_ts": idx[-1],
            "direction": state,
            "entry": entry_price,
            "exit": exit_price,
            "stop": stop,
            "target": np.nan,
            "exit_reason": "time",
            "pnl_price": pnl_price,
            "pnl_pips": pnl_price / PIP,
            "risk_pips": risk_price / PIP,
            "r_multiple": pnl_price / risk_price if risk_price > 0 else 0.0,
            "tag": "R9_DON",
        })

    return pd.DataFrame(trades)


def run(path: str, spread_pips: float = 0.5) -> None:
    print(f"Loading data: {path}")
    df = load_eurusd_m1(path)
    print(f"  Rows: {len(df):,}")

    trades = run_donchian(df)
    trades_net = apply_cost(trades, spread_pips=spread_pips)

    print("\n--- R9 Donchian-60 Trend ATR Trail (gross) ---")
    for k, v in report(trades, "R9_gross").items():
        print(f"  {k}: {v}")

    print(f"\n--- R9 net of {spread_pips} pip spread ---")
    for k, v in report(trades_net, f"R9_net_{spread_pips}p").items():
        print(f"  {k}: {v}")

    print("\n--- By year ---")
    print(report_by_year(trades_net))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python strategy_r09_donchian.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5
    run(sys.argv[1], spread_pips=spread)
