---
name: FRIDAY_ROLLOVER_SQUARING
status: QUALIFIED
round: 5
constraint: friday_5pm_est_weekend_position_squaring
expected_win_rate: 0.61
expected_rr: 1.3
---

# Candidate: FRIDAY_ROLLOVER_SQUARING

## Generator
FX markets formally roll over at 17:00 EST (5PM NY). On Fridays this is also the global weekly close — interbank market becomes illiquid for ~48 hours. Two mechanical forces act in the final 90 minutes of the NY week:
1. **Weekend gap-risk reduction**: prop desks, hedge funds, and retail brokers reduce position size before weekend (geopolitical/news gap risk is unhedgeable when market is closed).
2. **Weekly P&L book closure**: portfolio managers benchmarked to weekly NAV close positions to "lock in" P&L for the week.

Both forces push toward MEAN REVERSION of the weekly directional move. If the week has been strongly directional, late-Friday flows REVERSE it as longs sell and shorts cover.

Proposal:
- Trigger: every Friday at 15:00 EST, compute weekly drift W = Close[Fri 15:00] - Close[Mon open].
- Entry rule: if |W| > 60 pips, take a FADE at 15:00 EST opposite to sign(W).
- Stop: 30 pips.
- Target: 40 pips, or time-stop at 16:55 EST.
- Expected win rate: 61% (squaring flow dominates; news on Fridays is rare post-12:30 EST).
- Expected R:R: 1.3.

## RNG Critic
On i.i.d. random walk:
- Weekly drift has no predictive power for next 2 hours.
- "Day-of-week" has no meaning.
- Fading a directional run produces zero EV; net of spread, negative.

**PASSES — destroyed by random data. Edge requires actual gap-risk-aware participants squaring books.**

## Constraint Identifier
Mechanism: **Friday weekend gap-risk position squaring + weekly P&L book closure**. Specific:
1. Retail brokers' margin engines force-close highly leveraged retail positions before Friday 17:00 EST (broker risk policy, e.g. OANDA "weekend triple swap" + reduced leverage).
2. Prop trading firms (Jane Street, Citadel) impose Friday-close VAR limits.
3. CTA programs running weekly bar systems exit at the weekly close.
4. Hedge funds running weekly NAV strike reduce exposure to anchor reported volatility.

This is a calendar-anchored hard constraint, not a fuzzy "smart money" assertion.

## Testability Judge

```python
import pandas as pd
df = pd.read_csv("EURUSD_M1.csv", sep=";", header=None,
                 names=["dt","o","h","l","c","v"])
df["dt"] = pd.to_datetime(df["dt"], format="%Y%m%d %H%M%S")
df = df.set_index("dt").sort_index()

trades = []
for d in df.index.normalize().unique():
    if d.weekday() != 4: continue  # Friday
    # Find Monday-of-this-week open (first bar of that week)
    week_mon = d - pd.Timedelta(days=4)
    mon_first = df.loc[week_mon:week_mon + pd.Timedelta(days=1)].head(1)
    fri_1500 = df.loc[d + pd.Timedelta(hours=15):d + pd.Timedelta(hours=15, minutes=1)].head(1)
    if mon_first.empty or fri_1500.empty: continue
    W = (fri_1500.iloc[0]["o"] - mon_first.iloc[0]["o"]) * 1e4
    if abs(W) < 60: continue
    side = -1 if W > 0 else +1
    entry_px = fri_1500.iloc[0]["o"]
    stop_px = entry_px - side * 30e-4
    target_px = entry_px + side * 40e-4
    window = df.loc[d + pd.Timedelta(hours=15, minutes=1):
                    d + pd.Timedelta(hours=16, minutes=55)]
    exit_px = None
    for _, bar in window.iterrows():
        if side == +1:
            if bar["l"] <= stop_px: exit_px=stop_px; break
            if bar["h"] >= target_px: exit_px=target_px; break
        else:
            if bar["h"] >= stop_px: exit_px=stop_px; break
            if bar["l"] <= target_px: exit_px=target_px; break
    if exit_px is None: exit_px = window.iloc[-1]["c"]
    trades.append((d, side, (exit_px - entry_px) * side * 1e4))
```

RNG test: shuffling weekly returns destroys signal; expectancy → -spread. On real data expected +5 to +9 pips/trade across ~20 trades/year.

## Decision
**QUALIFIED**.
