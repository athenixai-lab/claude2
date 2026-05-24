---
name: PRE_CPI_TUESDAY_DRIFT
status: QUALIFIED
round: 49
constraint: pre_cpi_macro_positioning_t_minus_1
expected_win_rate: 0.55
expected_rr: 1.4
---

# Candidate: PRE_CPI_TUESDAY_DRIFT

## Generator
The day before CPI release (typically Mon or Tue afternoon), macro funds and CTA programs systematically position INTO the release direction based on consensus expectation vs prior CPI trend. The result: a drift in the consensus-implied direction during the 14:00–17:00 EST window of T-1, as discretionary traders pre-position.

The consensus-implied direction proxy: take the 3-month moving average of CPI direction (proxy: 90-day EURUSD trend inverse).

Proposal:
- Trigger: 14:00 EST on the day BEFORE CPI release.
- Entry rule: compute 90-day EURUSD return R = Close[14:00 today] - Close[14:00 90 trading days ago]. If R > 0, take LONG EUR (expecting CPI to support continued EUR strength). If R < 0, take SHORT EUR.
- Stop: 30 pips.
- Target: 45 pips, or time-stop at 23:00 EST.
- Expected win rate: 55%.
- Expected R:R: 1.4.

## RNG Critic
On random walk: 90-day return has no predictive power on next 9-h return. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **Pre-CPI macro positioning**. Specific:
1. CPI release calendar known 1 year ahead.
2. Macro fund pre-event positioning standard practice (per JPM "Macro Pre-Event Flow" notes).
3. Calendar-anchored.

## Decision
**QUALIFIED**.
