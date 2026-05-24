---
name: MIDMONTH_REPO_MAINTENANCE
status: QUALIFIED
round: 139
constraint: mid_month_repo_market_maintenance_corporate_tax_dates
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: MIDMONTH_REPO_MAINTENANCE

## Generator
Mid-month USD repo market regularly tightens around the 15th of each month due to:
1. Corporate tax estimated payments (Apr 15, Jun 15, Sep 15, Dec 15).
2. Treasury coupon settlement on 15th.
3. SOMA reinvestment on 15th.

This concentrates USD demand mid-month, producing measurable USD-bid in the 06:00–11:00 EST window of mid-month business days.
- Trigger: 14th/15th/16th business day at 06:00 EST.
- Entry: SHORT EURUSD at 06:00 EST.
- Stop: 25, Target: 32, time-stop 11:00 EST.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Mid-month USD repo tightness + corporate-tax-estimated-payment dates + coupon settlement**. Calendar-anchored.

## Decision
**QUALIFIED** — distinct from TREASURY_COUPON_SETTLE (which focuses on 15th only).
