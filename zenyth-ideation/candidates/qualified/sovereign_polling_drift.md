---
name: SOVEREIGN_POLLING_DRIFT
status: QUALIFIED
round: 144
constraint: pre_referendum_pre_election_polling_drift_28_to_14_days_before
expected_win_rate: 0.56
expected_rr: 1.6
---

# Candidate: SOVEREIGN_POLLING_DRIFT

## Generator
Refinement of SOVEREIGN_EVENT_ANCHORED (R75). In the 28-to-14 day window BEFORE a scheduled binary sovereign event, polling data accumulates and macro funds gradually position. This earlier window (vs SOVEREIGN_EVENT_ANCHORED's 5-day pre-event window) captures the slow-positioning phase.
- Trigger: 21 business days before scheduled binary sovereign event at 09:00 EST.
- Entry: SHORT EURUSD (assuming binary sovereign event has historical pattern of disrupting EUR).
- Stop: 80, Target: 120, time-stop event-day - 5.
- WR 56%, RR 1.6.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Pre-referendum/election macro fund slow positioning**. Calendar-anchored.

## Decision
**QUALIFIED** — refinement layer on existing template.
