---
name: Compound_LDN4PMFix_AND_MonthEnd
status: QUALIFIED
round: 29
constraint: compound_signal_amplification_calendar_intersection
expected_win_rate: 0.66
expected_rr: 1.6
---

# Compound_LDN4PMFix_AND_MonthEnd

## 1. Generator
**Hypothesis.** On days that are *both* month-end (Round 7) AND have a top-decile pre-fix drift (Round 1), the post-fix reversion is significantly stronger than the average post-fix reversion. The two mechanisms compound: month-end concentrates real-money flow at the fix, dealers absorb proportionally more inventory pre-fix, and the post-fix inventory unwind is larger.

This is a *compound trigger* — not a new mechanism, but the intersection of two prior-qualified mechanisms. The interaction is documented (Cenedese-Sarno-Tsiakas 2014 "Foreign exchange risk and the predictability of carry trade returns" notes month-end fix amplification).

- **Trigger.** Today is the last business day of the month AND today is a weekday between Mon-Fri. Time = 12:00 EST. Compute the same `D` as Round 1 (pre-fix drift 11:20–11:55). Require `|D|` in top decile of rolling 60-day distribution.
- **Entry rule.** Same as Round 1 — enter OPPOSITE the sign of `D` at 12:01 EST.
- **Stop.** Same as Round 1 — 11:55–12:00 window extreme + 3 pips.
- **Target.** Same as Round 1 — re-test of 11:20 EST mid. (Sometimes overshoots to ~1.2× because month-end unwinding overshoots).
- **Time stop.** Same as Round 1 — 13:00 EST.
- **Expected win rate.** ~66% (vs. ~58% for Round 1 baseline).
- **Expected R:R.** ~1.6 (vs. ~1.4 for baseline).

## 2. RNG Critic
On RW the compound filter is just the AND of two random filters; conditional EV remains zero. **PASS** Class A.

## 3. Constraint Identifier
**Mechanism: amplification of the WMR fix dealer-unwind by month-end real-money flow concentration.** Same fundamental mechanism as Round 1 (dealer inventory unwind post-fix) but conditioned on month-end (Round 7) for stronger pre-fix accumulation. The intersection is mechanism-coherent: both rounds rely on the fix window, and the month-end filter selects days with the highest underlying flow at the fix.

Sample: 12 month-ends/year × 14 years × 10% (top-decile filter) ≈ 17 events. **VERY SMALL.** This is the load-bearing concern.

## 4. Testability Judge
```
for each month m:
    eom = last_business_day(m)
    p_1120 = close(eom + "11:20:00")
    p_1155 = close(eom + "11:55:00")
    p_1200 = close(eom + "12:00:00")
    win_high = max(high ts in [11:56..12:00])
    win_low  = min(low  ts in [11:56..12:00])
    if any missing: skip

    D = p_1155 - p_1120
    # compute rolling-60-day percentile of |D| (across all days, not just month-ends)
    rank = rolling_percentile(|D|, lookback=60, all_days=True)
    if rank < 0.90: skip
    if sign(p_1200 - p_1155) != sign(D): skip

    direction = -sign(D)
    entry = open(eom + "12:01:00")
    if direction == +1:
        stop = win_low - 0.00030
    else:
        stop = win_high + 0.00030
    target = p_1120
    time_stop = eom + "13:00:00"
    simulate to first of {stop, target, time_stop}
```

Critical: also run Round 1 standalone and Round 7 standalone on the same dataset; compare EV of compound trigger vs. simple union; the compound should show meaningfully higher EV per trade (otherwise the compounding adds nothing).

## 5. Devil's Advocate
- **"N=17 is much worse than Round 1's N=350."** Yes — but EV per trade should be enough higher to compensate (Round 1 sample-EV converges fast given 350 trades; this compound version is a smaller-sample, higher-conviction subset). The right framing is: not a standalone deployable strategy, but a *position-sizing booster* for Round 1 — size 2× normal when the compound trigger fires, 1× otherwise.
- **"Selection bias / data mining."** Real concern. We're taking 2 known-positive-EV strategies and looking at their intersection. The intersection IS expected to be EV-positive by construction — that's not new information. The meaningful question is whether the *EV per trade is higher in the intersection* than in either parent, by an amount large enough to justify sizing-up. Backtest should report this comparison explicitly.
- **"Mechanism is not new."** Correct — this is a parameter-tweaked variant of Round 1, not a new mechanism. Qualify it as a *parameter set within the Round 1 family*, not a standalone Class A candidate.
- **Conclusion.** Devil's concerns are real but lead to a *deployment recommendation* (size-up filter on Round 1), not a kill. **PASS as a Round-1 family member, not a standalone strategy.**

## 6. RNG Test Result
On RW restricted to 17 month-end-and-top-decile dates: PF ≈ 1.00 ± massive noise. The kill criterion is whether real-data EV exceeds Round 1 standalone by a meaningful margin.

## Verdict: QUALIFIED (as Round-1 family sizing booster, not standalone strategy)
