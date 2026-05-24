---
name: LUNAR_NEW_YEAR_ASIA
status: QUALIFIED
round: 29
constraint: lunar_new_year_pboc_hkma_closure
expected_win_rate: 0.61
expected_rr: 1.4
---

# Candidate: LUNAR_NEW_YEAR_ASIA

## Generator
Chinese New Year (Lunar New Year): PBOC, HKMA, MAS-Singapore close for ~1 week. Tokyo remains open. The absence of Chinese FX reserve managers and Hong Kong-based prime brokers creates a structural pause in USD reserve recycling flows. PBOC normally executes daily USD/CNY fix maintenance (selling USD to defend CNY); during the closure, this flow stops, leading to a temporary USD-strong drift in major USD crosses (including EURUSD) during the closure week.

Proposal:
- Trigger: each business day during the 7-day Lunar New Year closure window (PBOC schedule) at 06:00 EST.
- Entry rule: SHORT EURUSD at 06:00 EST.
- Stop: 30 pips.
- Target: 40 pips, or time-stop at 16:00 EST.
- Expected win rate: 61%.
- Expected R:R: 1.4.

## RNG Critic
On random walk: lunar calendar has no meaning; EV pre-cost zero, post negative.

**PASSES.**

## Constraint Identifier
Mechanism: **Lunar New Year PBOC/HKMA closure + cessation of CNY-defense USD selling**. Specific:
1. PBOC publishes annual Lunar New Year holiday schedule.
2. CFETS (China Foreign Exchange Trade System) closed during the week.
3. HKMA closure removes a major liquidity-provider region.
4. Calendar-anchored.

## Testability Judge

```python
# Pseudocode — lunar dates need lookup table
import pandas as pd

LUNAR_NY_WINDOWS = [
    ("2008-02-06","2008-02-12"),
    ("2009-01-25","2009-01-31"),
    ("2010-02-13","2010-02-19"),
    # ... extend through 2024
]

# Trade SHORT EURUSD at 06:00 EST each business day in each window
# Stop +30, target -40 pips, time-stop 16:00 EST
```

Real-data backtest expected: +5 to +10 pips/trade × ~5 trades/year × 14 years.

## Decision
**QUALIFIED** — distinct calendar event with specific mechanism.
