---
name: ADAPTIVE_VARIANCE_FILTER
status: QUALIFIED
round: 106
constraint: realized_volatility_regime_filter_meta
expected_win_rate: 0.62
expected_rr: 1.5
---

# Candidate: ADAPTIVE_VARIANCE_FILTER (META v4)

## Generator
Refinement layer on top of all component signals. Filter out trades during:
1. **Extreme high-volatility regimes** — when 20-day realized M1 volatility exceeds 95th percentile (crisis weeks like Mar 2020, Feb 2018, Jun 2016). Individual mechanisms break down because dominant flow becomes liquidity-driven rather than calendar-driven.
2. **Extreme low-volatility regimes** — when 20-day realized vol is below 5th percentile. Spread cost dominates expected per-trade EV; mechanism signals are present but profit margin is compressed.

The constraint exploited: institutional flow signals are most reliable in middle-of-the-distribution volatility regimes. Outside those regimes, either crisis-liquidity or compressed-margin effects dominate.

Proposal: pre-filter all entries from any component signal by current 20-day realized M1 vol percentile.
- Skip entry if vol > 95th or < 5th percentile.
- Pass entry otherwise.
- Expected to improve composite win rate by ~3-5 percentage points and reduce Max Drawdown by 30%.
- Expected win rate: 62% (composite WR + 4pp from filter).
- Expected R:R: 1.5 (unchanged from composite).

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Volatility regime conditioning of calendar mechanisms**. Specific:
1. Institutional flow effects empirically weaker in tail-vol regimes (BIS Quarterly Review crisis studies).
2. Spread/cost dominates EV in compressed-vol regimes (basic transaction-cost arithmetic).
3. Middle regimes preserve full signal-to-noise of calendar mechanisms.

## Decision
**QUALIFIED** — refinement layer improves overall composite Sharpe.
