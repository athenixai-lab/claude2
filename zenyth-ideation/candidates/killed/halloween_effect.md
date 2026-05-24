---
name: HALLOWEEN_EFFECT
status: KILLED
round: 39
constraint: halloween_sell_in_may_seasonality
expected_win_rate: 0.52
expected_rr: 1.1
---

# Candidate: HALLOWEEN_EFFECT

## Generator
"Sell in May and go away, come back St Leger Day" — equity seasonality where May-October returns lag November-April. Hypothesized cause: vacation patterns, year-end tax distributions, Northern Hemisphere risk-aversion seasonality.

For EURUSD: if US equities underperform May-Oct, foreign holders may proportionally reduce USD-asset exposure → EUR/USD up. Trade: LONG EURUSD every May 1, exit October 31.

## RNG Critic
On random walk: calendar month has no special property. EV pre-cost zero.

But — this is a 6-MONTH HOLD strategy at M1 resolution. The variance over 6 months is enormous (3000+ pips realized over 6 months on EURUSD historically). Any conditional mean drift of ~50–100 pips/year is completely dwarfed by 6-month variance.

After spread/swap costs (6 months of triple-Wednesday swap, daily borrow cost), this is highly likely negative-EV.

PASSES RNG on EV grounds but FAILS variance/Sharpe — this is essentially a directional bet, not an exploitable constraint.

## Constraint Identifier
The mechanism is vague: "vacation patterns, year-end risk-aversion." No specific institutional flow, no specific time-of-day, no specific scheduled event. Just a calendar bias on the wrong time-frame (months) for an M1 system.

## Decision
**KILLED** — vague mechanism, wrong time-frame for M1, variance dominates. While the Halloween Effect IS documented in equities, the FX spillover is too noisy to qualify.
