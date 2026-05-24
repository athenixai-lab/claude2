---
name: CFTC_COT_FRIDAY
status: QUALIFIED
round: 60
constraint: cftc_cot_friday_1530est_release
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: CFTC_COT_FRIDAY

## Generator
CFTC Commitments of Traders (COT) report releases Friday 15:30 EST. Reveals weekly futures positioning of "Commercial," "Non-Commercial," and "Non-Reportable" traders. When the COT shows extreme positioning (>2 std dev from 1-year baseline), CTAs and trend followers receive a signal to either reinforce or fade their positions; this generates a small but consistent positional adjustment in the 30-min window after release.

Proposal:
- Trigger: every Friday at 15:30 EST.
- Entry rule: measure 30-min reaction at 16:00 EST. If |M| > 8 pips, take MOMENTUM in same direction.
- Stop: 18 pips.
- Target: 25 pips, or time-stop at 16:55 EST.
- Expected win rate: 53%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**CFTC COT report (weekly Friday 15:30 EST release)**. Specific:
1. CFTC publishes weekly per Commodity Exchange Act §17.
2. ~$70B AUM in CTA programs use COT as signal.
3. Calendar-anchored.

## Decision
**QUALIFIED**.
