---
name: ASIAN_RANGE_ALGO
status: KILLED
round: 14
constraint: asian_session_range_algo_trigger
expected_win_rate: 0.52
expected_rr: 1.4
---

# Candidate: ASIAN_RANGE_ALGO

## Generator
Proposal: many institutional algos use the Asian session high/low (00:00–06:00 EST) as a key reference for London-session breakout entries. Take a fade of the FIRST 5-min break of Asian range during 06:00–09:00 EST when the breakout has < 5 pips of follow-through within 10 min.

## RNG Critic
This is a classic "false breakout fade." On i.i.d. random walk, breakout of a prior range followed by reversal IS the natural behavior: when 360 minutes of returns sum to a small range, the first break of that range is statistically followed by mean reversion (high probability) because the breakout is itself a tail event in a mean-zero process.

The pattern of "low-volatility-followed-by-breakout-fade" exists on random walks. The win rate cited (52%) is dangerously close to the random-walk baseline. After spread, this is below zero EV even on real data.

**FAILS — random walk preserves the pattern.**

## Constraint Identifier
"Algo trigger" is vague — claiming "many institutional algos use Asian range" without naming a specific firm's strategy or a documented mechanism is exactly the kind of fuzzy reasoning the Constraint Identifier should kill.

## Testability Judge
N/A — RNG critic already killed.

## Decision
**KILLED** — pattern survives on RNG, vague mechanism, this is a basic ICT-adjacent setup essentially equivalent to "false breakout" which is on the rejection list.
