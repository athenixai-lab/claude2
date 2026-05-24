---
name: TIC_LONG_TERM_FRIDAY
status: QUALIFIED
round: 148
constraint: tic_long_term_securities_friday_release
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: TIC_LONG_TERM_FRIDAY

## Generator
US Treasury TIC long-term capital flows data — released ~16th of each month at 16:00 EST. Distinct from TIC monthly data (Round 83); this is the breakdown of foreign net purchases of long-term US securities by country and security type.
- Trigger: TIC long-term release at 16:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 16:30 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**US Treasury TIC long-term securities monthly release**. Calendar-anchored.

## Decision
**QUALIFIED**.
