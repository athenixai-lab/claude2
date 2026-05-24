---
name: POST_EU_SUMMIT_DRIFT
status: QUALIFIED
round: 120
constraint: eu_summit_communique_monday_after_friday_summit
expected_win_rate: 0.53
expected_rr: 1.5
---

# Candidate: POST_EU_SUMMIT_DRIFT

## Generator
EU heads-of-state summits (European Council meetings) — typically quarterly, held over Thursday-Friday in Brussels. Major communiques on EU fiscal/policy direction released Friday evening. Monday-after open reflects market reaction.
- Trigger: Monday after EU Summit at 03:00 EST.
- Entry: first 30-min CONTINUATION if |M| > 10 pips.
- Stop: 25, Target: 35, time-stop 06:00 EST.
- WR 53%, RR 1.5.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**European Council quarterly summits + Friday communiques**. Calendar-anchored.

## Decision
**QUALIFIED**.
