---
name: ECB_MRO_TUESDAY
status: QUALIFIED
round: 99
constraint: ecb_main_refinancing_operation_tuesday_0915cet
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: ECB_MRO_TUESDAY

## Generator
ECB Main Refinancing Operations (MRO) — weekly tender for 1-week liquidity to Eurozone banks. Bid deadline 09:30 CET Tuesday (03:30 EST). Allotment announced 11:15 CET (05:15 EST). Affects EUR money market rates and through them EUR/USD.
- Trigger: ECB MRO allotment Tuesday at 05:15 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 06:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB MRO weekly fixed-rate or variable-rate tender**. Calendar-anchored.

## Decision
**QUALIFIED**.
