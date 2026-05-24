---
name: MSCI_REBALANCE
status: QUALIFIED
round: 141
constraint: msci_quarterly_semiannual_rebalance_late_may_august_november
expected_win_rate: 0.54
expected_rr: 1.4
---

# Candidate: MSCI_REBALANCE

## Generator
MSCI publishes semi-annual review of country/sector classifications: May and November. Effective dates: last business day of those months. Roughly $14T tracks MSCI indices. Reclassifications (e.g. MSCI EM upgrade, frontier-to-EM) drive massive FX flows.
- Trigger: last business day of May / November at 14:00 EST.
- Entry: small directional based on month-to-date drift.
- Stop: 40, Target: 55, time-stop 16:00 EST.
- WR 54%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**MSCI semi-annual index review + country/sector reclassification**. Calendar-anchored.

## Decision
**QUALIFIED**.
