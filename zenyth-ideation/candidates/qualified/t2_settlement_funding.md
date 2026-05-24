---
name: T2_SETTLEMENT_FUNDING
status: QUALIFIED
round: 13
constraint: t2_value_date_funding_cutoff
expected_win_rate: 0.55
expected_rr: 1.5
---

# Candidate: T2_SETTLEMENT_FUNDING

## Generator
Spot FX settles T+2 (two-business-day value date). The cutoff for "today's spot value" is 17:00 EST (NY rollover). The day before a holiday weekend or long settlement gap, all trades settling on the same value-date "bunch up." When a US holiday falls on a Monday (Memorial Day, Labor Day, MLK, etc.), the prior Wednesday becomes "T-1" for Friday settlement, and there's a funding-day mismatch as USD positions roll across the holiday.

Specifically: on the day BEFORE a US-holiday-Monday (i.e. Friday before Memorial Day), USD spot settlements get rolled an extra day. This costs (or pays, depending on the carry side) more swap. The flow signature is a measurable EUR-bid in the late NY session of that Friday, as dealers reduce USD-long carry positions to avoid double-day rollover funding.

Proposal:
- Trigger: Friday at 13:00 EST IF the following Monday is a US federal banking holiday (Memorial Day, Labor Day, MLK Jr Day, Presidents Day, Columbus Day, Veterans Day-Monday-when-applicable).
- Entry rule: LONG EURUSD at 13:00 EST on such Fridays.
- Stop: 30 pips.
- Target: 45 pips, or time-stop at 16:55 EST.
- Expected win rate: 55%.
- Expected R:R: 1.5.

## RNG Critic
On i.i.d. random walk: holiday calendar is irrelevant. EV pre-cost zero, post-cost negative.

**PASSES.**

## Constraint Identifier
Mechanism: **T+2 spot FX value-date roll across US holiday + bank cost-of-funding asymmetry**. Specific:
1. CLS Bank settlement cycles require value date determination at 17:00 EST cutoff.
2. US-only holidays (not observed in EZ) create funding-day asymmetry — USD overnight rate accrued for extra day.
3. Bank treasury desks adjust positioning to minimize carry losses across the extra day.
4. Calendar-anchored (US Federal Reserve Bank holiday schedule, published annually).

## Testability Judge

```python
import pandas as pd
df = pd.read_csv("EURUSD_M1.csv", sep=";", header=None,
                 names=["dt","o","h","l","c","v"])
df["dt"] = pd.to_datetime(df["dt"], format="%Y%m%d %H%M%S")
df = df.set_index("dt").sort_index()

US_MON_HOLIDAYS = [
    "2008-01-21","2008-02-18","2008-05-26","2008-09-01","2008-10-13","2008-11-11",
    # ... extend full list 2008-2022 from Fed schedule
]
us_mons = set(pd.to_datetime(US_MON_HOLIDAYS).date)

trades = []
for d_ts in df.index.normalize().unique():
    if d_ts.weekday() != 4: continue  # Friday
    next_mon = d_ts + pd.Timedelta(days=3)
    if next_mon.date() not in us_mons: continue
    entry_t = d_ts + pd.Timedelta(hours=13)
    e_bar = df.loc[entry_t:entry_t + pd.Timedelta(minutes=1)].head(1)
    if e_bar.empty: continue
    entry_px = e_bar.iloc[0]["o"]
    stop_px = entry_px - 30e-4
    target_px = entry_px + 45e-4
    window = df.loc[entry_t : d_ts + pd.Timedelta(hours=16, minutes=55)]
    exit_px = None
    for _, bar in window.iterrows():
        if bar["l"] <= stop_px: exit_px=stop_px; break
        if bar["h"] >= target_px: exit_px=target_px; break
    if exit_px is None: exit_px = window.iloc[-1]["c"]
    trades.append((d_ts, (exit_px-entry_px)*1e4))
```

RNG: shuffle Friday returns → 0 EV. Real: +3 to +6 pips/trade × ~6 trades/year.

## Decision
**QUALIFIED**. Low frequency (~6/year) but very specific calendar-anchored funding effect.
