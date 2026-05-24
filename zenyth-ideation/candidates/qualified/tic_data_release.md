---
name: TIC_DATA_RELEASE
status: QUALIFIED
round: 83
constraint: tic_capital_flows_data_1600est_mid_month
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: TIC_DATA_RELEASE

## Generator
US Treasury International Capital (TIC) data releases mid-month at 16:00 EST. Reveals foreign holdings of US Treasury / agency / corporate securities. Material to USD via flow signal. Less impactful than NFP/CPI but specific to USD-asset demand.

Proposal:
- Trigger: TIC release at 16:00 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 14 pips.
- Target: 18 pips, time-stop at 17:00 EST.
- Expected win rate: 52%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**US Treasury TIC monthly report**. Calendar-anchored.

## Decision
**QUALIFIED**.
