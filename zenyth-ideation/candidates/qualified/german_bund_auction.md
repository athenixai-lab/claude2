---
name: GERMAN_BUND_AUCTION
status: QUALIFIED
round: 116
constraint: german_bund_auction_wednesday_bidding_deadline
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: GERMAN_BUND_AUCTION

## Generator
German Finance Agency conducts Bund auctions Wednesday 11:30 CET (05:30 EST). Foreign demand for German government bonds drives EUR demand (corresponding currency conversion). Auction results affect EUR/USD via Bund yield path.
- Trigger: Bund auction day at 05:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 06:30 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Bundesbank/German Finance Agency weekly Bund auction**. Calendar-anchored.

## Decision
**QUALIFIED**.
