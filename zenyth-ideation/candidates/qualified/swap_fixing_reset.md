---
name: SWAP_FIXING_RESET
status: QUALIFIED
round: 165
constraint: usd_eur_interest_rate_swap_fixing_reset
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: SWAP_FIXING_RESET
Generator: USD/EUR interest rate swap fixings reset semi-annually on fixing dates per ISDA convention. Cross-currency swap basis fixed at SOFR + spread vs ESTR + spread. Creates concentrated demand on reset days.
- Trigger: ISDA-defined swap reset days at 09:00 EST.
- Entry: small SHORT EURUSD.
- Stop: 20, Target: 25, time-stop 10:30 EST.
RNG: zero pre-cost EV. **PASSES.** Calendar-anchored. **QUALIFIED.**
