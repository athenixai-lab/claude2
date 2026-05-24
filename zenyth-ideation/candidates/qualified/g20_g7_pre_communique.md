---
name: G20_G7_PRE_COMMUNIQUE
status: QUALIFIED
round: 58
constraint: g20_g7_finance_ministers_communique_weekend
expected_win_rate: 0.57
expected_rr: 1.4
---

# Candidate: G20_G7_PRE_COMMUNIQUE

## Generator
G20 and G7 Finance Ministers + Central Bank Governors meet ~3 times/year, typically Friday-Sunday weekends. Joint communiques regularly reference FX policy ("we will refrain from competitive devaluations") — language is monitored heavily by macro desks. Sunday-evening reopen 17:00 EST shows directional drift based on whether communique language was strong-USD-supportive (USD reserve currency reaffirmation) or critical (USD policy concerns).

Proposal:
- Trigger: Sunday 17:30 EST after G20/G7 Finance Ministers weekend.
- Entry rule: measure first 30 min from 17:00 EST market open. If |M| > 12 pips, CONTINUE direction.
- Stop: 30 pips.
- Target: 45 pips, or time-stop at Monday 04:00 EST.
- Expected win rate: 57%.
- Expected R:R: 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**G20/G7 finance ministers communique + macro fund Sunday-evening repricing**. Specific:
1. G20 Finance Ministers schedule published 6+ months in advance.
2. ~3 meetings/year (Spring, Summer Sherpa, Annual).
3. Calendar-anchored.

## Decision
**QUALIFIED**.
