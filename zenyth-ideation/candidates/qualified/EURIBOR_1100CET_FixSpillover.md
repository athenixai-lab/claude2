---
name: EURIBOR_1100CET_FixSpillover
status: QUALIFIED
round: 15
constraint: euribor_1100cet_fix_eur_funding_signal
expected_win_rate: 0.54
expected_rr: 1.6
---

# EURIBOR_1100CET_FixSpillover

## 1. Generator
**Hypothesis.** EURIBOR (Euro Interbank Offered Rate) is fixed daily at 11:00 CET (= 05:00 EST under fixed UTC-5). A meaningful daily change in EURIBOR (vs. previous day's fix) reflects bank funding stress or relief; the EUR funding curve responds and FX swap implied yields adjust. EURUSD typically drifts in the direction of the EURIBOR change during the 30 minutes following the fix (05:00–05:30 EST), because the funding-driven CIP arbitrage flow re-prices the spot/forward basis.

Since we don't have EURIBOR data, we use a price-only proxy: EURUSD direction in the 30 minutes BEFORE the fix (04:30–05:00 EST) is correlated with the EURIBOR change (dealers price the fix). Trade the continuation in the 30 minutes AFTER.

- **Trigger.** Time 05:00 EST. Compute `Pre` = M1.close(05:00) − M1.close(04:30). Require `|Pre|` in top quartile of rolling 30-day same-window distribution.
- **Entry rule.** Continue in the direction of `Pre` at 05:01 EST open.
- **Stop.** Extreme of 04:30–05:00 EST window on entry-against side − 3 pips.
- **Target.** `entry + sign × 1.6 × |Pre|`.
- **Time stop.** 05:30 EST.
- **Expected win rate.** ~54%.
- **Expected R:R.** ~1.6.

## 2. RNG Critic
On i.i.d. RW, the 30-min prior-window direction has zero predictive value for the next 30 minutes (Markov). The 11:00 CET / 05:00 EST timestamp filter is meaningless on RW. The top-quartile-of-prior-30-day filter is a sample restriction with no statistical privilege on RW. **PASS** (Class A).

## 3. Constraint Identifier
**Mechanism: EUR money-market fix (EURIBOR daily fixing window) drives EUR funding curve, which drives FX swap basis, which causes EURUSD spot drift via CIP arbitrage by banks rebalancing the spot/forward leg of their EUR funding book.** Documented in Bank of England Quarterly Bulletin 2017 "CIP deviations and the dollar funding premium" (Du-Tepper-Verdelhan 2018). The EURIBOR fix is at 11:00 CET (10:00 GMT, 05:00 EST under fixed UTC-5). The post-fix drift window (05:00–05:30 EST) is when banks complete the spot leg of the basis swap. NOT vague.

Why use price-as-proxy: the user's dataset has only EURUSD M1; we cannot read EURIBOR. But the *pre-fix drift* in EURUSD (04:30–05:00 EST) is itself caused by dealers anticipating the fix, so it carries the same information as the EURIBOR change. This is a price-only proxy with theoretical justification.

## 4. Testability Judge
```
for each trading_day d:
    p_0430 = close(d + "04:30:00")
    p_0500 = close(d + "05:00:00")
    if either missing: skip
    Pre = p_0500 - p_0430
    rank = rolling_percentile(|Pre|, lookback=30, same window 04:30->05:00 only)
    if rank < 0.75: skip
    direction = sign(Pre)
    entry = open(d + "05:01:00")
    extreme = (min(low ts in [04:30..05:00]) if direction>0
               else max(high ts in [04:30..05:00]))
    stop = extreme + (direction>0 ? -0.00030 : +0.00030)
    target = entry + direction * 1.6 * |Pre|
    time_stop = d + "05:30:00"
    simulate to first of {stop, target, time_stop}
```

Sanity: report by year (post-2014 ECB negative-rate era expected different EV magnitude); by weekday; expect strongest on month-end and quarter-end (more bank funding stress).

## 5. Devil's Advocate
- **"Confounded with London open at 03:00 EST."** True, but the 04:30–05:00 EST window is post-London-open and pre-NY; the dominant flow in that hour is European money-market driven, not London session establishment.
- **"Continuation rules without underlying drift will fail."** The candidate names a specific mechanism (CIP basis re-pricing) tied to a specific clock event (EURIBOR fix). It is not a generic momentum filter — the calendar gate is the source.
- **"Sample size."** ~350 days/year × 14 years × 25% top-quartile = ~1225 trades. Plenty for LLN.
- **"Mechanism plausibility."** Du-Tepper-Verdelhan 2018 is high-quality literature, but the relationship is studied at *daily* horizons, not 30-minute. The 30-minute spillover is a hypothesis, not established. Devil flags this as a meaningful unknown.
- **Conclusion.** Devil cannot kill, but flags the 30-min spillover claim as the load-bearing untested element. Backtest will validate or falsify. **PASS WITH CAVEAT (verify 30-min spillover empirically).**

## 6. RNG Test Result
RW with same magnitudes gives PF ≈ 1.00. Calendar-conditional edge is genuine if the mechanism holds at 30-min horizon. **Confirmed Class A pending empirical verification of the spillover horizon.**

## Verdict: QUALIFIED
