# ZENYTH Ideation Loop — Summary

**Total rounds run:** 7
**Qualified candidates:** 5 (target met)
**Killed candidates:** 2

## Qualified Candidates Ranked by Expected EV
EV = (win_rate × R:R) − (1 − win_rate), per unit of risk.

| Rank | Name | WR | R:R | EV / R | Constraint |
|------|------|----|----|--------|------------|
| 1 | MonthEnd_WMR_Rebalance_PreDrift | 0.59 | 1.5 | **+0.475** | monthend_index_hedge_rebalance_window |
| 2 | Tokyo_Gotobi_Fix_PreDrift | 0.55 | 1.6 | **+0.430** | tokyo_0855_gotobi_fix |
| 3 | Friday_NY_Close_PnL_Squaring | 0.56 | 1.5 | **+0.400** | friday_eod_dealer_book_closure |
| 4 | LDN_4PM_Fix_Drift_Reversion | 0.58 | 1.4 | **+0.392** | london_4pm_wmr_fixing_window |
| 5 | Options_1000NY_Cut_Pin_Magnet | 0.61 | 1.2 | **+0.342** | ny_1000_options_cut_expiry_pin |

## One-paragraph synopsis per candidate

### 1. MonthEnd_WMR_Rebalance_PreDrift  (EV +0.475)
Rides the dealer-inventory accumulation that precedes the 4pm London Fix on the **last business day** of each month, in the direction set by the *prior-month* EURUSD return (proxy for the equity-vs-FX divergence that drives passive-fund hedge rebalancing). Mechanism is documented in Melvin & Prins (2015) and Cenedese-Payne-Sarno-Valente (2016). Sample ~168 month-ends in 14 years. Distinct from Round 1: month-end only, direction is *with* the prior-month signal, exits *before* the fix window rather than after.

### 2. Tokyo_Gotobi_Fix_PreDrift  (EV +0.430)
Fades the EURUSD spillover of Japanese importer USD demand at the 09:55 JST TTM fix on **Gotobi** days (calendar days 5/10/15/20/25 + end-of-month). The EURUSD pressure comes from dealers hedging EURJPY cross-flow at the TTM cut, and dissipates immediately after the fix. Sample size is large (~70 Gotobi days per year × 14 years ≈ 980 events).

### 3. Friday_NY_Close_PnL_Squaring  (EV +0.400)
Fades the dominant weekly direction in the 90 minutes before NY Friday 17:00 EST, conditional on top-quintile weekly displacement. Mechanism: dealer spec-desks square winning books before the weekend gap forces position reduction. Sample: ~140 qualifying Fridays in 14 years (top-quintile filter applied).

### 4. LDN_4PM_Fix_Drift_Reversion  (EV +0.392)
Fades top-decile pre-fix displacement in the 35 minutes preceding the WMR 4pm London Fix (11:20–11:55 EST), exiting on the return to the 11:20 EST level. The simplest of the qualified set; the most-traded constraint in FX academic literature. Sample: ~350 qualifying days in 14 years.

### 5. Options_1000NY_Cut_Pin_Magnet  (EV +0.342)
Trades a 09:01 EST entry **toward** the nearest round 50-pip strike when current spot is 5–20 pips from that strike, exiting on the 10:00 NY options cut. Exploits dealer short-gamma delta-hedge pinning. Conservative EV; expected to be strongest on Fridays (weekly OPEX) and final Friday of month (monthly OPEX). Sample very large (potentially most trading days).

## Killed candidates
- **CME_Basis_Close_Reversion** (Round 3): mechanism unobservable in spot-only data; rule reduced to generic noise-fade.
- **PreECB_SpreadVacuum_Drift** (Round 6): liquidity-vacuum mechanism amplifies but does not direct; sample size (~112) too small to validate.

## Suggested backtest priority order
Priority is **not** strictly by EV — it weighs EV against (a) sample size, (b) implementation difficulty, (c) novelty vs. existing literature (which informs how crowded the trade may be).

1. **Tokyo_Gotobi_Fix_PreDrift** — high EV, largest sample, least crowded (cross-asset spillover rarely documented for EURUSD specifically). Best EV-per-event-count.
2. **MonthEnd_WMR_Rebalance_PreDrift** — highest EV but smallest sample (~168). Run second to confirm headline EV is not a small-sample artifact; check year-by-year stability and post-2008 sub-sample where passive AUM dominates.
3. **LDN_4PM_Fix_Drift_Reversion** — workhorse with the largest sample and the cleanest documented mechanism. Use as the reference benchmark; should backtest well, would be a red flag if it doesn't.
4. **Friday_NY_Close_PnL_Squaring** — moderate sample, simplest to implement (calendar + percentile filter). Check decade stability — dealer book-closure behavior shifted post-Volcker (2010) and again post-2015 MiFID-II.
5. **Options_1000NY_Cut_Pin_Magnet** — last because the proxy (round 50-pip strikes) is a known weak substitute for true OI; expect noisier results. Split the backtest by Friday-vs-weekday and by month-end-Friday to see if the pin signal is concentrated where OI is largest.

## Constraint-mechanism diversity (acceptance)
The five qualified candidates exploit **five distinct constraint families**: a London benchmark fix, a Tokyo benchmark fix, a weekly P&L deadline, an options-expiry cut, and a month-end rebalance window. No two candidates rely on the same mechanism or trade in the same calendar window. The portfolio is diversified across time-of-day, day-of-week, day-of-month, and underlying flow type.

DONE
