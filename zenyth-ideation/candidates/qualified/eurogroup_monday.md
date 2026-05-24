---
name: EUROGROUP_MONDAY
status: QUALIFIED
round: 115
constraint: eurogroup_meeting_monthly_monday
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: EUROGROUP_MONDAY

## Generator
Eurogroup — finance ministers of EU member states — meets monthly Monday afternoon in Brussels (or remotely). Communiques on EU fiscal/monetary coordination released ~21:00 CET (15:00 EST). Material to EUR via fiscal/political tone.
- Trigger: Eurogroup Monday at 15:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 15, Target: 19, time-stop 16:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Eurogroup monthly meeting + EU finance minister communique**. Calendar-anchored.

## Decision
**QUALIFIED**.
