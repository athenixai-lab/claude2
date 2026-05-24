---
name: NYFED_RRP_DRIFT
status: KILLED
round: 32
constraint: ny_fed_rrp_1330est_operation
expected_win_rate: 0.51
expected_rr: 1.1
---

# Candidate: NYFED_RRP_DRIFT

## Generator
NY Fed Open Market Desk conducts overnight RRP (Reverse Repo) operation daily at 13:30 EST. The size signals USD-system liquidity. Hypothesis: high-RRP-uptake days have spillover into EURUSD via USD-funding cost.

## RNG Critic
The proposed edge requires KNOWING the RRP size before trading on it; this data isn't in EURUSD M1 history. If we trade blindly at 13:30 EST every day, we have no directional signal — it's pure clock-time trading with no constraint identification.

**FAILS — no actionable directional signal from M1 data alone; the constraint requires external data we don't have.**

## Decision
**KILLED — not actionable on M1 EURUSD alone.**
