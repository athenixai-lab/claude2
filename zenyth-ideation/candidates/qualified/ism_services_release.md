---
name: ISM_SERVICES_RELEASE
status: QUALIFIED
round: 80
constraint: ism_services_pmi_third_business_day_1000est
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: ISM_SERVICES_RELEASE

## Generator
ISM Services PMI (formerly Non-Manufacturing) releases 3rd business day of each month at 10:00 EST. Services account for ~70% of US GDP; the release is highly material for USD.

Proposal:
- Trigger: ISM Services release day at 10:00 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 8 pips.
- Stop: 20 pips.
- Target: 26 pips, time-stop at 11:00 EST.
- Expected win rate: 53%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ISM Services PMI**. Calendar-anchored.

## Decision
**QUALIFIED**.
