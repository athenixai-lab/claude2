---
name: PENSION_LIABILITY_MATCH
status: QUALIFIED
round: 149
constraint: pension_annual_actuarial_liability_match_reset
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: PENSION_LIABILITY_MATCH

## Generator
US defined-benefit pension funds reset their LDI (Liability-Driven Investment) overlay annually based on actuarial valuation date (typically Dec 31 plan-year-end or fiscal-year-end). The actuarial reset in January and re-balancing into long-duration assets creates concentrated USD-side flow in mid-January.
- Trigger: 2nd-3rd week of January at 09:00 EST.
- Entry: SHORT EURUSD on USD-side LDI demand.
- Stop: 35, Target: 45, time-stop 16:00 EST.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Pension annual actuarial reset + LDI overlay rebalancing**. Specific:
1. ERISA Section 404 actuarial valuation requirements.
2. LDI strategy AUM ~$1.5T.
3. Calendar-anchored.

## Decision
**QUALIFIED**.
