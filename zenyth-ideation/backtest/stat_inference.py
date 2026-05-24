"""
Statistical inference tools for trade-level PnL series.

When you backtest a strategy and see "mean_R = +0.15", the question is always:
is that +0.15 the real edge, or just sampling noise from this particular dataset?

This module gives you the tools to answer.

Functions:
    bootstrap_mean_ci   — non-parametric confidence interval on mean R via resampling.
    p_value_against_zero — empirical one-sided p-value (mean R > 0).
    min_n_to_detect     — minimum trade count needed to detect a given effect size.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def bootstrap_mean_ci(r_multiples: np.ndarray | pd.Series,
                      n_iter: int = 10_000,
                      alpha: float = 0.05,
                      seed: int = 7) -> dict:
    """Bootstrap CI on the mean of per-trade R-multiples.

    Returns dict with:
        mean: point estimate of mean R
        ci_low / ci_high: alpha/2 .. 1-alpha/2 percentile of bootstrap distribution
        ci_level: nominal coverage (1 - alpha)
        n: sample size
        n_iter: number of bootstrap resamples
    """
    rng = np.random.default_rng(seed)
    r = np.asarray(r_multiples, dtype=float)
    n = len(r)
    if n < 10:
        return {
            "mean": float(r.mean()) if n else 0.0,
            "ci_low": float("nan"),
            "ci_high": float("nan"),
            "ci_level": 1 - alpha,
            "n": n,
            "n_iter": 0,
            "note": "sample too small (n<10) for bootstrap",
        }

    idx = rng.integers(0, n, size=(n_iter, n))
    boot_means = r[idx].mean(axis=1)

    lo = float(np.quantile(boot_means, alpha / 2))
    hi = float(np.quantile(boot_means, 1 - alpha / 2))
    return {
        "mean": float(r.mean()),
        "ci_low": lo,
        "ci_high": hi,
        "ci_level": 1 - alpha,
        "n": n,
        "n_iter": n_iter,
    }


def p_value_against_zero(r_multiples: np.ndarray | pd.Series,
                         n_iter: int = 10_000,
                         seed: int = 7) -> float:
    """One-sided permutation p-value for H0: E[R] = 0 vs. H1: E[R] > 0.

    Implementation: bootstrap the mean under H0 by shifting the sample to have mean 0,
    then resample. p-value = Pr[bootstrap_mean >= observed_mean].
    """
    r = np.asarray(r_multiples, dtype=float)
    if len(r) < 10:
        return float("nan")
    rng = np.random.default_rng(seed)
    obs = r.mean()
    centered = r - obs  # H0: mean 0
    boot = centered[rng.integers(0, len(r), size=(n_iter, len(r)))].mean(axis=1)
    return float((boot >= obs).mean())


def min_n_to_detect(effect_size_R: float, per_trade_sigma_R: float = 1.0,
                    alpha: float = 0.05, power: float = 0.80) -> int:
    """Approximate one-sided z-test sample size to detect effect_size_R at given alpha/power.

    N = ((z_{1-alpha} + z_{power}) * sigma / effect)^2
    """
    from math import erf, sqrt
    # Inverse-normal via approximation; for alpha=0.05 z=1.6449, power=0.80 z=0.8416
    z_alpha = 1.6449
    z_power = 0.8416
    if effect_size_R <= 0:
        return -1
    n = ((z_alpha + z_power) * per_trade_sigma_R / effect_size_R) ** 2
    return int(np.ceil(n))


def full_report(trades: pd.DataFrame) -> dict:
    """Run the full stats stack on a trades DataFrame."""
    if trades.empty:
        return {"error": "empty trades"}

    r = trades["r_multiple"].to_numpy(dtype=float)
    ci = bootstrap_mean_ci(r)
    p = p_value_against_zero(r)
    sigma_R = float(np.std(r, ddof=0))
    obs_mean = float(r.mean())

    min_n = min_n_to_detect(max(abs(obs_mean), 0.01), per_trade_sigma_R=sigma_R)
    sample_to_min = len(r) / min_n if min_n > 0 else float("nan")

    return {
        "n_trades": int(len(r)),
        "mean_R": obs_mean,
        "sigma_R": sigma_R,
        "ci_95_low": ci["ci_low"],
        "ci_95_high": ci["ci_high"],
        "p_value_vs_zero": p,
        "min_n_for_observed_effect_at_80pct_power": min_n,
        "sample_size_ratio": sample_to_min,
        "interpretation": _interpret(obs_mean, ci, p),
    }


def _interpret(mean: float, ci: dict, p: float) -> str:
    notes = []
    if ci.get("ci_low", float("nan")) > 0:
        notes.append("95% CI excludes zero — observed edge is statistically significant")
    elif ci.get("ci_high", float("nan")) < 0:
        notes.append("95% CI excludes zero NEGATIVELY — strategy is significantly LOSING")
    else:
        notes.append("95% CI includes zero — observed edge is NOT statistically distinguishable from noise")

    if not np.isnan(p):
        if p < 0.01:
            notes.append(f"p={p:.4f} < 0.01 — strongly rejects H0:E[R]=0")
        elif p < 0.05:
            notes.append(f"p={p:.4f} < 0.05 — rejects H0 at 5%")
        else:
            notes.append(f"p={p:.4f} — fails to reject H0")
    return "; ".join(notes)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Self-test mode (no args). Run with <path-to-trades.csv> to analyse real trades.")
        rng = np.random.default_rng(0)
        print("\n--- Simulating 1000 RW-noise trades (mean R should be ~0) ---")
        rw_R = rng.normal(0, 1, size=1000)
        for k, v in full_report(pd.DataFrame({"r_multiple": rw_R})).items():
            print(f"  {k}: {v}")

        print("\n--- Simulating 1000 edge-bearing trades (mean R = 0.15) ---")
        edge_R = rng.normal(0.15, 1, size=1000)
        for k, v in full_report(pd.DataFrame({"r_multiple": edge_R})).items():
            print(f"  {k}: {v}")
        sys.exit(0)

    trades = pd.read_csv(sys.argv[1])
    rep = full_report(trades)
    for k, v in rep.items():
        print(f"{k}: {v}")
