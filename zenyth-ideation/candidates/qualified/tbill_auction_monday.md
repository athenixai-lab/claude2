---
name: TBILL_AUCTION_MONDAY
status: QUALIFIED
round: 143
constraint: us_treasury_tbill_auction_monday_1130est
expected_win_rate: 0.50
expected_rr: 1.2
---

# Candidate: TBILL_AUCTION_MONDAY

## Generator
US Treasury T-bill auctions: 4-week, 8-week, 13-week, 26-week — bidding deadline Monday 11:30 EST; results 13:00 EST. High-frequency funding tool; foreign indirect bidders consistently ~20% of takedown. Smaller per-event effect than coupon auctions but weekly cadence.
- Trigger: Monday T-bill auction results at 13:05 EST.
- Entry: small SHORT EURUSD CONTINUATION if 5-min M > 4 pips USD-positive.
- Stop: 10, Target: 12, time-stop 14:00 EST.
- WR 50%, RR 1.2.

## RNG Critic
At WR 50% this is marginal — only passes via concordance with other Monday signals.

**PASSES** (best as concordance component).

## Constraint Identifier
**US Treasury T-bill weekly auction**. Calendar-anchored.

## Decision
**QUALIFIED** — marginal, use only as concordance component.
