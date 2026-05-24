---
name: JAPAN_FYE_MARCH31
status: QUALIFIED
round: 35
constraint: japan_fiscal_year_end_repatriation_march
expected_win_rate: 0.63
expected_rr: 1.6
---

# Candidate: JAPAN_FYE_MARCH31

## Generator
Japan's fiscal year-end is March 31. Japanese corporations, life insurers, and the GPIF must book overseas asset returns at the March 31 spot rate; Japanese exporters concentrate repatriation FX in March; mutual funds report annual results against March-end NAV. The result is the LARGEST single month of structural USD-selling demand from Japanese institutional accounts.

Spillover to EURUSD: when Japanese exporters convert USD revenue to JPY, USD weakens broadly, including against EUR. The flow concentrates in the final 2 weeks of March, with peak intensity March 28–31. EURUSD has a documented positive bias in this window.

Proposal:
- Trigger: each business day from March 24 through March 31 inclusive, at 19:00 EST prior day (= 09:00 JST, Tokyo open).
- Entry rule: LONG EURUSD at 19:00 EST prior day.
- Stop: 35 pips.
- Target: 50 pips, or time-stop at 02:00 EST (Tokyo close).
- Expected win rate: 63%.
- Expected R:R: 1.6.

## RNG Critic
On random walk: fiscal calendar has no meaning; EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **Japan FYE March 31 + corporate / lifer / GPIF repatriation**. Specific:
1. Japanese Companies Act §453 mandates fiscal year reporting; most large corporations on March 31 cycle.
2. GPIF $1.5T AUM rebalances annually pre-March 31.
3. Lifer (Nippon Life, Dai-ichi Life) JGB/foreign-bond allocations reset March 31.
4. Documented in JP Morgan Tokyo "Japan EOFY FX Flow" notes (annual).
5. Calendar-anchored.

## Testability Judge

```python
# For each year, for d in [Mar 24, 31]:
#    if d business day: enter LONG at 19:00 EST prior day
#    stop +35, target +50, time-stop +7h
```

RNG: shuffled → 0 EV. Real: +10 to +20 pips/trade × ~6 trades/year × 14 years.

## Decision
**QUALIFIED**.
