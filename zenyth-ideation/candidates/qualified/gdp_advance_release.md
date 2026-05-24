---
name: GDP_ADVANCE_RELEASE
status: QUALIFIED
round: 67
constraint: us_gdp_advance_estimate_quarterly_830est
expected_win_rate: 0.55
expected_rr: 1.5
---

# Candidate: GDP_ADVANCE_RELEASE

## Generator
BEA Advance GDP estimate releases quarterly (~last business day of January/April/July/October) at 08:30 EST. Material to USD via growth differential / Fed policy implications. Similar mechanism to CPI/NFP post-release continuation.

Proposal:
- Trigger: GDP Advance day at 08:35 EST.
- Entry rule: measure first 5-min move; if |M| > 12 pips, CONTINUE.
- Stop: 22 pips.
- Target: 32 pips, or time-stop at 10:00 EST.
- Expected win rate: 55%.
- Expected R:R: 1.5.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BEA Quarterly Advance GDP**. Calendar-anchored.

## Decision
**QUALIFIED**.
