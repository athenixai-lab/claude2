---
name: EXISTING_HOME_SALES
status: QUALIFIED
round: 85
constraint: nar_existing_home_sales_monthly_1000est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: EXISTING_HOME_SALES

## Generator
NAR Existing Home Sales report monthly Tuesday/Wednesday at 10:00 EST. Housing-market leading indicator. Modest USD impact but consistent calendar.

Proposal:
- Trigger: NAR release day at 10:00 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12 pips.
- Target: 14 pips, time-stop at 11:00 EST.
- Expected win rate: 51%.
- Expected R:R: 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**NAR monthly existing home sales report**. Calendar-anchored.

## Decision
**QUALIFIED**.
