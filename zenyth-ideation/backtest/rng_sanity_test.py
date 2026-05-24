"""
RNG Sanity Test: runs a strategy against three synthetic candle generators
and reports PASS/FAIL based on expected RNG behavior.

Usage:
    python rng_sanity_test.py <strategy_id> <real_data_csv> [--n-seeds 5]

Strategy IDs supported:
    r01   — LDN 4pm fix drift reversion (Class A; should LOSE on all RNG modes)
    r09   — Donchian 60 trend (Class B; should LOSE on Gaussian/shuffled, WIN on block-bootstrap)
    r18   — Microstructure 1-bar bounce (Class B; should LOSE on Gaussian/shuffled, WIN on block-bootstrap)

Expected results for each RNG mode:
    gaussian_rw         — EV ≈ 0 for everything (Doob).
    shuffled_returns    — EV ≈ 0 for AR-dependent strategies (R9, R18). Marginal-dependent
                          strategies (none in current set) could have EV > 0.
    block_bootstrap     — EV ≈ 0 for calendar strategies (R1). EV > 0 for AR strategies (R9, R18).

The test runs N seeds per mode and reports mean / std of per-trade EV in R.
A strategy 'PASSES' if its mean EV matches the expectation pattern qualitatively.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from data_loader import load_eurusd_m1  # noqa: E402
from harness import simulate, report, apply_cost  # noqa: E402
from rng_generators import generate, GeneratorMode  # noqa: E402

import strategy_r01_ldn_4pm_fix as r01  # noqa: E402
import strategy_r09_donchian as r09  # noqa: E402
import strategy_r18_microbounce as r18  # noqa: E402


STRATEGY_MAP: dict[str, dict] = {
    "r01": {
        "class": "A",
        "expected": {
            "gaussian_rw": "≈ 0",
            "shuffled_returns": "≈ 0",
            "block_bootstrap": "≈ 0 (calendar destroyed)",
        },
        "is_intent_based": True,
        "build": lambda df: r01.build_intents(df),
        "label": "R1 LDN 4pm fix",
    },
    "r09": {
        "class": "B",
        "expected": {
            "gaussian_rw": "≈ 0 (Doob)",
            "shuffled_returns": "≈ 0 (AR destroyed)",
            "block_bootstrap": "> 0 (AR preserved)",
        },
        "is_intent_based": False,
        "build": lambda df: r09.run_donchian(df),
        "label": "R9 Donchian-60",
    },
    "r18": {
        "class": "B",
        "expected": {
            "gaussian_rw": "≈ 0 (Doob)",
            "shuffled_returns": "≈ 0 (AR destroyed)",
            "block_bootstrap": "> 0 (AR preserved)",
        },
        "is_intent_based": True,
        "build": lambda df: r18.build_intents(df),
        "label": "R18 Micro bounce",
    },
}

MODES: list[GeneratorMode] = ["gaussian_rw", "shuffled_returns", "block_bootstrap"]


def run_one(strategy_id: str, df: pd.DataFrame, spread_pips: float = 0.5) -> dict:
    spec = STRATEGY_MAP[strategy_id]
    if spec["is_intent_based"]:
        intents = spec["build"](df)
        trades = simulate(df, intents)
    else:
        trades = spec["build"](df)
    trades_net = apply_cost(trades, spread_pips=spread_pips)
    rep = report(trades_net)
    return rep


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("strategy_id", choices=sorted(STRATEGY_MAP.keys()))
    parser.add_argument("real_data_csv")
    parser.add_argument("--n-seeds", type=int, default=3,
                        help="Number of seeds per RNG mode (more = lower noise; default 3)")
    parser.add_argument("--spread-pips", type=float, default=0.5)
    parser.add_argument("--max-bars", type=int, default=None,
                        help="Optional cap on bars used (for speed during dev)")
    args = parser.parse_args()

    spec = STRATEGY_MAP[args.strategy_id]
    print("=" * 72)
    print(f"RNG SANITY TEST — {spec['label']} (Class {spec['class']})")
    print("=" * 72)

    print(f"\nLoading reference data: {args.real_data_csv}")
    df_real = load_eurusd_m1(args.real_data_csv)
    if args.max_bars is not None:
        df_real = df_real.iloc[:args.max_bars]
    print(f"  Loaded {len(df_real):,} bars")

    # --- Real data baseline ---
    print("\n--- Real data baseline ---")
    rep_real = run_one(args.strategy_id, df_real, spread_pips=args.spread_pips)
    print(f"  trades={rep_real.get('trades', 0)}  "
          f"mean_R={rep_real.get('mean_R', float('nan')):.4f}  "
          f"PF={rep_real.get('profit_factor', float('nan')):.3f}")

    # --- RNG modes ---
    results: dict[str, list[dict]] = {m: [] for m in MODES}
    for mode in MODES:
        print(f"\n--- RNG: {mode}  (expected: {spec['expected'][mode]}) ---")
        for seed in range(args.n_seeds):
            df_syn = generate(mode, df_real, seed=seed)
            rep = run_one(args.strategy_id, df_syn, spread_pips=args.spread_pips)
            results[mode].append(rep)
            print(f"  seed={seed}  trades={rep.get('trades', 0)}  "
                  f"mean_R={rep.get('mean_R', float('nan')):.4f}  "
                  f"PF={rep.get('profit_factor', float('nan')):.3f}")

    # --- Summary table ---
    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"{'mode':<25} {'mean_R_mean':>12} {'mean_R_std':>12} {'PF_mean':>10}")
    for mode in MODES:
        rs = [r.get("mean_R", 0.0) for r in results[mode] if r.get("trades", 0) > 0]
        pfs = [r.get("profit_factor", 1.0) for r in results[mode] if r.get("trades", 0) > 0]
        if rs:
            print(f"{mode:<25} {np.mean(rs):>12.4f} {np.std(rs):>12.4f} {np.mean(pfs):>10.3f}")
        else:
            print(f"{mode:<25} {'-':>12} {'-':>12} {'-':>10}")
    print(f"{'REAL':<25} {rep_real.get('mean_R', 0.0):>12.4f} {'-':>12} {rep_real.get('profit_factor', 1.0):>10.3f}")

    # --- Judgement ---
    # We compare each mode's EV to a NEGATIVE cost baseline. A strategy that
    # "fails RNG" (mean_R near or below cost baseline) is the expected outcome
    # for any strategy on pure martingale RNG. A strategy "passes" if it shows
    # real-data EV measurably ABOVE its block-bootstrap EV (calendar/structure
    # added value beyond the AR baseline).
    print("\nInterpretation (qualitative — compare against expectations above):")
    bb_rs = [r.get("mean_R", 0.0) for r in results["block_bootstrap"] if r.get("trades", 0) > 0]
    g_rs = [r.get("mean_R", 0.0) for r in results["gaussian_rw"] if r.get("trades", 0) > 0]
    real_r = rep_real.get("mean_R", 0.0)

    if g_rs:
        print(f"  Gaussian RW EV={np.mean(g_rs):+.4f} R/trade — this is the cost-only baseline; "
              f"any strategy on pure RW returns ~this (Doob).")
    if bb_rs:
        diff_bb_vs_g = np.mean(bb_rs) - np.mean(g_rs) if g_rs else 0
        if diff_bb_vs_g > 0.05:
            print(f"  Block-bootstrap EV={np.mean(bb_rs):+.4f} > Gaussian by {diff_bb_vs_g:+.4f} — "
                  f"AR / fat-tail structure IS providing edge (Class B success).")
        else:
            print(f"  Block-bootstrap EV={np.mean(bb_rs):+.4f} ≈ Gaussian — "
                  f"AR / fat-tail structure not providing measurable edge in this sample "
                  f"(reference data may be Gaussian-like).")

    diff_real_vs_bb = real_r - np.mean(bb_rs) if bb_rs else 0
    if abs(diff_real_vs_bb) > 0.05:
        sign = "ABOVE" if diff_real_vs_bb > 0 else "BELOW"
        print(f"  Real-data EV={real_r:+.4f} is {sign} block-bootstrap by {diff_real_vs_bb:+.4f} — "
              f"calendar/non-stationarity {'adds' if diff_real_vs_bb > 0 else 'removes'} edge beyond the AR baseline.")
    else:
        print(f"  Real-data EV={real_r:+.4f} ≈ block-bootstrap — "
              f"calendar/non-stationarity is not the source of edge in this sample.")

    # Class-specific interpretations
    if spec["class"] == "A":
        print(f"\n  CLASS A interpretation: edge should be REAL>>BB and REAL>>SHUFFLE. "
              f"If real EV is not measurably above bootstrap, the calendar mechanism is not "
              f"adding value (kill the candidate).")
    else:
        print(f"\n  CLASS B interpretation: edge should be BB>>GAUSS (AR carries the edge). "
              f"REAL ≈ BB means the strategy is doing what it was designed to do — "
              f"exploiting autocorrelation.")
    print()


if __name__ == "__main__":
    main()
