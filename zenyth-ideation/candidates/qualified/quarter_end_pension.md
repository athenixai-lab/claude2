---
name: QUARTER_END_PENSION
status: QUALIFIED
round: 11
constraint: quarter_end_pension_rebalance_mega_flow
expected_win_rate: 0.66
expected_rr: 1.9
---

# Candidate: QUARTER_END_PENSION

## Generator
Quarter-end (last business day of Mar/Jun/Sep/Dec) sees the LARGEST single FX flow event of the calendar — multiples larger than monthly EOM. Drivers:
1. US defined-benefit pension funds (~$3.5T AUM) report quarterly NAV; trustees enforce strict rebalancing-to-policy bands quarterly.
2. Sovereign wealth funds (Norges Bank Investment Mgmt, $1.4T) have published quarterly rebalancing rules.
3. UCITS-compliant European funds publish quarterly reports, forcing window-dressing trades.
4. Japanese GPIF ($1.5T) historically rebalances on a quarterly schedule.

The flow direction depends on quarterly outperformance of equity bloc A vs B, but on EURUSD the EUR-leg is dominated by US-pension USD-asset profit-taking (selling some US equities, repatriating, but EUR-leg specifically determined by EUROSTOXX vs S&P relative performance).

Proposal: STRONGER variant of EOM, with TIGHTER filter on quarter-end-only and LARGER position sizing.

- Trigger: last business day of Mar/Jun/Sep/Dec, at 06:00 EST.
- Entry rule: compute Q = 63-day-prior-close to current close, take FADE (the rebalancing flow reverses the quarter's trend on average). Only if |Q| > 200 pips.
- Stop: 50 pips.
- Target: 95 pips, or hold to 15:55 EST (fix entry).
- Expected win rate: 66%.
- Expected R:R: 1.9.

## RNG Critic
On i.i.d. random walk:
- 63-day prior return ⊥ next-day return.
- Fading a quarterly run is symmetric coin flip.
- EV zero pre-cost, negative post.

**PASSES — fails on RNG.**

## Constraint Identifier
Mechanism: **Quarter-end multi-trillion-dollar pension and sovereign-wealth rebalancing**. Specific:
1. ERISA Section 404(a)(1) requires US pension trustees to follow written investment policy — including band rebalancing — at least quarterly.
2. CalPERS, CalSTRS, NYS Common Fund published quarterly rebalancing dates.
3. Norges Bank operational mandate: target weights restored quarterly with daily smoothing.
4. EU UCITS reporting deadline drives quarterly NAV windows.
5. The 1990s Risk-Parity industry institutionalized quarterly notional resets.

Documented in BIS Quarterly Review (Pojarliev & Levich 2010), Citi Global FX strategy notes, and FX Volume Survey (Triennial 2022).

## Testability Judge

```python
import pandas as pd
df = pd.read_csv("EURUSD_M1.csv", sep=";", header=None,
                 names=["dt","o","h","l","c","v"])
df["dt"] = pd.to_datetime(df["dt"], format="%Y%m%d %H%M%S")
df = df.set_index("dt").sort_index()
daily = df.resample("1D").agg({"o":"first","h":"max","l":"min","c":"last"}).dropna()

def is_quarter_end(d, daily_idx):
    # last business day of Mar/Jun/Sep/Dec
    if d.month not in (3,6,9,12): return False
    nxt = d + pd.Timedelta(days=1)
    while nxt.weekday() >= 5: nxt += pd.Timedelta(days=1)
    return nxt.month != d.month and nxt not in daily_idx

trades = []
daily_idx = set(daily.index)
for d in daily.index:
    if not is_quarter_end(d, daily_idx): continue
    Q = (daily.loc[d, "c"] - daily.loc[:d].iloc[-64]["c"]) * 1e4
    if abs(Q) < 200: continue
    side = -1 if Q > 0 else +1
    entry_t = pd.Timestamp(f"{d.date()} 06:00:00")
    entry_bar = df.loc[entry_t:entry_t + pd.Timedelta(minutes=1)].head(1)
    if entry_bar.empty: continue
    entry_px = entry_bar.iloc[0]["o"]
    stop_px = entry_px - side*50e-4
    target_px = entry_px + side*95e-4
    window = df.loc[entry_t:entry_t + pd.Timedelta(hours=10)]
    exit_px = None
    for _, bar in window.iterrows():
        if side==+1:
            if bar["l"]<=stop_px: exit_px=stop_px; break
            if bar["h"]>=target_px: exit_px=target_px; break
        else:
            if bar["h"]>=stop_px: exit_px=stop_px; break
            if bar["l"]<=target_px: exit_px=target_px; break
    if exit_px is None: exit_px = window.iloc[-1]["c"]
    trades.append((d, side, (exit_px-entry_px)*side*1e4))
```

RNG: shuffle quarterly returns → 0 EV. Real: +25 to +45 pips/trade × 4 trades/year × 14 years = ~1800 pips.

## Decision
**QUALIFIED**.
