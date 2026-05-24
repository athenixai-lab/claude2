---
name: BOJ_RATE_DECISION
status: QUALIFIED
round: 52
constraint: boj_rate_decision_tuesday_jst_noon
expected_win_rate: 0.55
expected_rr: 1.4
---

# Candidate: BOJ_RATE_DECISION

## Generator
BoJ announces rate decisions on no-fixed-time around noon JST (22:00 prior-day EST), 8 times/year. JPY-side flow at announcement spills into EURUSD via EUR/JPY cross within minutes.

Proposal:
- Trigger: BoJ announcement day at 22:00 EST prior day.
- Entry rule: measure first 5-min cumulative move from 22:00 EST. If |M| > 8 pips, CONTINUE direction.
- Stop: 18 pips.
- Target: 25 pips, or time-stop at 23:00 EST.
- Expected win rate: 55%.
- Expected R:R: 1.4.

## RNG Critic
On random walk: EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **BoJ rate decision + EUR/JPY cross arbitrage spillover**. Specific:
1. BoJ calendar published 1 year in advance.
2. Calendar-anchored.

## Decision
**QUALIFIED**.
