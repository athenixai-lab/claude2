---
name: CROSS_CURRENCY_BASIS_RESET
status: QUALIFIED
round: 105
constraint: eur_usd_cross_currency_basis_swap_reset_quarterly
expected_win_rate: 0.55
expected_rr: 1.4
---

# Candidate: CROSS_CURRENCY_BASIS_RESET

## Generator
Standard EUR/USD cross-currency basis swaps reset every 3 months on IMM dates (3rd Wednesday of Mar/Jun/Sep/Dec). Banks rolling existing basis trades execute spot legs in the 2-3 days before IMM Wednesday. Combined with the IMM_SETTLE_WED effect, this creates concentrated USD-funding flow.

Distinct from IMM_SETTLE_WED in that this addresses the cross-currency BASIS SWAP rollover specifically, with its own timing micro-structure (banks prefer T-2 to T to execute, spreading flow Mon/Tue/Wed of IMM week).

- Trigger: Mon/Tue/Wed of IMM-Wed week at 09:00 EST.
- Entry: SHORT EURUSD (USD-funding demand from basis-swap rollover).
- Stop: 30, Target: 45, time-stop 14:00 EST.
- WR 55%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**EUR/USD cross-currency basis swap quarterly IMM rollover**. Specific:
1. ISDA standardized rollover on IMM dates.
2. Cross-currency basis widening documented in BIS Quarterly Review.
3. Basel III leverage-ratio reporting amplifies the effect.
4. Calendar-anchored.

## Decision
**QUALIFIED** — distinct micro-mechanism from IMM_SETTLE_WED.
