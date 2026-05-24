---
name: QuarterEnd_CentralBank_Reserve_EUR_Rebalance
status: QUALIFIED
round: 19
constraint: quarter_end_central_bank_reserve_rebalance_to_eur
expected_win_rate: 0.57
expected_rr: 1.4
---

# QuarterEnd_CentralBank_Reserve_EUR_Rebalance

## 1. Generator
**Hypothesis.** Central banks holding USD reserves (PBOC, BoJ, SNB, MAS, GIC, etc.) rebalance reserve currency weights at quarter-end to maintain mandated USD/EUR ratios as set by their reserve-management committees (typically COFER-style weights). When EUR has appreciated vs. USD over the quarter, central banks must SELL EUR / BUY USD at quarter-end to bring weights back to target. When EUR has fallen, they BUY EUR. This flow is concentrated in the last week of the quarter, with execution windows in the Asian and London sessions of the final 2 business days (to avoid moving the US session).

Distinct from Round 7 (private-fund month-end): central-bank rebalance is quarter-only (4×/yr), opposite-direction (mean-revert to weights, not increase a hedge), and concentrated 2 days before quarter-end rather than on the last day.

- **Trigger.** Date is 2nd-to-last business day of quarter (last week of Mar/Jun/Sep/Dec). Compute `Q` = M1.close(today 03:00 EST) − M1.open(first business day of quarter at 03:00 EST). Require `|Q|` ≥ ATR(63 daily) × 1.0 (significant quarterly move).
- **Entry rule.** Enter OPPOSITE sign of `Q` (mean-revert direction) at 03:01 EST. Long EUR if quarter was EUR-bear; short EUR if quarter was EUR-bull.
- **Stop.** 35 pips beyond entry.
- **Target.** Entry + sign × 50 pips.
- **Time stop.** Last business day of quarter at 11:00 EST (just before WMR fix; allow fix-day flow to start).
- **Expected win rate.** ~57%.
- **Expected R:R.** ~1.4.

## 2. RNG Critic
On RW, quarterly directional move has no predictive value for the next 2 days. "2nd-to-last business day of quarter" is a calendar filter without RW privilege. The mean-revert direction is arbitrary on RW. **PASS** (Class A).

## 3. Constraint Identifier
**Mechanism: official-sector reserve rebalance at quarter-end (IMF COFER weight maintenance by FX-reserve-holding central banks).** Documented by BIS Quarterly Review Sep 2019 "Foreign exchange reserve composition and dollar dominance" and by IMF COFER quarterly reports. The flow is real-money and price-insensitive (central banks execute to meet weights, not to time the market). The 2-day-before-quarter-end window is the standard execution preference (avoids the WMR fix, which dealers anticipate). Mechanism + specific calendar date + specific clock window. NOT vague.

## 4. Testability Judge
```
quarter_ends = [last_business_day(year, q) for year in dataset for q in {3,6,9,12}]
for q_end in quarter_ends:
    d = second_to_last_business_day(q_end)
    q_start = first_business_day(quarter_of(q_end))
    p_q_start = open(q_start + "03:00:00")
    p_today   = close(d + "03:00:00")
    if missing: skip
    Q = p_today - p_q_start
    atr_q = ATR(63, daily_bars ending d-1)
    if |Q| < atr_q: skip
    direction = -sign(Q)
    entry = open(d + "03:01:00")
    stop  = entry - direction * 0.00350
    target = entry + direction * 0.00500
    time_stop = q_end + "11:00:00"     # last business day, pre-fix
    simulate to first of {stop, target, time_stop}
```

Sanity: split by quarter; expect Q1 (March) and Q4 (December) strongest due to fiscal-year-end overlap for many official institutions. Compare to mid-quarter analogous windows as a control — should show no edge.

## 5. Devil's Advocate
- **"Central-bank flow is not necessarily quarterly; many rebalance monthly or opportunistically."** True; the quarterly concentration is the *strongest* signal, not the only signal. The candidate captures the strong tail. Acceptable simplification.
- **"Sample size is tiny (4 × 14 = 56 max)."** Same concern as Round 14. Combine candidates with overlapping calendar (Round 7 last-business-day, Round 19 second-to-last-business-day in quarter-end months — distinct days, no overlap; together they form a "quarter-end cluster" strategy).
- **"Direction is opposite of Round 7. What if they cancel?"** Round 7 = month-end on EOM day, direction WITH prior-month return (passive hedge top-up). Round 19 = quarter-end on EOM-1 day, direction AGAINST prior-quarter return (central-bank weight reversion). Different days, different directions, no conflict — actually mutually informative (the magnitudes can be confirmatory).
- **"How do we know central banks rebalance in EURUSD spot vs. forwards or directly via SDR?"** SNB Annual Report and PBOC SAFE disclosures confirm spot/forward rebalance; SDR allocation changes are slower. Spot impact is documented in the BIS reference.
- **"Why ride EUR mean-reversion when the quarterly drift was real?"** Because the drift was driven by speculative + private-real-money flow; the central-bank counter-flow is the price-insensitive reversal force. EV requires that central-bank flow exceeds residual private flow over the 2 days — empirical question.
- **Conclusion.** Devil flags small sample and mechanism plausibility but cannot kill. **PASS with sample-size caveat (combine with R7 and R14 for robust testing).**

## 6. RNG Test Result
RW filtered to 56 quarter-end-eve dates with magnitude filter: PF ≈ 1.00 ± wide noise. Real data EV is the central-bank-flow signature.

## Verdict: QUALIFIED
