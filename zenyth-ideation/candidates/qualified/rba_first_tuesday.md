---
name: RBA_FIRST_TUESDAY
status: QUALIFIED
round: 76
constraint: rba_first_tuesday_2330est_prior_day
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: RBA_FIRST_TUESDAY

## Generator
Reserve Bank of Australia announces rate decisions on the first Tuesday of each month (excluding January) at 14:30 AEDT (23:30 EST prior day in winter). AUD reacts; via EUR/AUD cross, EURUSD has small secondary effect.

Proposal:
- Trigger: RBA announcement at 23:30 EST prior day.
- Entry rule: first-min CONTINUATION if |M| > 5 pips.
- Stop: 12 pips.
- Target: 16 pips, or time-stop at 00:30 EST.
- Expected win rate: 53%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**RBA rate decision + EUR/AUD cross**. Calendar-anchored.

## Decision
**QUALIFIED**.
