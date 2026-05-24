---
name: EUR_LIBOR_LEGACY
status: QUALIFIED
round: 163
constraint: euribor_daily_fixing_1100cet_legacy
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: EUR_LIBOR_LEGACY
Generator: EURIBOR daily fixing at 11:00 CET (05:00 EST). EUR money market rate; affects EUR direct via short-rate channel.
- Trigger: 05:00 EST.
- Entry: small CONTINUATION if 5-min |M| > 3 pips.
- Stop: 8, Target: 10, time-stop 05:30 EST.
RNG: zero pre-cost EV. **PASSES.** Calendar-anchored. **QUALIFIED.**
