---
name: BANK_STRESS_TESTS
status: QUALIFIED
round: 156
constraint: fed_eba_annual_bank_stress_test_release
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: BANK_STRESS_TESTS

## Generator
Fed Stress Test (CCAR/DFAST) results — annually late June. EBA Stress Test results — biennial late July/November. Both move bank-stock valuations and through them FX risk-on/off positioning. Material to USD.
- Trigger: stress test result release day at 16:30 EST.
- Entry: first 30-min CONTINUATION if |M| > 10 pips.
- Stop: 25, Target: 32, time-stop 17:30 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed CCAR/DFAST + EBA stress test annual cycle**. Calendar-anchored.

## Decision
**QUALIFIED**.
