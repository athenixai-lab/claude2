---
name: FED_H41_BALANCE
status: QUALIFIED
round: 101
constraint: fed_h41_weekly_balance_sheet_thursday_1630est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: FED_H41_BALANCE

## Generator
Federal Reserve releases the H.4.1 Statistical Release "Factors Affecting Reserve Balances" every Thursday at 16:30 EST. Material to USD-funding analysis: shows weekly Fed reserves, RRP usage, foreign reverse-repo facility, etc. Specifically watched during QT/QE transitions.
- Trigger: Thursday 16:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 14, time-stop 17:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed H.4.1 weekly Federal Reserve balance sheet**. Calendar-anchored.

## Decision
**QUALIFIED**.
