---
name: TIPS_AUCTION
status: QUALIFIED
round: 142
constraint: us_treasury_tips_inflation_protected_auction
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: TIPS_AUCTION

## Generator
US Treasury TIPS (Treasury Inflation-Protected Securities) auctions: 5-year (October, December, April), 10-year (January, March, May, July, September, November), 30-year (February, August). Foreign demand for TIPS — particularly during low-yield environments — has historically been ~20-25% indirect bid.
- Trigger: TIPS auction day at 13:05 EST.
- Entry: small SHORT EURUSD based on USD demand.
- Stop: 20, Target: 24, time-stop 14:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**US Treasury TIPS auction calendar**. Calendar-anchored.

## Decision
**QUALIFIED**.
