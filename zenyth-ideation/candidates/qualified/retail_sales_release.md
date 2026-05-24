---
name: RETAIL_SALES_RELEASE
status: QUALIFIED
round: 66
constraint: us_retail_sales_830est_mid_month
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: RETAIL_SALES_RELEASE

## Generator
US Census Bureau Retail Sales report releases mid-month (around 13th-16th calendar day) at 08:30 EST. Material to Fed real-economy assessment; algos parse the headline + control group for trend signal.

Proposal:
- Trigger: Retail Sales day at 08:35 EST.
- Entry rule: measure first 5-min reaction; if |M| > 10 pips, CONTINUE direction.
- Stop: 20 pips.
- Target: 26 pips, or time-stop at 09:30 EST.
- Expected win rate: 53%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**US Census Retail Sales monthly release**. Calendar-anchored.

## Decision
**QUALIFIED**.
