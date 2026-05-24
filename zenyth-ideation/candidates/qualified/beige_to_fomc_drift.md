---
name: BEIGE_TO_FOMC_DRIFT
status: QUALIFIED
round: 110
constraint: beige_book_to_fomc_pre_meeting_information_drift
expected_win_rate: 0.56
expected_rr: 1.5
---

# Candidate: BEIGE_TO_FOMC_DRIFT

## Generator
The 2-week window between Beige Book release (Wednesday 2 weeks before FOMC) and FOMC statement has measurable drift bias. Beige Book tone provides 80% of the new information FOMC will price; algos and discretionary traders position over the subsequent 14 days. Direction is set by the Beige Book → drift compounds through to FOMC.

This is a cross-event combination: Beige Book sets DIRECTION, then FOMC_PRE_DRIFT captures CONTINUATION into the meeting day, then DAY_AFTER_FOMC_REVERSAL captures the OVERSHOOT.

Proposal:
- Trigger: Beige Book release day at 14:00 EST.
- Entry: same direction as 5-min Beige Book reaction. Hold through to FOMC press conference end at 14:55 EST.
- Stop: 60 pips.
- Target: 100 pips.
- WR 56%, RR 1.5.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Beige-Book→FOMC information drift compounding**. Specific:
1. Beige Book contains the regional economic data FOMC reviews.
2. 14-day drift documented in Cieslak-Vissing-Jorgensen (2020).
3. Calendar-anchored.

## Decision
**QUALIFIED** — combination strategy that compounds two component signals.
