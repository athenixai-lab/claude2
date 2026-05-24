---
name: HOLIDAY_WEEKEND_BRIDGE
status: QUALIFIED
round: 157
constraint: 4day_weekend_bridge_holiday_friday_or_monday
expected_win_rate: 0.55
expected_rr: 1.3
---

# Candidate: HOLIDAY_WEEKEND_BRIDGE

## Generator
When US/UK/EU holiday falls on Friday or Monday, creating a 4-day weekend, the gap-risk and position-squaring effect is amplified vs normal weekend. Combined effects: more weekend gap-risk hedging + larger Sunday-open gap-fill flow.
- Trigger: Thursday at 14:00 EST before 4-day weekend (Friday holiday) OR Tuesday at 14:00 EST after 4-day weekend (Monday holiday).
- Entry: small FADE of prior 4-hr drift (excess pre-weekend hedging).
- Stop: 30, Target: 38, time-stop 16:55 EST.
- WR 55%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**4-day weekend bridge + amplified squaring**. Calendar-anchored.

## Decision
**QUALIFIED**.
