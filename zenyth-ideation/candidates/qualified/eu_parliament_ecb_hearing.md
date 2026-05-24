---
name: EU_PARLIAMENT_ECB_HEARING
status: QUALIFIED
round: 128
constraint: ecb_president_eu_parliament_quarterly_hearing
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: EU_PARLIAMENT_ECB_HEARING

## Generator
ECB President quarterly hearing before EU Parliament's ECON Committee (typically Monday or Tuesday in Strasbourg/Brussels). Statutory requirement; ~4 hearings/year. Material to EUR.
- Trigger: ECON Committee hearing at start-time.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 16, time-stop 30 min later.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB statutory quarterly EU Parliament hearing**. Calendar-anchored.

## Decision
**QUALIFIED**.
