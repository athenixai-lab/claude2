---
name: EUROZONE_HICP_FLASH
status: QUALIFIED
round: 69
constraint: eurozone_hicp_flash_last_business_day_month
expected_win_rate: 0.55
expected_rr: 1.5
---

# Candidate: EUROZONE_HICP_FLASH

## Generator
Eurostat publishes the Eurozone HICP Flash Estimate on the last business day of each month at 11:00 CET (05:00 EST in dataset). Most-watched EU inflation data; drives ECB policy expectations directly. Less impactful than US CPI but uniquely material to EUR-side pricing.

Proposal:
- Trigger: HICP flash day at 05:00 EST.
- Entry rule: measure first 5-min reaction; if |M| > 8 pips, CONTINUE direction.
- Stop: 18 pips.
- Target: 26 pips, or time-stop at 06:00 EST.
- Expected win rate: 55%.
- Expected R:R: 1.5.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Eurostat HICP Flash Estimate**. Calendar-anchored.

## Decision
**QUALIFIED**.
