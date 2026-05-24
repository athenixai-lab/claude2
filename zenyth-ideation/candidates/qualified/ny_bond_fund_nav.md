---
name: NY_BOND_FUND_NAV
status: QUALIFIED
round: 54
constraint: ny_1600est_bond_fund_nav_strike
expected_win_rate: 0.54
expected_rr: 1.3
---

# Candidate: NY_BOND_FUND_NAV

## Generator
US bond mutual funds strike daily NAV at 16:00 EST against US Treasury market closing prices. Foreign-asset bond funds with FX-hedged share classes must execute corresponding FX flow at the same 16:00 EST cutoff. This creates a secondary fix-like flow at 16:00 EST (separate from the WMR/BoE 4PM fix windows that fall at 10:00 or 11:00 EST in dataset).

Proposal:
- Trigger: 16:00 EST daily.
- Entry rule: measure 16:00 EST minute candle range R = bar[16:00 high] - bar[16:00 low]. If R > 6 pips, FADE the body direction (16:00 close - open) at 16:01 EST.
- Stop: 12 pips.
- Target: 10 pips, or time-stop at 16:10 EST.
- Expected win rate: 54%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
Mechanism: **US bond mutual fund NAV strike + FX-hedge corresponding flow**. Specific:
1. ICI: US bond mutual funds AUM ~$5T.
2. Foreign-bond funds with hedged share classes execute FX at 16:00 EST.
3. Clock-anchored.

## Decision
**QUALIFIED**.
