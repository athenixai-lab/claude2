---
name: ECB_SPF_RELEASE
status: QUALIFIED
round: 133
constraint: ecb_survey_professional_forecasters_quarterly
expected_win_rate: 0.51
expected_rr: 1.3
---

# Candidate: ECB_SPF_RELEASE

## Generator
ECB Survey of Professional Forecasters — quarterly survey of EZ inflation/growth expectations, released early in each quarter. Tracks consensus for ECB targeting.
- Trigger: SPF release day at 09:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 12, Target: 16, time-stop 09:45 EST.
- WR 51%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB SPF quarterly publication**. Calendar-anchored.

## Decision
**QUALIFIED**.
