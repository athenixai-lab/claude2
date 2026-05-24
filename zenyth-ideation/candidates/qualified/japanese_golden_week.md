---
name: JAPANESE_GOLDEN_WEEK
status: QUALIFIED
round: 63
constraint: japanese_golden_week_boj_market_closure
expected_win_rate: 0.58
expected_rr: 1.4
---

# Candidate: JAPANESE_GOLDEN_WEEK

## Generator
Japanese Golden Week (April 29–May 5 with several public holidays). BoJ closed; Tokyo banks closed; corporate FX desks closed. The absence of Japanese institutional flow is similar in nature to Lunar New Year (Round 29) but with different timing and milder magnitude. Spillover to EURUSD via missing USD/JPY-side flow.

Proposal:
- Trigger: each business day in Golden Week (Apr 29 – May 5 inclusive, EU/US business days only) at 06:00 EST.
- Entry rule: LONG EURUSD at 06:00 EST.
- Stop: 25 pips.
- Target: 35 pips, or time-stop at 14:00 EST.
- Expected win rate: 58%.
- Expected R:R: 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Japanese Golden Week + BoJ/MOF closure**. Specific:
1. Japanese national holiday law: Showa Day (Apr 29), Constitution Day (May 3), Greenery Day (May 4), Children's Day (May 5).
2. JST trading desks effectively closed.
3. Calendar-anchored.

## Decision
**QUALIFIED**.
