---
name: TRIPLE_STRIKE_REVERSION
status: KILLED
round: 74
constraint: three_consecutive_calendar_same_direction
expected_win_rate: 0.50
expected_rr: 1.0
---

# Candidate: TRIPLE_STRIKE_REVERSION

## Generator
After 3 consecutive same-direction calendar-signal trades, expect mean reversion on the 4th.

## RNG Critic
This is a gambler's-fallacy variant. On real data with positive-EV individual signals, three consecutive same-direction signals firing is more likely a sign that the underlying flow is genuine and persistent, NOT a reason to fade. Fading positive-EV signals because of a "streak" destroys EV. On RNG, streaks happen randomly with no predictive power.

## Decision
**KILLED** — gambler's fallacy, no mechanism.
