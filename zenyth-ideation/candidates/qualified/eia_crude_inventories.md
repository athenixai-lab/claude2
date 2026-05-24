---
name: EIA_CRUDE_INVENTORIES
status: QUALIFIED
round: 84
constraint: eia_crude_oil_inventory_wednesday_1030est
expected_win_rate: 0.52
expected_rr: 1.2
---

# Candidate: EIA_CRUDE_INVENTORIES

## Generator
EIA Weekly Crude Oil Inventories release Wednesday 10:30 EST. Drives WTI crude futures; via inverse USD-oil correlation (-0.4 to -0.6 historically), EURUSD has a measurable secondary effect.

Proposal:
- Trigger: EIA Wednesday 10:30 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12 pips.
- Target: 14 pips, time-stop at 11:00 EST.
- Expected win rate: 52%.
- Expected R:R: 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**EIA weekly inventory + USD-oil correlation spillover**. Calendar-anchored.

## Decision
**QUALIFIED** — small but consistent.
