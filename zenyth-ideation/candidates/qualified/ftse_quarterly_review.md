---
name: FTSE_QUARTERLY_REVIEW
status: QUALIFIED
round: 147
constraint: ftse_russell_index_quarterly_review_effective_dates
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: FTSE_QUARTERLY_REVIEW

## Generator
FTSE Russell publishes quarterly index reviews (March, June, September, December — effective after market close on 3rd Friday). Less impact than the annual Russell reconstitution but consistent quarterly cadence.
- Trigger: 3rd Friday of March/June/September/December at 14:00 EST.
- Entry: small directional.
- Stop: 30, Target: 40, time-stop 15:55 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**FTSE Russell quarterly index review**. Calendar-anchored.

## Decision
**QUALIFIED**.
