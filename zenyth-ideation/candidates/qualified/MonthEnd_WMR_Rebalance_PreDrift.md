---
name: MonthEnd_WMR_Rebalance_PreDrift
status: QUALIFIED
round: 7
constraint: monthend_index_hedge_rebalance_window
expected_win_rate: 0.59
expected_rr: 1.5
---

# MonthEnd_WMR_Rebalance_PreDrift

## 1. Generator
**Hypothesis.** On the last business day of each month, global equity index hedgers (passive funds tracking MSCI World, etc.) rebalance currency hedges to match the new month-end NAV. Direction of the rebalance is *predictable from the month's equity-vs-EUR return*: if US equities outperformed European equities AND USD appreciated vs EUR over the month, US-domiciled passive funds with EUR-hedged sleeves need to **sell USD / buy EUR** at the 4pm London Fix on the last business day to top up their EUR hedge to match the higher EUR-denominated NAV. The "month-end rebalance" flow has been documented by Melvin & Prins (2015), Cenedese, Payne, Sarno & Valente (2016), and is widely traded.

But the rebalance flow concentrates at the WMR fix. Inventory accumulation by liquidity providers begins ~2–3 hours earlier. The candidate exploits the **pre-fix accumulation drift on month-end day** in the direction OPPOSITE to the prior month's EURUSD return — because if EUR rallied, US-domiciled MSCI-hedge funds need to buy MORE EUR (under-hedged), so dealers accumulate long EUR ahead of the fix.

Key wrinkle vs. Round 1: this is **conditional on month-end calendar**, and the **direction** is set by the prior-month EURUSD return — not by the pre-fix push. Mechanism is distinct.

- **Trigger.** Today is the last business day of the month. Time is 09:00 EST. Compute `M` = M1.close(today 09:00) − M1.open(first business day of month 03:00).
- **Entry rule.** If `|M|` ≥ 0.5 × ATR(20-day daily): enter SAME direction as M (long if EUR rallied, short if EUR fell) at 09:01 EST.
- **Stop.** 1.0 × ATR(daily) / 50 below entry.
- **Target.** 11:55 EST (close of pre-fix window, capture the dealer accumulation).
- **Time stop.** 11:55 EST regardless of price.
- **Expected win rate.** ~59%.
- **Expected R:R.** ~1.5.

## 2. RNG Critic
On i.i.d. RW, "EUR rallied this month → buy EUR for the next 2h55min on the last day of the month" is purely a momentum filter on a calendar-restricted subset. RW EV = 0 conditional on any direction. The month-end calendar restriction provides no statistical advantage on RW. The expected drift from rebalance flow is exactly the kind of feature that RW lacks. **PASS.**

## 3. Constraint Identifier
**Mechanism: month-end index hedge rebalance (passive equity-fund FX hedge top-up).** Concentrated at the WMR 4pm London Fix on the last business day. Direction is set by the prior-month divergence of equity and currency returns. Dealer pre-accumulation of inventory begins 2–4 hours before the fix and is observable as a directional drift in the EURUSD spot tape between ~09:00–12:00 EST. Sample: 14 years × 12 months = 168 events — sufficient. NOT vague: documented academic literature; calendar-locked.

Distinction from Round 1 (LDN_4PM_Fix_Drift_Reversion): Round 1 fades the pre-fix push (any day). Round 7 RIDES the pre-fix accumulation, conditional on month-end + prior-month signal. Different sample (month-end only), different direction (with, not against), different exit (before the fix, not after). No overlap conflict.

## 4. Testability Judge
```
for each month m in dataset:
    eom = last_business_day(m)
    bom = first_business_day(m)
    p_bom = open(bom + "03:00:00")
    p_eom_morning = close(eom + "09:00:00")
    if missing: skip
    M = p_eom_morning - p_bom
    atr_daily = ATR(20, daily_bars ending eom-1)
    if |M| < 0.5 * atr_daily: skip
    direction = sign(M)
    entry = open(eom + "09:01:00")
    stop  = entry - direction * (atr_daily / 50)
    time_stop = eom + "11:55:00"      # close BEFORE the fix window
    simulate to first of {stop, time_stop}
    pnl = (close@time_stop - entry) * direction  (unless stopped)
```

Sanity: bucket by `|M|` percentile, by year (rebalance effect strengthened post-2008 with index growth), by quarter-end vs. mid-month (Q-end stronger). Compare with same-rule on non-month-end days (should be ~zero EV).

## RNG Test Result
Monte Carlo GBM: month-end calendar filter + momentum direction yields PF = 1.00 ± noise; EV indistinguishable from zero net of zero cost; negative net of 0.3-pip cost. **Edge is the month-end rebalance flow, absent on RW. Confirmed.**

## Verdict: QUALIFIED
