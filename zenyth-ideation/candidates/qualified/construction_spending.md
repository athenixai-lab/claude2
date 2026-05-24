---
name: CONSTRUCTION_SPENDING
status: QUALIFIED
round: 90
constraint: us_construction_spending_first_business_day_1000est
expected_win_rate: 0.50
expected_rr: 1.2
---

# Candidate: CONSTRUCTION_SPENDING

## Generator
US Construction Spending monthly, first business day at 10:00 EST. Often released same day as ISM Manufacturing PMI.
- Trigger: release at 10:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 10, Target: 12, time-stop 10:30 EST.
- WR 50%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES** (marginal — at WR 50% this is at the edge of acceptable; spread cost makes net EV near zero. Better to combine via CONCORDANCE rather than standalone).

## Constraint Identifier
**US Construction Spending monthly**. Calendar-anchored.

## Decision
**QUALIFIED** — weak; ideally only used in concordance with other releases.
