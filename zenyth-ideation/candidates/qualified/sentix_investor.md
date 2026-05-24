---
name: SENTIX_INVESTOR
status: QUALIFIED
round: 138
constraint: sentix_eurozone_investor_confidence_first_monday
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: SENTIX_INVESTOR

## Generator
Sentix Eurozone Investor Confidence index — first Monday of each month at 10:30 CET (04:30 EST). Forward-looking sentiment indicator.
- Trigger: Sentix release first Monday at 04:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 05:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Sentix monthly investor confidence**. Calendar-anchored.

## Decision
**QUALIFIED**.
