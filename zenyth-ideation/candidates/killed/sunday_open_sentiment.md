---
name: SUNDAY_OPEN_SENTIMENT
status: KILLED
round: 50
constraint: friday_sentiment_sunday_continuation
expected_win_rate: 0.50
expected_rr: 1.0
---

# Candidate: SUNDAY_OPEN_SENTIMENT

## Generator
Hypothesis: if Friday closes strongly directional, Sunday open continues the move.

## RNG Critic
This is the OPPOSITE of SUNDAY_GAP_FILL — and it can't be true both at the same time. SUNDAY_GAP_FILL (Round 10) FADES the gap. If both edges existed independently, they'd cancel.

On random walk, Friday-close direction has zero predictive power on Sunday open. The "continuation" idea is just a behavioral guess.

## Decision
**KILLED** — directly contradicts SUNDAY_GAP_FILL which has a stronger mechanism (Wellington-open market-maker inventory limits). The "weekend continuation" thesis has no specific institutional mechanism.
