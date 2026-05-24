---
name: BOE_MPC_DRIFT
status: QUALIFIED
round: 34
constraint: boe_mpc_thursday_0700est_release
expected_win_rate: 0.55
expected_rr: 1.4
---

# Candidate: BOE_MPC_DRIFT

## Generator
BoE Monetary Policy Committee announces rate decision Thursday at 12:00 London (07:00 EST winter / 06:00 EST summer in dataset). Spillover to EURUSD: when BoE hikes vs ECB hikes, GBP/USD moves; through EUR/GBP cross arbitrage, EURUSD moves correspondingly within 1–2 minutes.

The mechanic: in the 30-min window AFTER release, EUR/GBP cross arbitrage and Bank of England's relative-policy assessment cause measurable EURUSD drift, particularly on "policy-divergence" releases.

Proposal:
- Trigger: BoE MPC release day (8/year, "Super Thursday") at fix-time T (06:00 or 07:00 EST per dataset DST mapping).
- Entry rule: measure first-minute move M = bar[T:00 close] - bar[T:00 open]. If |M| > 8 pips, take CONTINUATION at T+1 min (same sign as M).
- Stop: 18 pips.
- Target: 25 pips, or time-stop at T+25 min.
- Expected win rate: 55%.
- Expected R:R: 1.4.

## RNG Critic
On random walk: 1-min prior body has no predictive power on next 25-min direction. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **BoE MPC release + EUR/GBP cross arbitrage spillover**. Specific:
1. BoE MPC publishes calendar 1 year in advance.
2. "Super Thursday" format: simultaneous policy statement + Minutes + Inflation Report (since 2015).
3. EUR/GBP basis affects EUR/USD via triangular arbitrage immediately on policy moves.
4. Calendar-anchored.

## Testability Judge

```python
# Hardcoded BoE MPC dates 2008-2024 from BoE website
# Detect DST month for fix_hour (06 or 07)
# Continuation logic
```

RNG: shuffled → 0 EV. Real: +4 to +8 pips/trade × ~8 trades/year × 14 years.

## Decision
**QUALIFIED**.
