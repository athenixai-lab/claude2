"""
Driver: runs R1, R9, R18 sequentially and prints comparable stats.

Usage:
    python run_all.py /path/to/EURUSD_M1.csv [spread_pips]
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import strategy_r01_ldn_4pm_fix as r01
import strategy_r09_donchian as r09
import strategy_r18_microbounce as r18


def main():
    if len(sys.argv) < 2:
        print("usage: python run_all.py <EURUSD_M1.csv> [spread_pips]")
        sys.exit(2)
    path = sys.argv[1]
    spread = float(sys.argv[2]) if len(sys.argv) >= 3 else 0.5

    print("=" * 70)
    print("ZENYTH backtest suite — R1 (calendar), R9 (trend), R18 (micro)")
    print("=" * 70)

    print("\n\n#### Round 1 ####")
    r01.run(path, spread_pips=spread)

    print("\n\n#### Round 9 ####")
    r09.run(path, spread_pips=spread)

    print("\n\n#### Round 18 ####")
    r18.run(path, spread_pips=spread)


if __name__ == "__main__":
    main()
