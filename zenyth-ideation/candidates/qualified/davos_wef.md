---
name: DAVOS_WEF
status: QUALIFIED
round: 121
constraint: davos_world_economic_forum_late_january_tuesday_friday
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: DAVOS_WEF

## Generator
World Economic Forum annual meeting in Davos — late January (typically Tuesday to Friday). Central bank governors, finance ministers, and large asset manager CEOs attend; speeches and panel discussions can move EUR via policy-direction hints (e.g. 2017 Draghi comments).
- Trigger: each business day of Davos week at 09:00 EST.
- Entry: small CONTINUATION position based on prior-day drift.
- Stop: 25, Target: 32, time-stop 16:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Annual WEF Davos forum**. Calendar-anchored.

## Decision
**QUALIFIED** — discretionary effect, but calendar-anchored.
