---
name: IMF_MEETINGS
status: QUALIFIED
round: 108
constraint: imf_world_bank_spring_annual_meetings_weekend
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: IMF_MEETINGS

## Generator
IMF / World Bank Group Spring Meetings (mid-April) and Annual Meetings (mid-October) bring together global central bank governors and finance ministers in DC. Concurrent G20 and G7 finance side-meetings. Monday-after-meetings open shows directional drift based on weekend communiques/announcements.
- Trigger: Monday morning at 03:00 EST after IMF Spring/Annual Meetings weekend.
- Entry: first 30-min CONTINUATION if |M| > 12 pips.
- Stop: 35, Target: 50, time-stop 09:00 EST.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**IMF semi-annual meetings + concurrent G20 / G7 sideline + reserve-manager attendance**. Calendar-anchored.

## Decision
**QUALIFIED**.
