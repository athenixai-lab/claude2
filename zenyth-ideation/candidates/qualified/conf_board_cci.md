---
name: CONF_BOARD_CCI
status: QUALIFIED
round: 88
constraint: conference_board_consumer_confidence_last_tuesday_1000est
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: CONF_BOARD_CCI

## Generator
Conference Board Consumer Confidence Index releases last Tuesday of month at 10:00 EST. Complementary to U Mich Sentiment.
- Trigger: release at 10:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 14, time-stop 11:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Conference Board CCI monthly**. Calendar-anchored.

## Decision
**QUALIFIED**.
