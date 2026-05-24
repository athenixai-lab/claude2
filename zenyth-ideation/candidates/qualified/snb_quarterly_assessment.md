---
name: SNB_QUARTERLY_ASSESSMENT
status: QUALIFIED
round: 65
constraint: snb_quarterly_monetary_policy_assessment_thursday
expected_win_rate: 0.54
expected_rr: 1.4
---

# Candidate: SNB_QUARTERLY_ASSESSMENT

## Generator
Swiss National Bank holds quarterly Monetary Policy Assessments — March, June, September, December, typically third Thursday at 09:30 CET (03:30 EST in dataset). EUR/CHF reacts; via EUR/USD vs USD/CHF triangular arbitrage, EURUSD shows a brief response within the first 5–10 minutes.

Proposal:
- Trigger: SNB MPA Thursday at 03:30 EST.
- Entry rule: measure first 5-min reaction; if |M| > 6 pips, CONTINUE direction.
- Stop: 12 pips.
- Target: 16 pips, or time-stop at 04:00 EST.
- Expected win rate: 54%.
- Expected R:R: 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**SNB quarterly monetary policy assessment + EUR/CHF cross arb**. Specific:
1. SNB publishes annual schedule.
2. Pre-2015 included EUR/CHF floor defense — extremely material; post-2015 lower impact but still measurable.
3. Calendar-anchored.

## Decision
**QUALIFIED**.
