---
name: DAY_AFTER_FOMC_REVERSAL
status: QUALIFIED
round: 47
constraint: post_fomc_overshoot_reversion_day_plus_one
expected_win_rate: 0.58
expected_rr: 1.5
---

# Candidate: DAY_AFTER_FOMC_REVERSAL

## Generator
Documented post-announcement behavior: the first-day reaction to FOMC often OVERSHOOTS the equilibrium price discovered over the subsequent week. Macro fund position adjustments (entering / exiting based on dot plot) finish in the first 4-6 hours, then market begins to REGRESS toward the "well-considered" price over the next 1-3 days. The day AFTER FOMC (T+1) has shown a small but consistent reversal of the FOMC-day move.

Proposal:
- Trigger: day after FOMC (T+1) at 03:00 EST (London open).
- Entry rule: measure FOMC-day move F = Close[FOMC day 17:00] - Close[FOMC day 13:55]. If |F| > 40 pips, FADE at 03:00 EST.
- Stop: 35 pips.
- Target: 50 pips, or time-stop at 14:00 EST T+1.
- Expected win rate: 58%.
- Expected R:R: 1.5.

## RNG Critic
On random walk: yesterday's return has zero predictive power on today's. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **FOMC overshoot + multi-day reversion**. Specific:
1. Macro fund position adjustments complete within 4-6h of release.
2. CTA program updates run overnight T+0 → T+1.
3. Documented in Lucca-Moench (2015) + follow-up: FOMC day move regresses partially.
4. Calendar-anchored.

## Decision
**QUALIFIED**.
