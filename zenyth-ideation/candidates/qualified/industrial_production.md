---
name: INDUSTRIAL_PRODUCTION
status: QUALIFIED
round: 86
constraint: fed_industrial_production_mid_month_915est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: INDUSTRIAL_PRODUCTION
## Generator
Federal Reserve Industrial Production & Capacity Utilization release ~15th of each month at 09:15 EST. Manufacturing-sector indicator.
- Trigger: IP release at 09:15 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 14, Target: 17, time-stop 10:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed Industrial Production monthly**. Calendar-anchored.

## Decision
**QUALIFIED**.
