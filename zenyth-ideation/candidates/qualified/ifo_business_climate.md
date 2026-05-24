---
name: IFO_BUSINESS_CLIMATE
status: QUALIFIED
round: 77
constraint: ifo_index_release_last_monday_month
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: IFO_BUSINESS_CLIMATE

## Generator
Ifo Institute releases the Business Climate Index for Germany on the last Monday of each month at 10:00 CET (04:00 EST in dataset). Germany is the EZ's largest economy; Ifo is a closely-watched forward indicator. Direct effect on EUR via German PMI/business-sentiment readthrough.

Proposal:
- Trigger: Ifo release Monday at 04:00 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12 pips.
- Target: 16 pips, time-stop at 05:00 EST.
- Expected win rate: 52%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Ifo Business Climate Index monthly release**. Calendar-anchored.

## Decision
**QUALIFIED**.
