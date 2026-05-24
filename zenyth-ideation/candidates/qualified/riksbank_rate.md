---
name: RIKSBANK_RATE
status: QUALIFIED
round: 104
constraint: riksbank_sweden_rate_decision_0330est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: RIKSBANK_RATE

## Generator
Sveriges Riksbank rate decisions ~6 times/year Tuesday/Wednesday at 09:30 CET (03:30 EST). SEK reacts; via EUR/SEK cross small EUR/USD spillover.
- Trigger: Riksbank decision at 03:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 04:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Riksbank scheduled rate decisions**. Calendar-anchored.

## Decision
**QUALIFIED**.
