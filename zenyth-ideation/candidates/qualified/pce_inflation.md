---
name: PCE_INFLATION
status: QUALIFIED
round: 135
constraint: us_pce_inflation_friday_830est_late_month
expected_win_rate: 0.55
expected_rr: 1.4
---

# Candidate: PCE_INFLATION

## Generator
US Personal Consumption Expenditures (PCE) inflation — Fed's preferred inflation gauge. Released by BEA at 08:30 EST near month-end (typically last business day of month or 25th-30th). Materially impacts USD via direct Fed-policy implication. Highly market-moving since Fed's 2020 framework refresh making PCE the targeted inflation measure.
- Trigger: PCE release at 08:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 8 pips.
- Stop: 20, Target: 28, time-stop 09:30 EST.
- WR 55%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BEA PCE Inflation monthly release + Fed-targeted measure**. Calendar-anchored.

## Decision
**QUALIFIED**.
