---
name: PHILLY_FED_MFG
status: QUALIFIED
round: 82
constraint: philly_fed_manufacturing_third_thursday_830est
expected_win_rate: 0.51
expected_rr: 1.3
---

# Candidate: PHILLY_FED_MFG

## Generator
Federal Reserve Bank of Philadelphia Manufacturing Survey releases 3rd Thursday of month at 08:30 EST. Companion to Empire State Survey but a few days later in cycle.

Proposal:
- Trigger: Philly Fed release Thursday at 08:30 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 14 pips.
- Target: 18 pips, time-stop at 09:30 EST.
- Expected win rate: 51%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Philadelphia Fed Manufacturing Survey**. Calendar-anchored.

## Decision
**QUALIFIED**.
