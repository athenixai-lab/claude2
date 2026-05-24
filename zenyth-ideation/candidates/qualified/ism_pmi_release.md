---
name: ISM_PMI_RELEASE
status: QUALIFIED
round: 64
constraint: ism_manufacturing_pmi_1000est_first_business_day
expected_win_rate: 0.54
expected_rr: 1.4
---

# Candidate: ISM_PMI_RELEASE

## Generator
ISM Manufacturing PMI releases at 10:00 EST on the first business day of each month. Pre-2019 was the most-watched non-NFP US macro release; still material on EURUSD via Fed policy expectations. PMI > 50 vs < 50 distinction (expansion vs contraction) triggers algorithmic responses.

Proposal:
- Trigger: ISM Manufacturing PMI day (first business day of month, occasionally Tuesday if Mon = holiday) at 10:00 EST.
- Entry rule: measure first 5-min reaction; if |M| > 8 pips, CONTINUE.
- Stop: 20 pips.
- Target: 28 pips, or time-stop at 11:00 EST.
- Expected win rate: 54%.
- Expected R:R: 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ISM Manufacturing PMI release**. Specific:
1. Institute for Supply Management releases monthly schedule.
2. Calendar-anchored to first business day.

## Decision
**QUALIFIED**.
