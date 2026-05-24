---
name: TOKYO_LUNCH_BREAKOUT
status: KILLED
round: 3
constraint: tokyo_lunch_liquidity_vacuum
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: TOKYO_LUNCH_BREAKOUT

## Generator
Tokyo lunch break (23:30–00:30 EST in dataset; 12:30–13:30 JST). Japanese banks and corporates pause; liquidity drops; range often contracts. Proposal: trade the breakout of the lunch range when Tokyo desks return at 00:30 EST.

## RNG Critic
On a random walk, contracted-range followed by expansion IS the natural behavior of any random process: when 60 1-min returns sum to a small range, the next 60 returns will likely produce a larger range simply by the law of expected absolute deviation growth. Breakout of an artificially-narrow range on a random walk DOES generate a positive raw expectancy in the breakout direction (selection bias: we only act when the range is small, and any subsequent move is "outside" the small range with high probability).

**FAILS — this strategy makes money on a random walk. The "breakout" pattern is a statistical artifact of low-volatility periods being followed by mean-reverting volatility, present in i.i.d. data too.**

## Constraint Identifier
"Liquidity vacuum" — too vague. Tokyo lunch is real but the supposed asymmetric edge (direction of breakout) is NOT driven by a specific institutional flow. Without a directional driver, this reduces to a momentum-on-range-expansion strategy, which is not constraint-based.

## Testability Judge
Backtestable, but RNG critic already invalidated it. No need to write spec.

## Decision
**KILLED** — survives on random walk. Common volatility-clustering artifact, not a real institutional edge.
