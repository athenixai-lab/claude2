"""
Round 30 implementation: combine trades from multiple strategies into a single
portfolio PnL series, with inverse-vol weighting.

Usage (in code):
    from portfolio_combine import combine
    portfolio = combine({
        "R1": r01_trades_df,
        "R9": r09_trades_df,
        "R18": r18_trades_df,
    })

Or from CLI to run all three strategies on a CSV and report aggregate:

    python portfolio_combine.py <EURUSD_M1.csv> [spread_pips]
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from data_loader import load_eurusd_m1  # noqa: E402
from harness import simulate, report, apply_cost  # noqa: E402

import strategy_r01_ldn_4pm_fix as r01  # noqa: E402
import strategy_r09_donchian as r09  # noqa: E402
import strategy_r12_vol_cluster as r12  # noqa: E402
import strategy_r18_microbounce as r18  # noqa: E402


def _compute_per_strategy_pnl_series(trades: pd.DataFrame, dates: pd.DatetimeIndex) -> pd.Series:
    """Convert per-trade DF into a per-day pnl_pips series indexed by exit date."""
    if trades.empty:
        return pd.Series(0.0, index=dates)
    t = trades.copy()
    t["exit_date"] = pd.to_datetime(t["exit_ts"]).dt.normalize()
    daily = t.groupby("exit_date")["pnl_pips"].sum()
    return daily.reindex(dates, fill_value=0.0)


def combine(trades_by_name: dict[str, pd.DataFrame], dates: pd.DatetimeIndex | None = None,
            weighting: str = "inverse_vol") -> dict:
    """Combine trades from multiple strategies into a portfolio.

    Returns a dict with:
      - per_strategy_stats: dict[name -> report dict]
      - weights: dict[name -> weight]
      - pairwise_corr: DataFrame of daily PnL correlations
      - portfolio_pnl_daily: pd.Series of weighted daily PnL in pips
      - portfolio_stats: dict with aggregate stats
    """
    if dates is None:
        all_dates = []
        for trades in trades_by_name.values():
            if not trades.empty:
                all_dates.extend(pd.to_datetime(trades["exit_ts"]).dt.normalize().tolist())
        if not all_dates:
            return {"error": "no trades in any strategy"}
        dates = pd.DatetimeIndex(sorted(set(all_dates)))

    per_strategy_pnl = {name: _compute_per_strategy_pnl_series(t, dates)
                        for name, t in trades_by_name.items()}

    per_strategy_stats = {name: report(t, name) for name, t in trades_by_name.items()}

    daily_df = pd.DataFrame(per_strategy_pnl)
    pairwise_corr = daily_df.corr()

    # Inverse-vol weights
    if weighting == "inverse_vol":
        vols = daily_df.std()
        inv = 1.0 / vols.replace(0, np.nan)
        weights = (inv / inv.sum()).fillna(0.0).to_dict()
    elif weighting == "equal":
        weights = {name: 1.0 / len(trades_by_name) for name in trades_by_name}
    else:
        raise ValueError(f"unknown weighting: {weighting}")

    portfolio_pnl_daily = sum(per_strategy_pnl[name] * weights[name]
                              for name in trades_by_name)

    pnl = portfolio_pnl_daily.to_numpy()
    equity = pnl.cumsum()
    peak = np.maximum.accumulate(equity) if len(equity) else np.array([0.0])
    dd = equity - peak

    portfolio_stats = {
        "days": int((portfolio_pnl_daily != 0).sum()),
        "mean_pips_per_day": float(pnl.mean()) if len(pnl) else 0.0,
        "std_pips_per_day": float(pnl.std(ddof=0)) if len(pnl) else 0.0,
        "annualised_sharpe": float(pnl.mean() / pnl.std(ddof=0) * np.sqrt(252))
                              if pnl.std(ddof=0) > 0 else 0.0,
        "total_pips": float(pnl.sum()),
        "max_dd_pips": float(dd.min()) if len(dd) else 0.0,
    }

    return {
        "per_strategy_stats": per_strategy_stats,
        "weights": weights,
        "pairwise_corr": pairwise_corr,
        "portfolio_pnl_daily": portfolio_pnl_daily,
        "portfolio_stats": portfolio_stats,
    }


def main():
    if len(sys.argv) < 2:
        print("usage: python portfolio_combine.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    path = sys.argv[1]
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5

    print(f"Loading data: {path}")
    df = load_eurusd_m1(path)
    print(f"  Rows: {len(df):,}")

    print("\nRunning R1...")
    r1_trades = apply_cost(simulate(df, r01.build_intents(df)), spread_pips=spread)
    print(f"  R1: {len(r1_trades)} trades")

    print("Running R9...")
    r9_trades = apply_cost(r09.run_donchian(df), spread_pips=spread)
    print(f"  R9: {len(r9_trades)} trades")

    print("Running R12...")
    r12_trades = apply_cost(simulate(df, r12.build_intents(df)), spread_pips=spread)
    print(f"  R12: {len(r12_trades)} trades")

    print("Running R18...")
    r18_trades = apply_cost(simulate(df, r18.build_intents(df)), spread_pips=spread)
    print(f"  R18: {len(r18_trades)} trades")

    result = combine({
        "R1": r1_trades,
        "R9": r9_trades,
        "R12": r12_trades,
        "R18": r18_trades,
    })

    print("\n--- Per-strategy stats ---")
    for name, stats in result["per_strategy_stats"].items():
        print(f"\n[{name}]")
        for k in ("trades", "win_rate", "mean_R", "total_pips", "profit_factor", "max_dd_pips"):
            if k in stats:
                print(f"  {k}: {stats[k]}")

    print("\n--- Weights (inverse-vol) ---")
    for name, w in result["weights"].items():
        print(f"  {name}: {w:.4f}")

    print("\n--- Pairwise correlation (daily PnL) ---")
    print(result["pairwise_corr"].round(3))

    print("\n--- Portfolio aggregate ---")
    for k, v in result["portfolio_stats"].items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
