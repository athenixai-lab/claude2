---
name: PPI_RELEASE
status: QUALIFIED
round: 70
constraint: us_ppi_release_830est_mid_month
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: PPI_RELEASE

## Generator
US BLS Producer Price Index releases mid-month (1-2 days before CPI typically) at 08:30 EST. Provides leading signal for CPI direction.

Proposal:
- Trigger: PPI day at 08:30 EST.
- Entry rule: measure first 5-min reaction; if |M| > 8 pips, CONTINUE direction.
- Stop: 18 pips.
- Target: 24 pips, or time-stop at 09:30 EST.
- Expected win rate: 52%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BLS PPI monthly release**. Calendar-anchored.

## Decision
**QUALIFIED** — weak but real signal.
