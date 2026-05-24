---
name: SOFR_FIXING
status: QUALIFIED
round: 92
constraint: sofr_daily_fixing_0800est_post_2018
expected_win_rate: 0.52
expected_rr: 1.2
---

# Candidate: SOFR_FIXING

## Generator
Secured Overnight Financing Rate (SOFR) — published daily by NY Fed at 08:00 EST (post-LIBOR transition since 2018). SOFR is the reference rate for ~$300T notional in USD derivatives. Daily publication can move EURUSD via USD-funding-cost adjustments.
- Trigger: 08:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 14, time-stop 08:30 EST.
- WR 52%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**SOFR daily fixing (NY Fed publication)**. Calendar-anchored.

## Decision
**QUALIFIED** — limited to 2018+ data; weak signal.
