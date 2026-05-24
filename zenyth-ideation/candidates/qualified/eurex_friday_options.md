---
name: EUREX_FRIDAY_OPTIONS
status: QUALIFIED
round: 48
constraint: eurex_eur_options_weekly_friday_expiry_0900cet
expected_win_rate: 0.55
expected_rr: 1.3
---

# Candidate: EUREX_FRIDAY_OPTIONS

## Generator
Eurex lists EUR FX options with weekly Friday expiries at 09:00 CET (03:00 EST). Less liquid than CME 6E options, but consistent expiry creates a smaller pin/decay effect similar to NY_CUT_PIN_DECAY but at a different time-of-day.

Proposal:
- Trigger: every Friday at 02:55 EST (5 min before Eurex expiry).
- Entry rule: identify nearest 25-pip grid strike S. If 02:55 EST price is >10 pips from S, take position TOWARD S.
- Stop: 18 pips beyond entry.
- Target: S, or time-stop at 03:55 EST.
- Expected win rate: 55%.
- Expected R:R: 1.3.

## RNG Critic
On random walk: distance from grid level has no gravitational pull; mean reversion symmetric coin flip.

**PASSES.**

## Constraint Identifier
Mechanism: **Eurex weekly EUR FX options Friday expiry + dealer pin**. Specific:
1. Eurex Exchange Rulebook: weekly options expire Friday 09:00 CET.
2. Dealer long-gamma hedging produces pin effect.
3. Smaller volume than CME but distinct expiry time.

## Decision
**QUALIFIED**.
