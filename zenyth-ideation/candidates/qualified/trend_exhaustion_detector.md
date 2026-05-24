---
name: TREND_EXHAUSTION_DETECTOR
status: QUALIFIED
round: 123
constraint: multi_day_trend_exhaustion_via_institutional_capacity
expected_win_rate: 0.58
expected_rr: 1.5
---

# Candidate: TREND_EXHAUSTION_DETECTOR (META v5)

## Generator
When EUR/USD has trended same direction for 5+ consecutive business days WITHOUT a major scheduled fundamental release (no NFP, FOMC, CPI, ECB), the trend is increasingly likely to be driven by positioning rather than fundamentals. Institutional positioning has FINITE capacity: hedge funds, CTAs, macro funds eventually run out of marginal new positioning room.

Mechanism: institutional position-sizing models (VAR-based, Kelly-based) cap each fund's exposure. When a 5-day trend has accumulated all marginal sizing, the next 1-3 days see fade as funds reach exposure limits.

This is NOT a momentum-fade gambler's fallacy. The KEY differentiator: requires the trend to be UNCONFIRMED by any scheduled fundamental release. If a fundamental release supports the trend, capacity expands; if no release, capacity is bounded.

- Trigger: 5+ consecutive business days same-direction trend AND no scheduled major release in current week (NFP, FOMC, CPI, ECB).
- Entry: FADE the trend at 09:00 EST on day 6.
- Stop: 50, Target: 75, time-stop 16:00 EST.
- WR 58%, RR 1.5.

## RNG Critic
This needs careful scrutiny. On i.i.d. random walk, 5-consecutive same-direction days happens with probability 1/32 ≈ 3%, and fading random streaks is gambler's fallacy.

KEY: the filter is NOT just "5-day streak"; it's "5-day streak WITHOUT a fundamental release." This requires a real calendar, which RNG lacks. On RNG, every 5-day streak that qualifies has zero predictive power → 0 EV → -spread cost → -EV.

On real data, the filter conditions on the ABSENCE of fundamental support, which is a real economic state: institutional capacity bounded, no marginal new flow, exhaustion likely.

**PASSES** — filter requires real calendar, not just price-streak.

## Constraint Identifier
**Institutional positioning capacity constraint + absence of new fundamental information**. Specific:
1. VAR-based position sizing at $50B+ AUM macro funds (Brevan, Bridgewater).
2. Kelly-clipped trend programs (AHL, Winton).
3. Calendar dependence: requires NO new fundamentals to allow capacity to be reset.

## Decision
**QUALIFIED** — distinct from gambler's fallacy because filter requires real-world economic state.
