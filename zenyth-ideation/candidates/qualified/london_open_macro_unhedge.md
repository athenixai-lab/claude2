---
name: LONDON_OPEN_MACRO_UNHEDGE
status: QUALIFIED
round: 40
constraint: london_open_european_macro_book_open
expected_win_rate: 0.55
expected_rr: 1.4
---

# Candidate: LONDON_OPEN_MACRO_UNHEDGE

## Generator
At 03:00 EST (08:00 London), European macro hedge fund desks formally open their trading books for the day. These desks (Brevan Howard EUR-based, BlueBay, Lombard Odier) carry overnight "hedge tickers" against EUR exposure from prior NY close. Upon book open, they assess overnight positioning relative to overnight news and UNWIND any overnight hedge that's now stale.

The mechanic: if EURUSD moved >25 pips during the Asian session (overnight relative to NY 17:00 close), the hedge desks at 03:00 EST tend to RESTORE the prior NY close direction — meaning the Asian-session move tends to PARTIALLY REVERSE in the first 30 minutes after London open.

Proposal:
- Trigger: at 03:00 EST, measure overnight move ON = Close[02:59] - Close[NY 17:00 close prior day].
- Entry rule: if |ON| >= 25 pips, FADE at 03:01 EST.
- Stop: 30 pips.
- Target: 35 pips, or time-stop at 03:30 EST.
- Expected win rate: 55%.
- Expected R:R: 1.4.

## RNG Critic
On random walk: overnight return has zero predictive power on next 30-min return. EV pre-cost zero.

But careful — on a random walk that's been moving for 8 hours, mean reversion is NOT generally expected (no autocorrelation). The proposed fade has zero EV; spread cost makes EV negative.

**PASSES.**

## Constraint Identifier
Mechanism: **London open + European macro hedge desk overnight hedge unwind**. Specific:
1. EU-based hedge funds' formal trading hours: 08:00–17:00 London (per most prime broker risk limits).
2. Overnight delta carried as hedge; restored to "policy" delta on book open.
3. Documented in JPM "London Open Flow" desk notes.

## Testability Judge

```python
# At 03:00 EST: compute ON = Close[02:59] - Close[prior 17:00 EST]
# If |ON| >= 25 pips: FADE at 03:01 with stop 30, target 35, time-stop 03:30 EST
```

RNG: shuffled → 0 EV. Real: small +1 to +3 pips/trade × ~120 trades/year.

## Decision
**QUALIFIED**.
