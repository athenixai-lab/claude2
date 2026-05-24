---
name: NEW_HOME_SALES
status: QUALIFIED
round: 89
constraint: us_new_home_sales_monthly_1000est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: NEW_HOME_SALES

## Generator
US Census New Home Sales monthly Tuesday at 10:00 EST. Construction-cycle indicator.
- Trigger: release at 10:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 14, time-stop 11:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**US Census New Home Sales monthly**. Calendar-anchored.

## Decision
**QUALIFIED**.
