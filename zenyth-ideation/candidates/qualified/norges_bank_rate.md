---
name: NORGES_BANK_RATE
status: QUALIFIED
round: 103
constraint: norges_bank_rate_decision_thursday_0400est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: NORGES_BANK_RATE

## Generator
Norges Bank (Norway) rate decisions 8 times/year Thursday at 10:00 CET (04:00 EST). NOK reacts; via EUR/NOK cross spillover to EUR/USD (small).
- Trigger: Norges decision Thursday at 04:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 04:30 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Norges Bank scheduled rate decisions**. Calendar-anchored.

## Decision
**QUALIFIED** — small effect via EUR/NOK cross.
