---
name: JOLTS_RELEASE
status: QUALIFIED
round: 136
constraint: bls_jolts_job_openings_1000est_monthly
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: JOLTS_RELEASE

## Generator
BLS Job Openings and Labor Turnover Survey (JOLTS) — monthly Tuesday at 10:00 EST. Important labor-market indicator (Fed Chair Powell has cited JOLTS quits/openings ratio as key labor-tightness measure).
- Trigger: JOLTS release at 10:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 14, Target: 18, time-stop 11:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**BLS JOLTS monthly release**. Calendar-anchored.

## Decision
**QUALIFIED**.
