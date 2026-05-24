---
name: FED_FUNDS_FUTURES_ROLL
status: QUALIFIED
round: 140
constraint: fed_funds_30day_futures_monthly_roll_last_business_day
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: FED_FUNDS_FUTURES_ROLL

## Generator
CBOT 30-day Fed Funds futures (ZQ) settle on the LAST business day of each month at 16:00 EST. Rate-derivatives traders roll positions in the days before. Material to USD rate expectations and through them EUR/USD.
- Trigger: last business day of month at 15:55 EST.
- Entry: SHORT EURUSD if month-to-date has shown rising Fed-implied path (proxy: month-to-date USD strength); LONG if falling.
- Stop: 18, Target: 22, time-stop 16:05 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**CBOT Fed Funds 30-day futures monthly settlement**. Calendar-anchored.

## Decision
**QUALIFIED**.
