---
name: SHORT_SELLER_BORROW_RESET
status: QUALIFIED
round: 161
constraint: equity_short_seller_securities_lending_borrow_fee_reset
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: SHORT_SELLER_BORROW_RESET
Generator: Equity short-seller securities lending fees reset daily 16:00 EST per CFTC/SEC convention. When borrow costs spike on heavily-shorted US stocks, equity volatility increases; spillover to EUR via risk-on/off.
- Trigger: 16:00 EST.
- Entry: small fade of 15:55-16:00 spike if range > 6 pips.
- Stop: 12, Target: 14, time-stop 16:10 EST.
RNG: zero pre-cost EV. **PASSES.** Calendar/clock-anchored. **QUALIFIED.**
