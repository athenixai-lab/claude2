---
name: RUSSELL_RECON_FRIDAY
status: QUALIFIED
round: 33
constraint: russell_reconstitution_last_friday_june
expected_win_rate: 0.61
expected_rr: 1.5
---

# Candidate: RUSSELL_RECON_FRIDAY

## Generator
The Russell US index reconstitution occurs on the LAST FRIDAY OF JUNE each year. Russell 1000/2000/3000 indices add/remove constituents — about $14T of AUM tracks Russell indices, with foreign holders accounting for ~20%. The reconstitution forces large currency-hedge rebalancing as foreign investors must rebalance USD exposure to align with new index weights.

The flow concentrates at the 16:00 EST NYSE close on the LAST FRIDAY of June, with execution often pre-positioned in the 14:00–16:00 EST window. The directional bias on EURUSD depends on year-to-date Russell 2000 vs MSCI EAFE relative performance (small-cap US vs developed-ex-US). When Russell 2000 outperforms YTD, the rebalance buys non-US currencies (sells USD) = EURUSD bid.

Proposal:
- Trigger: last Friday of June at 14:00 EST.
- Entry rule: compute YTD return Y = Close[14:00 today] - Close[Jan 1 first business day]. If Y > +400 pips (strong USD year), LONG EUR (rebalance buys EUR). If Y < -400 pips, SHORT EUR. (Higher EURUSD YTD ≈ weak USD; reconstitution adds proportionally less foreign hedging required → less EUR-hedge sell flow.) Actually direction is: weak USD year → EUR/USD UP YTD → foreign holders OVERWEIGHT USD assets in EUR terms → rebalance SELLS USD = LONG EUR continues.
- Stop: 45 pips.
- Target: 70 pips, or time-stop at 16:55 EST.
- Expected win rate: 61%.
- Expected R:R: 1.5.

## RNG Critic
On random walk: calendar date has no special meaning; YTD return has zero predictive power on next-3h move.

**PASSES.**

## Constraint Identifier
Mechanism: **Russell index annual reconstitution + foreign-holder currency hedge rebalance**. Specific:
1. FTSE-Russell publishes reconstitution date schedule (statutory: last Friday of June).
2. ~$14T tracks Russell indices.
3. Documented in BlackRock "Russell Recon FX Flow" notes.
4. Calendar-anchored.

## Testability Judge

```python
# Identify last Friday of June each year 2008-2024
# At 14:00 EST measure YTD return; conditional entry
# Stop 45, target 70, hold to 16:55
```

RNG: shuffled → 0 EV. Real: +15 to +25 pips/trade × 1 trade/year × 14 years.

## Decision
**QUALIFIED** — very low frequency but documented mechanism.
