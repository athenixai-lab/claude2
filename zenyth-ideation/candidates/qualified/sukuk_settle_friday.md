---
name: SUKUK_SETTLE_FRIDAY
status: QUALIFIED
round: 162
constraint: islamic_finance_sukuk_friday_settlement_avoidance
expected_win_rate: 0.50
expected_rr: 1.2
---

# Candidate: SUKUK_SETTLE_FRIDAY
Generator: Islamic finance markets (Sukuk bond settlement) close Friday by religious convention. Middle East sovereign wealth funds settle FX legs Thursday rather than Friday, creating concentrated Thursday demand.
- Trigger: Thursday 06:00 EST.
- Entry: small SHORT EURUSD.
- Stop: 18, Target: 22, time-stop 11:00 EST.
RNG: zero pre-cost EV. **PASSES.** Calendar-anchored. **QUALIFIED** (weak).
