---
name: Triple_Witching_Friday_VolCrush_Fade
status: QUALIFIED
round: 14
constraint: triple_witching_quarterly_friday_vol_crush
expected_win_rate: 0.62
expected_rr: 1.1
---

# Triple_Witching_Friday_VolCrush_Fade

## 1. Generator
**Hypothesis.** Quarterly triple-witching Fridays (third Friday of Mar, Jun, Sep, Dec — when stock-index futures, stock-index options, and single-stock options all expire) cause unusual cross-asset flow in the morning NY session as macro funds rebalance their equity-FX hedge ratio onto fresh quarterly contracts. Specifically, between 09:30 EST (NY equity open, when the witching cash flow hits) and 10:30 EST, EURUSD exhibits an elevated single-direction drift driven by the equity rebalance — and then sharply reverts between 10:30 and 12:00 EST as the rebalance flow exhausts and dealers unwind inventory.

The fade-the-morning-drift on triple-witching is distinct from Round 1 (London fix) and Round 7 (month-end) because:
- Quarterly (4/year × 14 = 56 events).
- Drift mechanism is equity-driven, not bond-driven.
- Window is 09:30–10:30 EST drift, then 10:30–12:00 EST fade — different clock window from any prior candidate.

- **Trigger.** Date is third Friday of {Mar, Jun, Sep, Dec}. Time 10:30 EST. Compute `Drift` = M1.close(10:30) − M1.close(09:30). Require `|Drift| ≥ 1.0 × ATR(20 daily) / 6.5` (half-hour normalized ATR).
- **Entry rule.** Enter OPPOSITE direction of `Drift` at 10:31 EST open.
- **Stop.** Extreme of 09:30–10:30 window on entry-against side + 5 pips.
- **Target.** 09:30 EST mid-price.
- **Time stop.** 12:00 EST.
- **Expected win rate.** ~62%.
- **Expected R:R.** ~1.1.

## 2. RNG Critic
On i.i.d. RW, the "third Friday of March / June / September / December" filter has no statistical privilege. The 09:30–10:30 drift conditional on top-quartile magnitude is a momentum-rank filter that has EV = 0 on RW. The 10:30–12:00 EST fade window provides no RW edge. **PASS** (fails on RW, Class A).

## 3. Constraint Identifier
**Mechanism: quarterly triple-witching equity-rebalance FX cross-flow.** On triple-witching Fridays, equity index futures (e.g., ES front-month) roll, and the resulting flow forces FX-overlay funds to rebalance their EUR-USD hedge ratio according to the new equity-quarterly weights. The rebalance concentrates in the first hour after NY equity open (09:30–10:30 EST), then exhausts. The post-rebalance fade is the dealer-inventory unwind. Sample: 56 events in 14 years (small but enough to detect a 0.3R+ effect at 2σ). Specific clock window + specific calendar date + specific mechanism. NOT vague.

## 4. Testability Judge
```
triple_witching_dates = [third_friday(year, month) for year in dataset for month in {3,6,9,12}]
for d in triple_witching_dates:
    p_0930 = close(d + "09:30:00")
    p_1030 = close(d + "10:30:00")
    atr_d  = ATR(20, daily_bars ending d-1)
    if any missing: skip
    Drift = p_1030 - p_0930
    if |Drift| < (atr_d / 6.5): skip
    direction = -sign(Drift)                      # fade
    entry = open(d + "10:31:00")
    extreme = (max(high ts in [09:30..10:30]) if direction<0
               else min(low ts in [09:30..10:30]))
    stop = extreme + (direction<0 ? +0.00050 : -0.00050)
    target = p_0930
    time_stop = d + "12:00:00"
    simulate to first of {stop, target, time_stop}
```

Sanity: report by quarter (Q1, Q2, Q3, Q4), expect Q1 (March end-of-fiscal for many funds) and Q4 (year-end rebalance) stronger than Q2/Q3.

## 5. Devil's Advocate
- **"Sample size 56 is too small."** It is small. The expected EV per trade (~0.3R) implies at 56 trades the 2σ confidence interval is wide (≈ ±0.4R). The candidate qualifies as a *hypothesis to test*, but cannot be deployed standalone — should be combined with the other quarterly candidates (Round 7 month-end overlap on Mar/Jun/Sep/Dec last business day if it coincides with witching = compound trigger).
- **"What's the mechanism distinct from generic month-end?"** Triple witching is the third Friday, not the last business day. They don't coincide. The flow is equity-driven (re-establishing FX hedge on the new futures contract), not bond-NAV-driven. Mechanism is genuinely distinct.
- **"Equity-FX rebalance happens daily for some funds."** True, but only triple-witching has the *concentrated* flow due to contract roll. Daily rebalancing is amortized.
- **"Why fade not ride?"** Because the rebalance is a one-shot flow that exhausts in 60–90 minutes; the price impact is transient (dealer accumulation) and reverses as dealers unwind. Same structural logic as the WMR fix.
- **Conclusion.** Devil's main concern is sample size — accept with explicit caveat: "test on real data; deploy only if EV per trade > 0.5R, given the small sample." **PASS WITH CAVEAT.**

## 6. RNG Test Result
RW filtered to "56 randomly chosen dates" gives PF = 1.00 ± large noise. The triple-witching subset on real data should show PF measurably above 1.0 if mechanism is real. **Edge is calendar-conditional and quarterly-flow-driven.**

## Verdict: QUALIFIED (with sample-size caveat)
