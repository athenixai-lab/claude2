---
name: SCHEDULED_LAGARDE_SPEECH
status: QUALIFIED
round: 127
constraint: ecb_president_scheduled_speech_pre_announced
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: SCHEDULED_LAGARDE_SPEECH

## Generator
ECB President scheduled speeches (excluding Sintra, ECB Press Conferences, EU summits). Speeches at G30, IIF, European Parliament hearings, etc. Material to EUR when topic is monetary policy.
- Trigger: scheduled speech at announced start-time.
- Entry: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 14, Target: 20, time-stop 30 min later.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB President scheduled speech**. Calendar-anchored.

## Decision
**QUALIFIED**.
