---
name: YOM_KIPPUR_THIN
status: QUALIFIED
round: 130
constraint: yom_kippur_jewish_holiday_trading_desk_thin
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: YOM_KIPPUR_THIN

## Generator
Yom Kippur (September/October per Hebrew calendar). Significant fraction of NY/London trading desks observe the holiday — desks reduced to ~50-60% staff. Israeli markets closed. Thinner book; calendar-anchored to Hebrew calendar.
- Trigger: Yom Kippur date at 09:00 EST.
- Entry: small SHORT EURUSD (USD-bid in thin book per CLS data history).
- Stop: 25, Target: 32, time-stop 15:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Yom Kippur cultural/religious holiday + NY/London desk reduced staffing**. Calendar-anchored (Hebrew calendar).

## Decision
**QUALIFIED**.
