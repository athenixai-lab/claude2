---
name: SOMA_REINVESTMENT
status: QUALIFIED
round: 91
constraint: ny_fed_soma_treasury_reinvestment_1st_15th
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: SOMA_REINVESTMENT

## Generator
Federal Reserve System Open Market Account (SOMA) reinvests maturing Treasury holdings on the 1st and 15th of each month (or next business day). Adds steady USD-side demand on these dates as the Fed rolls maturing securities. Small but consistent effect on USD funding.
- Trigger: 1st or 15th business day at 10:00 EST.
- Entry: SHORT EURUSD at 10:00 EST.
- Stop: 25, Target: 30, time-stop 14:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed SOMA Treasury reinvestment policy** (regulated; published in NY Fed releases). Calendar-anchored.

## Decision
**QUALIFIED**.
