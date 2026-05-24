---
name: PRE_NFP_PREMIUM_DECAY
status: KILLED
round: 20
constraint: pre_nfp_implied_volatility_decay
expected_win_rate: 0.0
expected_rr: 0.0
---

# Candidate: PRE_NFP_PREMIUM_DECAY

## Generator
Implied vol spikes ahead of NFP. Idea: M1-scale volatility compression in the final 60 min before NFP.

## RNG Critic / Decision
This is fundamentally a non-directional volatility trade. EURUSD M1 spot directional trading cannot capture vol-decay edge — that requires options. **KILLED — not testable as directional spot strategy.**
