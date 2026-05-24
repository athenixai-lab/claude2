---
name: SCHEDULED_POWELL_SPEECH
status: QUALIFIED
round: 126
constraint: fed_chair_scheduled_speech_pre_announced
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: SCHEDULED_POWELL_SPEECH

## Generator
Federal Reserve Chair scheduled speeches (excluding Humphrey-Hawkins and Jackson Hole, which are separate candidates). Speeches at conferences, university events, etc., typically pre-announced 1-2 weeks ahead. Material to USD when speech topic is monetary policy.
- Trigger: scheduled Powell speech at announced start-time.
- Entry: first 5-min CONTINUATION if |M| > 8 pips.
- Stop: 18, Target: 25, time-stop 30 min later.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed Chair scheduled speech**. Calendar-anchored.

## Decision
**QUALIFIED**.
