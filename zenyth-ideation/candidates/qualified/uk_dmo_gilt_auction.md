---
name: UK_DMO_GILT_AUCTION
status: QUALIFIED
round: 164
constraint: uk_dmo_gilt_auction_tuesday_wednesday_thursday
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: UK_DMO_GILT_AUCTION
Generator: UK Debt Management Office gilt auctions Tue/Wed/Thu mornings. GBP demand → EUR/GBP cross spillover to EUR/USD.
- Trigger: gilt auction day at 04:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 3 pips.
- Stop: 8, Target: 10, time-stop 05:00 EST.
RNG: zero pre-cost EV. **PASSES.** Calendar-anchored. **QUALIFIED.**
