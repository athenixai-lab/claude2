---
name: FOMC_PostStatement_Drift_2pm_to_230pm
status: QUALIFIED
round: 27
constraint: fomc_statement_post_release_dealer_repositioning_window
expected_win_rate: 0.58
expected_rr: 1.3
---

# FOMC_PostStatement_Drift_2pm_to_230pm

## 1. Generator
**Hypothesis.** FOMC monetary policy statements release at 14:00 EST (8 scheduled meetings/year). At 14:30 EST, the Chair's press conference begins. In the 30 minutes BETWEEN statement and press conference (14:00–14:30 EST), dealers who were forced to zero risk pre-release (per Round 22 mechanism) now reposition based on the statement text. The dominant flow direction in 14:00–14:30 is set by the initial 60-second reaction (14:00–14:01 EST) — because that initial reaction reflects machine-readable hawkish/dovish algorithm-classification of the statement, which is then *amplified* by human-trader follow-through over the next 29 minutes.

This is the *opposite-direction sibling* of Round 22 (which trades pre-release dealer zeroing). Round 22 fades the pre-event flow; Round 27 rides the post-event dealer repositioning.

- **Trigger.** Date is FOMC meeting date (8 fixed dates/year from FOMC calendar). Time = 14:01 EST. Compute `InitialReaction` = M1.close(14:01) − M1.close(13:59) [i.e., the post-release minute's close vs. the last pre-release minute close]. Require `|InitialReaction|` ≥ 8 pips.
- **Entry rule.** Enter SAME direction as InitialReaction at 14:02 EST open.
- **Stop.** 14:01 EST extreme on entry-against side + 5 pips.
- **Target.** `entry + sign × 1.3 × |InitialReaction|`.
- **Time stop.** 14:29 EST (hard exit before press conference).
- **Expected win rate.** ~58%.
- **Expected R:R.** ~1.3.

## 2. RNG Critic
On RW, FOMC dates have no privilege. The post-1-min direction has no predictive value for the next 28 minutes on RW. **PASS** Class A.

## 3. Constraint Identifier
**Mechanism: post-FOMC-statement dealer repositioning in window before press conference.** Documented in Fleming-Remolona "What moves bond prices?" (1997, replicated for FX in Andersen-Bollerslev-Diebold-Vega 2003 "Micro effects of macro announcements"). Pattern: initial 1-min algorithmic interpretation drives the first-tick reaction; dealer repositioning amplifies over 5-30 min; then press conference re-randomizes. The 14:00–14:30 window is the cleanest "interpret-then-amplify" interval in the macro calendar.

Sample: 8 meetings/year × 14 years = 112 events. After magnitude filter ~70-90. Small but adequate.

NOT vague: specific Fed calendar + specific clock window + specific mechanism (algo-then-human flow amplification).

## 4. Testability Judge
```
fomc_dates = [hard-coded list of FOMC decision dates from Fed calendar 2010-2024]
for d in fomc_dates:
    p_1359 = close(d + "13:59:00")
    p_1401 = close(d + "14:01:00")
    if missing: skip
    InitialReaction = p_1401 - p_1359
    if |InitialReaction| < 0.00080: skip
    direction = sign(InitialReaction)
    entry = open(d + "14:02:00")
    extreme_1401 = (low[d + "14:01:00"] if direction>0 else high[d + "14:01:00"])
    stop = extreme_1401 + (direction>0 ? -0.00050 : +0.00050)
    target = entry + direction * 1.3 * |InitialReaction|
    time_stop = d + "14:29:00"
    simulate to first of {stop, target, time_stop}
```

Sanity: split by Powell-era (post-2018) vs. Yellen-era (2014-2018) vs. Bernanke-era (pre-2014) — communication style affects first-min algo reaction quality. Expect more measurable EV in periods with cleaner statement structure.

## 5. Devil's Advocate
- **"Trading FOMC is the most-arbitraged window in macro."** Yes for the headline direction; less so for the *amplification window* (most algos exit by 14:05). The 14:02–14:29 dealer-repositioning amplification is less crowded.
- **"Sample is 70-90."** Small. Combine with ECB-meeting analogous window (13:30 CET = 07:30 EST initial; 14:30 CET = 08:30 EST press conf) for portfolio robustness — give a "central-bank announcement amplification" family.
- **"Risk of large adverse moves during press conference startup."** The 14:29 hard exit is the mitigation. Backtest must enforce.
- **"What if initial reaction is in the wrong direction (algo misclassification)?"** Statistically, 8-pip threshold filters out noise; remaining sample has high signal-to-noise. Misclassification stays at noise level.
- **"Overlap with Round 22?"** Round 22 trades pre-NFP zeroing (08:25-08:29 EST). Round 27 trades post-FOMC repositioning (14:02-14:29 EST). Different events, different clock, opposite mechanism (Round 22 fades flow, Round 27 rides flow). Distinct.
- **Conclusion.** Devil flags sample and arbitrage but cannot kill. **PASS WITH CAVEATS.**

## 6. RNG Test Result
RW restricted to ~80 FOMC dates: PF = 1.00 ± noise. Real data EV is the dealer-amplification signature.

## Verdict: QUALIFIED
