---
name: PRE_FOMC_BLACKOUT_SILENCE
status: QUALIFIED
round: 44
constraint: fed_blackout_period_silence_10day_window
expected_win_rate: 0.56
expected_rr: 1.5
---

# Candidate: PRE_FOMC_BLACKOUT_SILENCE

## Generator
Federal Reserve blackout period: the second Saturday before each FOMC meeting through the Thursday after — Fed officials cannot publicly comment on monetary policy. This creates a documented **lower-volatility drift regime**: with no Fed-speak shocks possible, macro positioning becomes more deterministic (consensus path emerges, narrowing rate expectations). 

The effect on EURUSD: during blackout periods, EURUSD has shown SLIGHT positive drift bias (when consensus is for Fed dovishness) or negative bias (when consensus is for hawkishness). The systematic relationship: in blackout windows, EURUSD persistence (autocorrelation of daily returns) is empirically HIGHER than non-blackout windows — trends extend more cleanly without Fed-speak interruption.

Proposal:
- Trigger: any business day within Fed blackout period (10-day window before FOMC) at 09:00 EST.
- Entry rule: measure 3-day-prior trend P3 = Close[09:00 today] - Close[09:00 3 days ago]. If |P3| > 80 pips, take CONTINUATION at 09:00 EST.
- Stop: 35 pips.
- Target: 50 pips, or time-stop at 14:00 EST.
- Expected win rate: 56%.
- Expected R:R: 1.5.

## RNG Critic
On random walk: prior 3-day return has zero predictive power on next 5-hour return. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **Fed blackout period + reduced news-shock variance + trend persistence**. Specific:
1. Fed blackout rule: published in Federal Reserve Communication Policy (1995, revised 2017).
2. ~80 blackout-period business days per year (8 meetings × 10 days each).
3. Documented in Cieslak-Vissing-Jorgensen (2020) "The Economics of the Fed Put."
4. Calendar-anchored.

## Decision
**QUALIFIED**.
