---
name: MSCI_STANDARD_REVIEW
status: QUALIFIED
round: 146
constraint: msci_quarterly_standard_review_march_september
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: MSCI_STANDARD_REVIEW

## Generator
MSCI Standard Index Review — quarterly process: February, May, August, November (announced); effective last business day of March, June, September, December. Smaller-magnitude review (constituent additions/deletions, not country reclassification) compared to MSCI_REBALANCE (R141 = the larger semi-annual May/November country review).
- Trigger: last business day of March / September at 14:00 EST.
- Entry: small directional based on month-to-date drift.
- Stop: 25, Target: 32, time-stop 15:55 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**MSCI quarterly standard review (smaller than semi-annual)**. Calendar-anchored.

## Decision
**QUALIFIED**.
