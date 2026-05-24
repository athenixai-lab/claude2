"""
RNG generators for sanity testing strategies.

Three RNG modes, in order of increasing realism:

1. gaussian_rw         — pure i.i.d. Gaussian returns at same vol as input.
                         Pure martingale. NO strategy can have EV > 0 on this
                         (Doob's optional stopping theorem). Class A and Class B
                         should both produce EV ≈ 0.

2. shuffled_returns    — shuffles real returns (preserves marginal distribution
                         including fat tails, but destroys autocorrelation).
                         Distinguishes "fat-tail edge" from "autocorrelation edge."

3. block_bootstrap     — block-bootstrap of real returns (preserves short-range
                         autocorrelation AND fat tails, but breaks long-range
                         structure and calendar effects).
                         Class B momentum/mean-reversion strategies should retain
                         most of their EV here. Class A calendar strategies should
                         lose their EV (calendar is destroyed).

Each generator returns an OHLC DataFrame in the same format as data_loader.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Literal

import numpy as np
import pandas as pd

from data_loader import EST_FIXED


def _ohlc_from_path(price_path: np.ndarray, sigma_intrabar: float,
                    timestamps: pd.DatetimeIndex,
                    rng: np.random.Generator) -> pd.DataFrame:
    """Build an OHLC dataframe from a per-bar close-price path."""
    closes = price_path
    opens = np.empty_like(closes)
    opens[0] = closes[0]
    opens[1:] = closes[:-1]  # open of bar t = close of bar t-1

    # Add modest intrabar high/low extensions.
    bar_moves = np.abs(closes - opens)
    extra = np.abs(rng.normal(0.0, sigma_intrabar / 2, size=len(closes)))
    highs = np.maximum(closes, opens) + extra
    lows = np.minimum(closes, opens) - np.abs(rng.normal(0.0, sigma_intrabar / 2, size=len(closes)))
    # Ensure high >= max(open,close) and low <= min(open,close)
    highs = np.maximum(highs, np.maximum(opens, closes))
    lows = np.minimum(lows, np.minimum(opens, closes))

    df = pd.DataFrame(
        {"open": opens, "high": highs, "low": lows, "close": closes},
        index=timestamps,
    )
    return df


def gaussian_rw(reference_df: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    """Pure Gaussian random walk at the same per-bar vol as the reference."""
    rng = np.random.default_rng(seed)
    rets = reference_df["close"].diff().dropna().to_numpy()
    sigma = float(np.std(rets))
    start_price = float(reference_df["close"].iloc[0])
    N = len(reference_df)
    new_rets = rng.normal(0.0, sigma, size=N - 1)
    prices = np.concatenate([[start_price], start_price + np.cumsum(new_rets)])
    return _ohlc_from_path(prices, sigma, reference_df.index, rng)


def shuffled_returns(reference_df: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    """Shuffle real returns (destroys autocorrelation, preserves marginal incl. fat tails)."""
    rng = np.random.default_rng(seed)
    rets = reference_df["close"].diff().dropna().to_numpy()
    shuffled = rng.permutation(rets)
    sigma = float(np.std(shuffled))
    start_price = float(reference_df["close"].iloc[0])
    prices = np.concatenate([[start_price], start_price + np.cumsum(shuffled)])
    return _ohlc_from_path(prices, sigma, reference_df.index, rng)


def block_bootstrap(reference_df: pd.DataFrame, block_size: int = 30, seed: int = 7) -> pd.DataFrame:
    """Stationary block-bootstrap (preserves short-range AR + fat tails)."""
    rng = np.random.default_rng(seed)
    rets = reference_df["close"].diff().dropna().to_numpy()
    N = len(rets)
    n_blocks = (N // block_size) + 1
    starts = rng.integers(0, N - block_size, size=n_blocks)
    blocks = np.concatenate([rets[s:s + block_size] for s in starts])
    bootstrap = blocks[:N]
    sigma = float(np.std(bootstrap))
    start_price = float(reference_df["close"].iloc[0])
    prices = np.concatenate([[start_price], start_price + np.cumsum(bootstrap)])
    return _ohlc_from_path(prices, sigma, reference_df.index, rng)


def synthetic_rw_index(n_bars: int = 100_000, start: datetime | None = None) -> pd.DatetimeIndex:
    """Generate a synthetic minute timestamp index (no weekend filtering — for unit tests)."""
    if start is None:
        start = datetime(2010, 1, 4, 0, 0, 0)
    return pd.date_range(start=start, periods=n_bars, freq="1min", tz=EST_FIXED)


def synthetic_reference(n_bars: int = 100_000, seed: int = 7, sigma: float = 0.00010) -> pd.DataFrame:
    """Build a synthetic 'reference' DataFrame for testing the RNG generators themselves."""
    rng = np.random.default_rng(seed)
    rets = rng.normal(0, sigma, size=n_bars)
    prices = 1.10000 + np.cumsum(rets)
    ts = synthetic_rw_index(n_bars)
    return _ohlc_from_path(prices, sigma, ts, rng)


# ----- Top-level dispatch -----

GeneratorMode = Literal["gaussian_rw", "shuffled_returns", "block_bootstrap"]


def generate(mode: GeneratorMode, reference_df: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    if mode == "gaussian_rw":
        return gaussian_rw(reference_df, seed=seed)
    if mode == "shuffled_returns":
        return shuffled_returns(reference_df, seed=seed)
    if mode == "block_bootstrap":
        return block_bootstrap(reference_df, seed=seed)
    raise ValueError(f"unknown mode: {mode}")
