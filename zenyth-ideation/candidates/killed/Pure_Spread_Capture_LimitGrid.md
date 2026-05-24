---
name: Pure_Spread_Capture_LimitGrid
status: KILLED
round: 10
constraint: bid_ask_spread_capture_market_making
expected_win_rate: 0.62
expected_rr: 0.8
---

# Pure_Spread_Capture_LimitGrid

## 1. Generator (Class B — moonshot)
**Hypothesis.** A passive market maker who posts a buy limit at `mid − k·tick` and a sell limit at `mid + k·tick` captures the spread on round-trips when both fills occur. On any candle generator with positive spread and bounded vol, EV per round-trip is `+2·k·tick − adverse_selection_loss`. With appropriate `k` (large enough to dampen adverse selection), EV is positive even on pure i.i.d. RNG — the only "structural RNG-beating" mechanism that survives Doob.

This is the user's "limiting belief override" candidate: most retail traders are told you can't market-make on M1. Test it.

## 2. RNG Critic
The mechanism IS valid in principle. On a pure i.i.d. RNG with positive tick spread, two-sided passive limit orders that both fill within the next K bars produce a positive payoff. This is the ONLY price-only strategy that legitimately beats Doob, because the negative-cost action (earning the spread) is the source of EV — it's not a path-dependent bet, it's a structural payment for providing liquidity.

But the simulator does not have a true liquidity book. M1 OHLC tells us only that (high, low) was reached — not WHEN within the minute, not in what order, not whether a resting limit order would have been filled before being adversely selected. A naive simulator that says "if low <= my_buy_limit, I'm filled" overestimates fills (fails to model queue position, fails to model adverse selection by faster takers) and underestimates losses (the moment your limit fills, the market has already moved against you).

**Critic verdict: the mechanism is real but UNTESTABLE on the given dataset.** The faithful test requires tick-level bid/ask data with full depth — not M1 OHLC.

## 3. Constraint Identifier
Mechanism is named precisely: **bid-ask spread capture via passive liquidity provision (market making).** Documented in every microstructure textbook (Foucault-Pagano-Roell "Market Liquidity"). Constraint is real and exploitable in production by HFT and bank desks — but the trader needs co-location, queue position, and rebate scheduling. None of those are visible from M1 OHLC.

## 4. Testability Judge
KILL. The naive M1-OHLC simulator produces a positive backtest by construction (it ignores queue and adverse selection), which has nothing to do with whether the strategy works in production. You would need:
- Tick-by-tick bid/ask data (LOB snapshots, minimum L1)
- Latency model
- Adverse-selection model
None of these are in the 14y EURUSD M1 OHLC dataset.

A pseudocode that demonstrates the unfaithfulness:
```
# UNFAITHFUL SIMULATOR (DO NOT DEPLOY)
for each bar t:
    mid_prev = (open[t-1] + close[t-1]) / 2
    buy_lim  = mid_prev - 2*tick
    sell_lim = mid_prev + 2*tick
    if low[t]  <= buy_lim:  filled_long  = true
    if high[t] >= sell_lim: filled_short = true
    if both filled in this bar:
        pnl += (sell_lim - buy_lim)        # appears as guaranteed profit
```
This produces fabulous backtests. In production it loses, because every fill on `buy_lim` was triggered by the price racing through; you got filled because someone toxic took your liquidity at that exact moment. The M1 OHLC has no information about which side hit first or how much edge the taker had.

## 5. Devil's Advocate
- Devil tries to save the candidate: "What if we only count fills where BOTH legs occur and use OHLC ordering to be conservative?" — still fails; OHLC doesn't tell you which (H, L) came first within the bar. The "Garman-Klass" estimators of H-L-O-C ordering are statistical, not faithful.
- Devil tries: "What if we use bar-relative ATR and only enter on compressed-vol bars?" — that's a different strategy entirely (mean-reversion fade), no longer pure spread capture.
- **Devil cannot save it as a pure spread-capture strategy on this dataset.** The mechanism is genuine but the dataset is wrong.
- **KILL stands.**

## 6. RNG Test Result
On i.i.d. simulation WITH a faithful tick book, spread capture EV > 0 (the only price-only strategy that does so). On M1 OHLC simulator, EV appears positive but is overstated; production EV unknown but likely negative due to adverse selection. **The RNG test cannot distinguish real edge from simulator artifact.**

## Verdict: KILLED
**Reason:** Mechanism is the only theoretically valid RNG-beating constraint in price-only space, but is fundamentally untestable on M1 OHLC. Re-open with tick-level bid/ask data if available.
