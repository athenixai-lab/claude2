---
name: ECB_QE_OPERATION
status: QUALIFIED
round: 94
constraint: ecb_qe_app_pepp_friday_results_release
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: ECB_QE_OPERATION

## Generator
ECB publishes weekly purchases under APP (Asset Purchase Programme) and PEPP (Pandemic Emergency Purchase Programme) on Mondays/Tuesdays. Material to EUR-side bond yields and through that to EUR/USD. Effects strongest during active QE programs (2015-2022).
- Trigger: ECB weekly purchase report Monday at 09:45 CET (03:45 EST).
- Entry: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 14, Target: 18, time-stop 04:30 EST.
- WR 53%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB QE program weekly operation publication**. Calendar-anchored.

## Decision
**QUALIFIED** — limited to active QE periods.
