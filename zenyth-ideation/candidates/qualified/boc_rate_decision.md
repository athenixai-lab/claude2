---
name: BOC_RATE_DECISION
status: QUALIFIED
round: 51
constraint: boc_rate_decision_wednesday_1000est
expected_win_rate: 0.54
expected_rr: 1.3
---

# Candidate: BOC_RATE_DECISION

## Generator
Bank of Canada announces rate decisions Wednesday at 10:00 EST, 8 times per year. CAD reacts; through EUR/CAD cross arbitrage, EURUSD has a measurable secondary effect (smaller than direct CAD pairs but distinct). Direction depends on policy divergence.

Proposal:
- Trigger: BoC announcement Wednesday at 10:00 EST.
- Entry rule: measure first-min body M = bar[10:00 close] - bar[10:00 open]. If |M| > 6 pips, CONTINUE direction at 10:01 EST.
- Stop: 15 pips.
- Target: 20 pips, or time-stop at 10:30 EST.
- Expected win rate: 54%.
- Expected R:R: 1.3.

## RNG Critic
On random walk: 1-min body has zero predictive power on next 30-min direction. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **BoC rate decision + EUR/CAD cross arbitrage spillover**. Specific:
1. BoC publishes 8 announcement dates 1 year in advance.
2. CAD-side flow at 10:00 EST is large; cross-arb instant.
3. Calendar-anchored.

## Decision
**QUALIFIED** — small but consistent secondary effect.
