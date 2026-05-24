---
name: BOE_QE_OPERATION
status: QUALIFIED
round: 98
constraint: boe_apf_purchase_operation_window
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: BOE_QE_OPERATION

## Generator
Bank of England Asset Purchase Facility (APF) operations during active QE periods (2009-2012, 2016-2017, 2020-2022) at scheduled Monday/Wednesday/Thursday 14:15 GMT (09:15 EST winter / 08:15 EST summer). Operations affect GBP yields, with EUR/GBP cross spillover to EUR/USD.
- Trigger: BoE APF operation day at 08:15 or 09:15 EST per DST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 13, time-stop 30min later.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BoE APF purchase operation calendar** (BoE published schedule). Active-QE periods only.

## Decision
**QUALIFIED** — limited to active QE periods.
