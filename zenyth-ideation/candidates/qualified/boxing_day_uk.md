---
name: BOXING_DAY_UK
status: QUALIFIED
round: 132
constraint: boxing_day_uk_closed_us_open
expected_win_rate: 0.54
expected_rr: 1.3
---

# Candidate: BOXING_DAY_UK

## Generator
Dec 26 (Boxing Day): UK and many Commonwealth countries closed; US markets open (with reduced staffing). Similar mechanism to GOOD_FRIDAY_ASYMMETRY but reversed: US-side dominates with London absent. Small but consistent USD-side flow bias.
- Trigger: Dec 26 at 09:00 EST (or first business day after if 26th is weekend).
- Entry: SHORT EURUSD at 09:00 EST.
- Stop: 22, Target: 28, time-stop 14:00 EST.
- WR 54%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Boxing Day UK / Commonwealth closure + US-only quoting asymmetry**. Calendar-anchored.

## Decision
**QUALIFIED**.
