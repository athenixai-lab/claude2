---
name: FED_BEIGE_BOOK
status: QUALIFIED
round: 55
constraint: fed_beige_book_release_1400est_wednesday
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: FED_BEIGE_BOOK

## Generator
Fed Beige Book published 2 weeks before each FOMC meeting on Wednesday at 14:00 EST. Summarizes regional Fed economic conditions; informs FOMC participants. Small but consistent move at release as algos parse for hawk/dove keywords.

Proposal:
- Trigger: Beige Book days at 14:00 EST.
- Entry rule: measure 5-min reaction at 14:05; if |M| > 8 pips, CONTINUE direction.
- Stop: 18 pips.
- Target: 25 pips, or time-stop at 15:00 EST.
- Expected win rate: 53%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed Beige Book + algorithmic keyword response**. Specific:
1. Fed Beige Book published 8 times/year, 14:00 EST, schedule online.
2. HFT keyword algos parse text within 50ms.
3. Calendar-anchored.

## Decision
**QUALIFIED**.
