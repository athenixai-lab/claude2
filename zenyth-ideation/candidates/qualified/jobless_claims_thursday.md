---
name: JOBLESS_CLAIMS_THURSDAY
status: QUALIFIED
round: 68
constraint: us_initial_jobless_claims_thursday_830est
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: JOBLESS_CLAIMS_THURSDAY

## Generator
US Department of Labor releases weekly initial jobless claims every Thursday at 08:30 EST. Lower-impact than NFP/CPI but consistent weekly cadence; algos parse for trend signal versus consensus.

Proposal:
- Trigger: every Thursday at 08:30 EST.
- Entry rule: measure first 5-min reaction; if |M| > 8 pips, CONTINUE direction.
- Stop: 18 pips.
- Target: 22 pips, or time-stop at 09:30 EST.
- Expected win rate: 53%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**DOL Weekly Jobless Claims**. Calendar-anchored.

## Decision
**QUALIFIED**.
