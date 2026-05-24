---
name: UMICH_CONSUMER_SENTIMENT
status: QUALIFIED
round: 79
constraint: umich_consumer_sentiment_friday_1000est
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: UMICH_CONSUMER_SENTIMENT

## Generator
University of Michigan Consumer Sentiment preliminary release: 2nd Friday of month at 10:00 EST; final release: 4th Friday of month at 10:00 EST. Modestly market-moving consumer-side indicator.

Proposal:
- Trigger: U Mich release Friday at 10:00 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 8 pips.
- Stop: 18 pips.
- Target: 22 pips, time-stop at 11:00 EST.
- Expected win rate: 52%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**U Mich consumer sentiment monthly release**. Calendar-anchored (preliminary + final).

## Decision
**QUALIFIED**.
