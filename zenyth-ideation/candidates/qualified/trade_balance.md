---
name: TRADE_BALANCE
status: QUALIFIED
round: 109
constraint: us_trade_balance_release_830est_monthly
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: TRADE_BALANCE

## Generator
US Trade Balance monthly Tuesday at 08:30 EST. Material to USD via current-account imbalance signal; modest reaction.
- Trigger: release at 08:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 14, time-stop 09:30 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BEA US Trade Balance monthly**. Calendar-anchored.

## Decision
**QUALIFIED**.
