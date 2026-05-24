---
name: ECB_M3_MONEY_SUPPLY
status: QUALIFIED
round: 152
constraint: ecb_m3_money_supply_monthly_release_0400est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: ECB_M3_MONEY_SUPPLY

## Generator
ECB Monetary Aggregates (M3) released monthly at 10:00 CET (04:00 EST). Important to EZ inflation tracking via quantity-theory channel.
- Trigger: M3 release at 04:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 04:30 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB monthly M3 release**. Calendar-anchored.

## Decision
**QUALIFIED**.
