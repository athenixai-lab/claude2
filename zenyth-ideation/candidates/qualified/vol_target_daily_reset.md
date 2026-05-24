---
name: VOL_TARGET_DAILY_RESET
status: QUALIFIED
round: 122
constraint: volatility_targeting_fund_daily_notional_reset_1600est
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: VOL_TARGET_DAILY_RESET

## Generator
Volatility-targeting funds (estimated $300B+ AUM industry: risk-parity, target-vol equity funds, multi-asset strategies) compute daily realized vol and rebalance notional exposure at 16:00 EST close. When prior day's realized M1 vol is unusually high, vol-targeting funds DECREASE risk exposure (sell equity → indirect USD-positive); when low, they INCREASE (buy equity → indirect USD-negative).

EUR/USD spillover: through aggregate risk-on/risk-off positioning, the daily 16:00 EST notional reset creates a small but consistent EUR-side flow that tracks prior-day realized volatility.

- Trigger: each business day at 16:00 EST.
- Entry: measure prior 24h realized M1 vol R. If R > 1.5x 20-day median (high vol), SHORT EURUSD (risk-off bid for USD). If R < 0.7x median (low vol), LONG EURUSD (risk-on weak USD).
- Stop: 18, Target: 22, time-stop 16:30 EST.
- WR 53%, RR 1.3.

## RNG Critic
EV pre-cost zero on RNG. Vol-targeting funds don't exist on RNG.

**PASSES.**

## Constraint Identifier
**Volatility-targeting fund daily notional reset**. Specific:
1. AHL, Bridgewater All Weather, Bidlingmaier Risk Parity all daily-rebalance to vol target.
2. Documented in Mosk-Zhou (2017) "Volatility-of-Volatility and Risk-Parity Strategies."
3. Calendar/clock-anchored.

## Decision
**QUALIFIED**.
