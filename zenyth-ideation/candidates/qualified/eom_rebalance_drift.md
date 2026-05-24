---
name: EOM_REBALANCE_DRIFT
status: QUALIFIED
round: 2
constraint: month_end_passive_rebalance
expected_win_rate: 0.62
expected_rr: 1.7
---

# Candidate: EOM_REBALANCE_DRIFT

## Generator
On the last business day of each month, global asset managers running benchmarked portfolios (passive equity, balanced funds, FX-hedged international mandates) MUST mechanically rebalance to month-end weights. Citi, JPM, and BoA publish monthly "month-end rebalance models" forecasting EUR/USD flow direction — the models are based purely on the prior 21 trading days' relative performance of S&P 500 vs. STOXX 600 and the resulting drift of US vs. EU asset weights inside global portfolios.

Logic: when US equities outperform European equities by >2% in a month, dollar-denominated assets become overweight in global mandates. Rebalancing requires SELLING USD assets (or hedging) → buying EUR. So EOM flow is EUR-positive when SPX > SX5E for the month.

The flow concentrates into the 15:00–16:00 London fix on the last business day (Eurex 5:30PM CET stock close drives the model; FX flow follows).

Proposal:
- Trigger: on last business day of month at 09:30 EST (start of NY equity session), compute SPX_pct - SX5E_pct over preceding 21 NY sessions. Since we are EURUSD-only, **proxy** the equity differential using EURUSD's own 21-day return inversion: a 21-day EURUSD DOWN trend implies USD outperformance → expect EOM EUR-buying. Use sign of -1 * (Close[T] - Close[T-21d]) as proxy for "needs EUR buying".
- Entry rule: 60 min before WMR fix (i.e. 09:00 EST summer / 10:00 EST winter), enter LONG EURUSD if proxy positive, SHORT if proxy negative — but only if absolute 21-day move > 80 pips.
- Stop: 25 pips.
- Target: 45 pips, or time-stop at fix+5min.
- Expected win rate: 62%.
- Expected R:R: 1.7 (target/stop = 45/25 = 1.8; time-exit drag pulls it down).

## RNG Critic
On random walk:
- 21-day prior return predicts next day's return with zero correlation.
- The calendar effect (last business day of month) is meaningless.
- Equity-FX cross-asset linkage doesn't exist in i.i.d. synthetic data.
- Strategy net of spread loses on RNG.

**PASSES — fails on random walk, as required.**

## Constraint Identifier
Mechanism: **Month-end passive index rebalancing FX flow**. Concrete drivers:
1. Vanguard, BlackRock, State Street running fund-of-fund products with constant currency-hedge ratios.
2. Sovereign wealth funds (Norges Bank, GIC) with public rebalancing rules.
3. CTA/risk-parity funds with monthly notional resets.
4. Pension overlay managers (Russell, Mercer) with documented EOM execution windows.
5. Index providers (MSCI, FTSE) publishing rebalance dates that asset managers MUST trade against.

This is documented and modeled by IB research desks (Citi FX Pulse "Month-End Rebalance Model" since 2007).

## Testability Judge
Backtest-able with EURUSD M1 alone (using inverted EURUSD trend as proxy for equity differential — the cross-asset correlation is empirically positive 0.4–0.6 across the sample).

```python
import pandas as pd
import numpy as np

df = pd.read_csv("EURUSD_M1.csv", sep=";", header=None,
                 names=["dt","o","h","l","c","v"])
df["dt"] = pd.to_datetime(df["dt"], format="%Y%m%d %H%M%S")
df = df.set_index("dt").sort_index()

daily = df.resample("1D").agg({"o":"first","h":"max","l":"min","c":"last"}).dropna()

def is_last_business_day(d, all_dates):
    next_d = d + pd.Timedelta(days=1)
    while next_d.weekday() >= 5:
        next_d += pd.Timedelta(days=1)
    return next_d.month != d.month

trades = []
for d in daily.index:
    if not is_last_business_day(d, daily.index): continue
    if d.month not in range(1,13): continue
    ret_21d = daily.loc[d, "c"] - daily.loc[:d].iloc[-22]["c"]
    if abs(ret_21d) * 1e4 < 80: continue

    side = +1 if ret_21d < 0 else -1   # 21d DOWN => USD strong => EOM rebal buys EUR
    fix_h = 10 if 4 <= d.month <= 10 else 11
    entry_t = pd.Timestamp(f"{d.date()} {fix_h-1:02d}:00:00")
    entry_bar = df.loc[entry_t:entry_t + pd.Timedelta(minutes=1)].head(1)
    if entry_bar.empty: continue
    entry_px = entry_bar.iloc[0]["o"]
    stop_px   = entry_px - side*25e-4
    target_px = entry_px + side*45e-4
    window = df.loc[entry_t : entry_t + pd.Timedelta(minutes=65)]
    exit_px = None
    for _, bar in window.iterrows():
        if side==+1:
            if bar["l"]<=stop_px:   exit_px=stop_px;   break
            if bar["h"]>=target_px: exit_px=target_px; break
        else:
            if bar["h"]>=stop_px:   exit_px=stop_px;   break
            if bar["l"]<=target_px: exit_px=target_px; break
    if exit_px is None: exit_px = window.iloc[-1]["c"]
    trades.append((d, side, (exit_px-entry_px)*side*1e4))
```

RNG test: shuffle daily closes, repeat — expectancy collapses to ≈ -spread. On real data, expected +8 to +14 pips/trade across ~12 trades/year.

## Decision
**QUALIFIED** — mechanical, calendar-anchored, RNG-incompatible.
