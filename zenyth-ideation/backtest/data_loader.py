"""
EURUSD M1 data loader for the ZENYTH ideation loop backtests.

Expected file format (per spec):
- Semicolon delimiter
- No header
- Timestamp format: YYYYMMDD HHMMSS
- Timestamps in EST UTC-5 (no DST shifts)
- Columns: TIMESTAMP;OPEN;HIGH;LOW;CLOSE;VOLUME

Example line:
20100104 030000;1.43320;1.43350;1.43300;1.43330;120

Usage:
    from data_loader import load_eurusd_m1
    df = load_eurusd_m1("/path/to/EURUSD_M1.csv")
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timezone, timedelta

try:
    import pandas as pd
    import numpy as np
except ImportError:
    sys.stderr.write(
        "pandas and numpy required. Install with: pip install pandas numpy\n"
    )
    raise


EST_FIXED = timezone(timedelta(hours=-5))  # Per spec: fixed UTC-5, no DST.


def load_eurusd_m1(
    path: str,
    chunksize: int | None = None,
    keep_volume: bool = False,
) -> pd.DataFrame:
    """Load EURUSD M1 data.

    Returns DataFrame indexed by tz-aware timestamp (EST fixed UTC-5),
    with columns ['open','high','low','close'] (and 'volume' if keep_volume).
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}")

    cols = ["ts", "open", "high", "low", "close", "volume"]
    dtype = {
        "ts": str,
        "open": "float64",
        "high": "float64",
        "low": "float64",
        "close": "float64",
        "volume": "float64",
    }

    df = pd.read_csv(
        path,
        sep=";",
        header=None,
        names=cols,
        dtype=dtype,
        engine="c",
    )

    df["ts"] = pd.to_datetime(df["ts"], format="%Y%m%d %H%M%S", utc=False)
    df["ts"] = df["ts"].dt.tz_localize(EST_FIXED)
    df = df.set_index("ts").sort_index()

    if not keep_volume:
        df = df[["open", "high", "low", "close"]]

    return df


def add_helpers(df: pd.DataFrame) -> pd.DataFrame:
    """Add common derived columns used by multiple strategies."""
    df = df.copy()
    df["ret"] = df["close"].diff()
    df["range"] = df["high"] - df["low"]
    df["weekday"] = df.index.weekday  # 0=Mon ... 6=Sun
    df["hhmm"] = df.index.strftime("%H%M").astype(int)
    df["yyyymmdd"] = df.index.strftime("%Y%m%d").astype(int)
    df["day_of_month"] = df.index.day
    df["month"] = df.index.month
    df["year"] = df.index.year
    return df


def atr(df: pd.DataFrame, n: int) -> pd.Series:
    """Average True Range over n bars (rolling, simple mean)."""
    prev_close = df["close"].shift(1)
    tr = pd.concat(
        [
            (df["high"] - df["low"]),
            (df["high"] - prev_close).abs(),
            (df["low"] - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return tr.rolling(n, min_periods=n).mean()


def daily_atr(df: pd.DataFrame, n: int) -> pd.Series:
    """Daily ATR computed from daily aggregation; reindexed back to M1."""
    daily = df.resample("1D").agg({"high": "max", "low": "min", "close": "last"}).dropna()
    daily_prev_close = daily["close"].shift(1)
    tr_d = pd.concat(
        [
            (daily["high"] - daily["low"]),
            (daily["high"] - daily_prev_close).abs(),
            (daily["low"] - daily_prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    atr_d = tr_d.rolling(n, min_periods=n).mean()
    # forward-fill onto the M1 index using each day's date
    atr_m1 = atr_d.reindex(df.index.normalize()).values
    return pd.Series(atr_m1, index=df.index, name=f"atr_daily_{n}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python data_loader.py <path-to-EURUSD-M1.csv>")
        sys.exit(2)
    df = load_eurusd_m1(sys.argv[1])
    print(f"Loaded {len(df):,} rows, range {df.index[0]} -> {df.index[-1]}")
    print(df.head())
    print(df.tail())
