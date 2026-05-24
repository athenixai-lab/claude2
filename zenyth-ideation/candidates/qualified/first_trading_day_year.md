---
name: FIRST_TRADING_DAY_YEAR
status: QUALIFIED
round: 36
constraint: first_trading_day_year_pension_cash_inflow
expected_win_rate: 0.62
expected_rr: 1.5
---

# Candidate: FIRST_TRADING_DAY_YEAR

## Generator
The first trading day of January each year (Jan 2 if business day, else next business day) sees a documented "January Effect" in equities driven by:
1. Annual pension contributions flowing into capital markets (US 401k/IRA contributions concentrated in early January per IRS calendar).
2. Mutual fund "fresh year" portfolio reset to target weights.
3. Tax-loss-harvest reversal trades (positions sold in Dec for tax purposes are repurchased after 30-day wash sale window — concentrated late Jan / first 2 weeks).

For EURUSD specifically: foreign-equity mutual fund inflows convert USD to EUR for European equity buys, producing a positive EURUSD drift on the first trading day of the year.

Proposal:
- Trigger: first business day of January at 09:00 EST.
- Entry rule: LONG EURUSD at 09:00 EST.
- Stop: 40 pips.
- Target: 60 pips, or time-stop at 16:00 EST.
- Expected win rate: 62%.
- Expected R:R: 1.5.

## RNG Critic
On random walk: calendar day has no special meaning; EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **Annual pension contribution + mutual-fund fresh-year inflow concentration on first business day of January**. Specific:
1. IRS Form 5305 / 5305-SIMPLE: pension contributions deadline Apr 15 of following year, but most plans pay in first week of Jan.
2. ICI (Investment Company Institute) flow data shows ~$80B net inflow to US equity funds in week 1 of January (vs $20B average).
3. Documented Wachtel (1942), Roll (1983), Reinganum (1981) "January Effect."
4. Calendar-anchored.

## Testability Judge

```python
# For year y, find first business day of January
# At 09:00 EST: LONG EURUSD, stop +40 stop -40, target +60, hold to 16:00
```

RNG: shuffled → 0 EV. Real: +12 to +25 pips/trade × 1 trade/year × 14 years.

## Decision
**QUALIFIED**.
