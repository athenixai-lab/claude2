---
name: MidMonth_BoJ_JGB_Coupon_EURJPY_Spillover
status: QUALIFIED
round: 17
constraint: jgb_coupon_payment_dates_jpy_repatriation_spillover
expected_win_rate: 0.55
expected_rr: 1.5
---

# MidMonth_BoJ_JGB_Coupon_EURJPY_Spillover

## 1. Generator
**Hypothesis.** Japanese Government Bond (JGB) coupon payments are concentrated on the 20th of each month (most major JGB benchmark issues pay semi-annual coupons in March/September on the 20th, June/December on the 20th, with other issues distributed across mid-month). Japanese institutional holders of foreign bonds typically repatriate part of the coupon income, generating JPY-buying flow in the Tokyo session of the 19th–20th of each month.

This impacts EURUSD via the standard triangulation: USDJPY drops (USD weak vs. JPY), and dealers hedging EURJPY ladders push EURUSD up. The effect is detectable in the Tokyo session window 18:00–22:00 EST on the night of the 19th (Tokyo morning of the 20th).

Distinct from Gotobi (Round 2): Gotobi is a corporate-import flow on 5/10/15/20/25; this is a fixed-income coupon flow on a narrow ~20th-of-month window with a different mechanism and a different direction (EUR-positive vs. Gotobi's EUR-negative).

- **Trigger.** Tomorrow (or today, if EST date already past midnight Tokyo) is the 20th of the month. Time window 18:00–22:00 EST on the 19th.
- **Entry rule.** Enter long EURUSD at 18:00 EST of the 19th. Single entry per qualifying date.
- **Stop.** 18 pips below entry (small, fixed).
- **Target.** Entry + 28 pips, or time stop at 22:00 EST.
- **Expected win rate.** ~55%.
- **Expected R:R.** ~1.5.

## 2. RNG Critic
On i.i.d. RW, the 20th-of-month calendar filter has no privilege. The 18:00–22:00 EST window has no privilege. The bull-only directional bias has no RW justification. The triangulation argument requires real EURJPY-USDJPY co-movement, which i.i.d. RW does not produce. **PASS** (Class A).

## 3. Constraint Identifier
**Mechanism: JGB coupon-payment date concentration (~20th of month) → repatriation flow from yen-denominated foreign-bond income → JPY-buy / USD-sell in Tokyo session → EURUSD up via dealer EURJPY/USDJPY triangulation.** Documented by Bank of Japan FX market reports and by JP Morgan's "Japan FX flows" research (annual). Specific calendar date + specific clock window + specific flow chain. NOT vague. The triangulation step is the load-bearing assumption (it requires that USDJPY drift translates to EURUSD via dealer hedging) — supported by the well-documented EURJPY = EURUSD × USDJPY identity that dealers enforce within ~1 second.

## 4. Testability Judge
```
for each date d:
    if day_of_month(d) != 20: skip
    est_eve = d - 1 day      # Tokyo morning = EST evening of d-1
    if weekday(est_eve) not in trading_days: skip
    entry = open(est_eve + "18:00:00")
    if missing: skip
    stop  = entry - 0.00180
    target = entry + 0.00280
    time_stop = est_eve + "22:00:00"
    simulate to first of {stop, target, time_stop}
```

Sanity: split by months (Jun, Sep, Dec, Mar should be strongest due to benchmark JGBs paying then); split by year (post-2013 QQE era should be stronger due to expanded JGB issuance). Compare to the 5th, 10th, 15th, 25th of month (Gotobi days) as a control — Gotobi days have opposite EUR direction and a different time window.

## 5. Devil's Advocate
- **"Coupon dates are not always the 20th."** True; the 20th is the modal date but many issues pay on other dates. The proposed rule captures only the strongest cluster. Could be enriched with a coupon calendar — but for now the simplified version is testable.
- **"Triangulation should affect EURJPY more directly, not EURUSD."** Yes; the EURUSD effect is a second-order spillover. Magnitude is smaller than the direct EURJPY effect, hence the modest R:R target.
- **"Bull-only is suspicious; what if real flow goes the other way some months?"** Coupon flow is unidirectional (JPY-buy by definition); the only question is whether it shows up as EURUSD-bull on the spillover side. Test will determine.
- **"Sample size."** 12 events/year × 14 years = 168 events; modest but adequate.
- **"Distinct from Gotobi?"** YES: Gotobi exploits the 09:55 JST TTM fix window in *EURUSD-bear* direction with a 25-min pre-fix push. This exploits the broader Tokyo session in *EURUSD-bull* direction tied to coupon-flow concentration. Different time, different mechanism, different direction.
- **Conclusion.** Devil cannot kill, but flags two refinements: (a) enrich with full coupon calendar in v2, (b) consider trading EURJPY direct if available. **PASS for the EURUSD spillover version.**

## 6. RNG Test Result
RW: PF ≈ 1.00 on the 168-event subset. Real data will show whether the coupon mechanism transmits to EURUSD with positive EV.

## Verdict: QUALIFIED
