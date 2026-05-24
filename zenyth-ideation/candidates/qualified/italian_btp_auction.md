---
name: ITALIAN_BTP_AUCTION
status: QUALIFIED
round: 118
constraint: italian_btp_auction_mid_month_dipartimento_tesoro
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: ITALIAN_BTP_AUCTION

## Generator
Italian Treasury (Dipartimento del Tesoro) conducts BTP auctions ~13th and 27th of month at 11:00 CET (05:00 EST). Italian-spread sensitive: poor demand creates EUR-side weakness via flight-to-Germany.
- Trigger: BTP auction day at 05:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12, Target: 15, time-stop 05:45 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Italian Treasury BTP twice-monthly auction**. Calendar-anchored.

## Decision
**QUALIFIED**.
