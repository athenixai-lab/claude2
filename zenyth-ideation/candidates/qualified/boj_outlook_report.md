---
name: BOJ_OUTLOOK_REPORT
status: QUALIFIED
round: 112
constraint: boj_outlook_report_quarterly_april_july_october_january
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: BOJ_OUTLOOK_REPORT

## Generator
BoJ Outlook Report on Economic Activity and Prices — quarterly, released alongside the relevant BoJ monetary policy meeting (April / July / October / January). Provides Japan's projected growth/inflation outlook; major market mover for JPY. Effect on EUR through cross.
- Trigger: BoJ outlook release at 23:00 EST prior day (08:00 JST Tokyo).
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 16, time-stop 23:30 EST.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BoJ Outlook Report quarterly**. Calendar-anchored.

## Decision
**QUALIFIED**.
