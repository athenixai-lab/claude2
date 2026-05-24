---
name: TANKAN_QUARTERLY
status: QUALIFIED
round: 102
constraint: boj_tankan_quarterly_survey_release
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: TANKAN_QUARTERLY

## Generator
BoJ Tankan Quarterly Survey of Japanese enterprises — published at 08:50 JST (19:50 EST prior day) in early April/July/October/January. Single most important Japanese macro release after CPI. JPY-side flow with EUR cross spillover.
- Trigger: Tankan release at 19:50 EST prior day.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 16, time-stop 21:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BoJ quarterly Tankan survey**. Calendar-anchored.

## Decision
**QUALIFIED**.
