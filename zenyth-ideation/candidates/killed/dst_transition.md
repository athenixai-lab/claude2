---
name: DST_TRANSITION
status: KILLED
round: 71
constraint: dst_transition_weekend_drift
expected_win_rate: 0.50
expected_rr: 1.0
---

# Candidate: DST_TRANSITION

## Generator
DST transition weekends (early Nov fall-back, mid-March spring-forward in US; late Mar/Oct in EU). Hypothesis: synchronization mismatch creates drift.

## RNG Critic / Constraint Identifier
DST shifts are pure scheduling artifacts that affect WHEN trading happens, not WHO trades or WHAT they trade. There's no specific institutional flow driven by the DST transition itself. The "weekend gap" effect already captured by SUNDAY_GAP_FILL.

## Decision
**KILLED** — no distinct mechanism beyond what's captured by other gap-fill rules.
