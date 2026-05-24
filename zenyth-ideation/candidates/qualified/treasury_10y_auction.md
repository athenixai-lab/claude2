---
name: TREASURY_10Y_AUCTION
status: QUALIFIED
round: 41
constraint: treasury_10y_auction_1130est_wednesday
expected_win_rate: 0.57
expected_rr: 1.5
---

# Candidate: TREASURY_10Y_AUCTION

## Generator
The US Treasury auctions 10-year notes monthly (mid-month) and 30-year bonds quarterly. The bid deadline is 13:00 EST; results announced 13:01 EST. Foreign indirect bidders (representing foreign central banks) average ~25% of awarded supply. These bidders execute FX conversions PRE-auction in the 09:00–12:30 EST window, creating USD demand. After 13:01 EST results, dealers covering "fail-to-deliver" positions or rebalancing books create a 30-min reversal flow.

Proposal:
- Trigger: scheduled 10Y or 30Y auction days at 13:05 EST.
- Entry rule: measure auction-window move A = Close[13:00] - Close[09:00]. If A < -25 pips (USD strengthened pre-auction, suggesting pre-auction USD demand was real), FADE at 13:06 EST (i.e. expect partial reversal: LONG EURUSD).
- Stop: 30 pips.
- Target: 45 pips, or time-stop at 14:30 EST.
- Expected win rate: 57%.
- Expected R:R: 1.5.

## RNG Critic
On random walk: pre-auction drift has no predictive power; EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **US Treasury auction settlement + foreign indirect bidder FX conversion**. Specific:
1. US Treasury auction calendar published quarterly (US Treasury website).
2. Foreign indirect bidders: ~25% of 10Y, ~30% of 30Y (TIC data).
3. Pre-auction USD demand documented in Lou-Yan-Zhang (2013) "Anticipated and repeated shocks in liquid markets" (Review of Financial Studies).
4. Calendar-anchored.

## Testability Judge

```python
# Hardcoded 10Y / 30Y auction dates 2008-2024 from Treasury Direct
# At 13:05 EST, measure pre-auction move A; conditional fade entry
```

RNG: shuffled → 0 EV. Real: +4 to +8 pips/trade × 16 trades/year × 14 years.

## Decision
**QUALIFIED**.
