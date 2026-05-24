---
name: ROUND_NUMBER_STOP_RUN
status: KILLED
round: 18
constraint: generic_round_number_stop_clusters
expected_win_rate: 0.55
expected_rr: 1.3
---

# Candidate: ROUND_NUMBER_STOP_RUN

## Generator
Round-number stop clusters at 1.0500, 1.1000 etc. Trade reversal after stops are run through the level.

## RNG Critic
Generic round-number stops are a basic ICT/retail pattern. The user explicitly listed "generic round numbers" in REJECT category. Also: the "stop run + reversal" pattern can partially appear on RNG due to the symmetric nature of mean-reverting noise.

## Constraint Identifier
"Stop cluster" exists but is generic — every round level has stops. Without a specific time-of-day or specific fund-driven liquidity event, this is not a unique constraint.

## Decision
**KILLED** — in user's explicit rejection list ("generic round numbers"). Not novel.
