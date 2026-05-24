---
name: FRENCH_OAT_AUCTION
status: QUALIFIED
round: 117
constraint: french_oat_auction_thursday_agence_france_tresor
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: FRENCH_OAT_AUCTION

## Generator
Agence France Trésor conducts OAT auctions ~first Thursday of each month at 10:55 CET (04:55 EST). Similar mechanism to German Bund — foreign demand creates EUR-side flow.
- Trigger: OAT auction Thursday at 04:55 EST.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 12, time-stop 05:30 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Agence France Trésor monthly OAT auction**. Calendar-anchored.

## Decision
**QUALIFIED**.
