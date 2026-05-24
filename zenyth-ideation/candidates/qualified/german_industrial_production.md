---
name: GERMAN_INDUSTRIAL_PRODUCTION
status: QUALIFIED
round: 153
constraint: destatis_german_industrial_production_monthly
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: GERMAN_INDUSTRIAL_PRODUCTION

## Generator
Destatis German Industrial Production monthly release at 08:00 CET (02:00 EST). Germany is EZ's largest economy; IP is a key leading indicator.
- Trigger: German IP release at 02:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 02:30 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Destatis German Industrial Production monthly**. Calendar-anchored.

## Decision
**QUALIFIED**.
