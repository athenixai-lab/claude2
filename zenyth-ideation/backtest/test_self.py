"""
Self-test: generate ~2 years of synthetic EURUSD-like M1 data in the spec format,
write it to disk, and run all three strategies end-to-end.

This validates that:
- the data loader parses the spec format,
- the harness simulates trades,
- the strategy modules build intents and run without errors.

It does NOT validate that the strategies have positive EV (synthetic data is
random; on random data EV should be ~0 / slightly negative after cost).
The validation is "the code runs to completion and produces a stats block."
"""

from __future__ import annotations

import os
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from data_loader import load_eurusd_m1  # noqa: E402
from harness import simulate, TradeIntent, report, PIP  # noqa: E402
import strategy_r01_ldn_4pm_fix as r01  # noqa: E402
import strategy_r09_donchian as r09  # noqa: E402
import strategy_r18_microbounce as r18  # noqa: E402


def generate_synthetic_csv(out_path: str, n_days: int = 730, seed: int = 7):
    """Generate ~n_days of synthetic M1 bars in the spec format.

    Format per line: YYYYMMDD HHMMSS;O;H;L;C;V
    Skip weekends (no bars Sat/Sun outside 17:00+ on Sun).
    """
    rng = np.random.default_rng(seed)
    sigma_bar = 0.00010  # ~1 pip per minute std
    price = 1.10000

    rows: list[str] = []
    start_date = datetime(2010, 1, 4)  # Monday
    total_bars_per_weekday = 24 * 60  # 1440 minutes; for simplicity, always include all minutes
    cur = start_date.replace(hour=0, minute=0, second=0)

    for d in range(n_days):
        day = start_date + timedelta(days=d)
        weekday = day.weekday()  # 0=Mon
        if weekday >= 5:
            # FX is open Sunday 17:00 EST -> Friday 17:00 EST.
            if weekday == 6:  # Sunday: include 17:00..23:59
                for h in range(17, 24):
                    for m in range(60):
                        bar = (h * 60 + m)
                        # generate
                        ret = rng.normal(0, sigma_bar)
                        new_price = price + ret
                        hi = max(price, new_price) + abs(rng.normal(0, sigma_bar / 2))
                        lo = min(price, new_price) - abs(rng.normal(0, sigma_bar / 2))
                        ts = day.replace(hour=h, minute=m, second=0).strftime("%Y%m%d %H%M%S")
                        rows.append(f"{ts};{price:.5f};{hi:.5f};{lo:.5f};{new_price:.5f};100")
                        price = new_price
            continue
        # Friday: only up to 17:00 EST (1020 bars)
        max_min = 17 * 60 if weekday == 4 else 24 * 60
        for tot in range(max_min):
            h = tot // 60
            m = tot % 60
            ret = rng.normal(0, sigma_bar)
            new_price = price + ret
            hi = max(price, new_price) + abs(rng.normal(0, sigma_bar / 2))
            lo = min(price, new_price) - abs(rng.normal(0, sigma_bar / 2))
            ts = day.replace(hour=h, minute=m, second=0).strftime("%Y%m%d %H%M%S")
            rows.append(f"{ts};{price:.5f};{hi:.5f};{lo:.5f};{new_price:.5f};100")
            price = new_price

    with open(out_path, "w") as f:
        f.write("\n".join(rows))
    return len(rows)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        csv_path = os.path.join(tmp, "synthetic_eurusd_m1.csv")
        print(f"Generating synthetic data -> {csv_path}")
        n = generate_synthetic_csv(csv_path, n_days=400)
        print(f"  Wrote {n:,} bars")

        print("\nLoading...")
        df = load_eurusd_m1(csv_path)
        print(f"  Loaded {len(df):,} bars  span {df.index[0]} -> {df.index[-1]}")
        assert len(df) > 1000, "data load too small"

        # --- Test harness with a trivial fixed intent ---
        first_ts = df.index[100]
        last_ts = df.index[200]
        intent = TradeIntent(
            entry_ts=first_ts,
            direction=+1,
            stop=float(df["open"].iat[100]) - 20 * PIP,
            target=float(df["open"].iat[100]) + 30 * PIP,
            time_stop_ts=last_ts,
            tag="self_test",
        )
        res = simulate(df, [intent])
        assert not res.empty, "simulator produced no result for valid intent"
        print(f"\nHarness self-test: 1 trade simulated, exit_reason={res.iloc[0]['exit_reason']}")

        # --- R1 ---
        print("\n\n=== Running R1 on synthetic ===")
        r01.run(csv_path, spread_pips=0.5)

        # --- R9 ---
        print("\n\n=== Running R9 on synthetic ===")
        r09.run(csv_path, spread_pips=0.5)

        # --- R18 ---
        print("\n\n=== Running R18 on synthetic ===")
        r18.run(csv_path, spread_pips=0.5)

    print("\n\nSELF-TEST OK — all three strategy modules ran end-to-end.")


if __name__ == "__main__":
    main()
