---
name: TLTRO_OPERATION
status: QUALIFIED
round: 119
constraint: ecb_tltro_targeted_longer_term_refinancing_operation_results
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: TLTRO_OPERATION

## Generator
ECB TLTRO (Targeted Longer-Term Refinancing Operations) — series of multi-year bank liquidity programs (TLTRO-I 2014-18, II 2016-18, III 2019-21). Auction-style operations Thursday with results announced 11:15 CET (05:15 EST). Take-up size moves EUR via banking-sector liquidity signal.
- Trigger: TLTRO operation Thursday at 05:15 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 16, time-stop 06:00 EST.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB TLTRO operations during active programs**. Calendar-anchored.

## Decision
**QUALIFIED** — period-specific.
