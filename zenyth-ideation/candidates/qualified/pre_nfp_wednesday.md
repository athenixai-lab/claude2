---
name: PRE_NFP_WEDNESDAY
status: QUALIFIED
round: 154
constraint: pre_nfp_wednesday_positioning_drift
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: PRE_NFP_WEDNESDAY

## Generator
The Wednesday of NFP week (typically when ADP releases) sees broad pre-NFP positioning by macro funds in addition to the ADP reaction. Beyond the ADP_WED_DRIFT (R43) initial-spike capture, the broader 09:30-12:00 EST window of NFP-Wednesday shows directional drift as funds size into their NFP-bet.
- Trigger: NFP-Wednesday at 09:30 EST.
- Entry: same direction as 08:15 ADP-reaction (if any), or LONG bias on EUR if no clear ADP signal.
- Stop: 25, Target: 35, time-stop 12:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**NFP-week macro fund pre-positioning** beyond ADP-day initial. Calendar-anchored.

## Decision
**QUALIFIED** — distinct from ADP_WED_DRIFT (which captures 08:15-08:30 reaction).
