---
name: BIS_ANNUAL_MEETING
status: QUALIFIED
round: 114
constraint: bis_annual_general_meeting_late_june
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: BIS_ANNUAL_MEETING

## Generator
Bank for International Settlements (BIS) Annual General Meeting — late June each year in Basel. Concurrent with publication of BIS Annual Economic Report (Sunday before AGM). Central bank governors meet; communiques release Sunday/Monday. Material to FX-policy assessment.
- Trigger: Monday after BIS AGM weekend at 03:00 EST.
- Entry: first 30-min CONTINUATION if |M| > 10 pips.
- Stop: 25, Target: 32, time-stop 06:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BIS Annual General Meeting + Annual Economic Report**. Calendar-anchored.

## Decision
**QUALIFIED** — annual, distinct from Sintra Forum.
