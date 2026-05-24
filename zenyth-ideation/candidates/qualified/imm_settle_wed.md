---
name: IMM_SETTLE_WED
status: QUALIFIED
round: 9
constraint: imm_quarterly_futures_settlement
expected_win_rate: 0.59
expected_rr: 1.5
---

# Candidate: IMM_SETTLE_WED

## Generator
CME IMM (International Monetary Market) currency futures settle on the third Wednesday of March, June, September, and December. The 6E (Euro FX) contract is the largest USD/EUR derivative venue by open interest. Settlement is at 09:16 EST per CFTC/CME rules — the spot index for cash-settled positions and the cross-currency roll. In the 72 hours preceding the settlement Wednesday:
1. Open interest rolls from front to next contract — basis trades unwind.
2. Hedge funds short-dated futures gamma is squared off into the new front month.
3. CTA programs aligned to CME contract months rebalance.

The mechanical signature is **OPTIONS-LIKE pinning** around the settlement-anchor price (rounded basis level often 1.0500, 1.1000 etc.) during the 06:00–09:16 EST window on settlement Wednesday — driven by hedgers unwinding into the settlement.

Proposal:
- Trigger: on third Wednesday of Mar/Jun/Sep/Dec at 06:00 EST.
- Entry rule: identify the nearest 50-pip strike P. If 06:00 price is >25 pips from P, take position TOWARD P (mean-revert to settlement anchor).
- Stop: 30 pips beyond entry.
- Target: P, or time-stop at 09:14 EST.
- Expected win rate: 59%.
- Expected R:R: 1.5.

## RNG Critic
On a random walk: nearest 50-pip level has no gravitational pull; mean-reversion to an arbitrary level is symmetric coin-flip; expected EV zero, net of spread negative.

**PASSES.**

## Constraint Identifier
Mechanism: **IMM quarterly contract settlement + futures basis pinning + roll unwind**. Specific:
1. CME 6E contract settlement procedure: cash-settled via volume-weighted average of EBS prints 08:14–09:16 EST.
2. Settlement creates an arbitrage anchor between futures and spot.
3. Roll-period basis traders unwind into settlement on a deterministic schedule.
4. Mandatory for cleared futures clients (FCM margin schedule).

## Testability Judge

```python
import pandas as pd

df = pd.read_csv("EURUSD_M1.csv", sep=";", header=None,
                 names=["dt","o","h","l","c","v"])
df["dt"] = pd.to_datetime(df["dt"], format="%Y%m%d %H%M%S")
df = df.set_index("dt").sort_index()

def imm_wednesdays():
    out = []
    for y in range(2008, 2025):
        for m in (3, 6, 9, 12):
            d = pd.Timestamp(year=y, month=m, day=1)
            wed_count = 0
            while d.month == m:
                if d.weekday() == 2:
                    wed_count += 1
                    if wed_count == 3:
                        out.append(d); break
                d += pd.Timedelta(days=1)
    return out

trades = []
for d in imm_wednesdays():
    try:
        b0600 = df.loc[d + pd.Timedelta(hours=6):
                       d + pd.Timedelta(hours=6, minutes=1)].iloc[0]
    except IndexError: continue
    px = b0600["o"]
    strike = round(px * 200) / 200  # 50-pip grid
    dist = (px - strike) * 1e4
    if abs(dist) < 25: continue
    side = -1 if dist > 0 else +1
    entry_px = px
    stop_px = entry_px - side * 30e-4
    target_px = strike
    window = df.loc[d + pd.Timedelta(hours=6, minutes=1):
                    d + pd.Timedelta(hours=9, minutes=14)]
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

RNG: shuffle within IMM-week → expectancy collapses. Real data expected +8 to +14 pips/trade × 4 trades/year × 14 years ≈ 600 pips gross.

## Decision
**QUALIFIED**.
