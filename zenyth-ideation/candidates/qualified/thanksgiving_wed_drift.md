---
name: THANKSGIVING_WED_DRIFT
status: QUALIFIED
round: 45
constraint: thanksgiving_wed_us_partial_close
expected_win_rate: 0.59
expected_rr: 1.3
---

# Candidate: THANKSGIVING_WED_DRIFT

## Generator
Wednesday before US Thanksgiving (4th Thursday of November): partial early close for US markets (NYSE closes at 13:00 EST Friday after; CME has reduced hours Wed-Fri); US bank desks ~30% staffed. EU & Asian markets normal. Result: structural USD-side liquidity decline for the entire 2.5-day Thanksgiving stretch. EURUSD has shown a small but consistent positive drift on T-Wed and T-Fri (the partial-close days) — likely from EU-side desks dominating quoting with widened spreads.

Proposal:
- Trigger: Wednesday before Thanksgiving at 09:00 EST.
- Entry rule: LONG EURUSD at 09:00 EST.
- Stop: 25 pips.
- Target: 35 pips, or time-stop at 14:00 EST.
- Expected win rate: 59%.
- Expected R:R: 1.3.

## RNG Critic
On random walk: holiday calendar irrelevant; EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **US Thanksgiving Wednesday partial-close + EU-side desk dominance**. Specific:
1. NYSE / CME / NASDAQ early-close schedules (published annually).
2. US bank desk staffing dropped per NY Fed surveys.
3. Calendar-anchored (4th Thursday of November).

## Decision
**QUALIFIED**.
