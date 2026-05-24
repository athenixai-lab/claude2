---
name: POWELL_HUMPHREY_HAWKINS
status: QUALIFIED
round: 59
constraint: fed_chair_semiannual_congressional_testimony
expected_win_rate: 0.55
expected_rr: 1.5
---

# Candidate: POWELL_HUMPHREY_HAWKINS

## Generator
Fed Chair semi-annual monetary policy testimony to Congress (Senate Banking Committee and House Financial Services Committee), known by tradition as "Humphrey-Hawkins" — though the legal mandate (HH Act 1978) was rolled into Fed Reform Act 2000. Schedule: late February & mid-July annually, 10:00 EST. The first day of testimony (Senate) is more market-moving than the second.

The first 30 min of testimony (10:00–10:30 EST) reveals tone shift; market repositions for the next 1-2 hours.

Proposal:
- Trigger: HH testimony day at 10:00 EST.
- Entry rule: measure 30-min reaction R = Close[10:30] - Close[10:00]. If |R| > 15 pips, CONTINUE direction at 10:31 EST.
- Stop: 30 pips.
- Target: 45 pips, or time-stop at 12:30 EST.
- Expected win rate: 55%.
- Expected R:R: 1.5.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed Reform Act 2000 (formerly HH 1978) + Fed Chair semi-annual testimony**. Specific:
1. Statutory requirement: Fed Chair must testify before Congress on monetary policy.
2. Schedule: Senate Banking Committee + House Financial Services.
3. Calendar-anchored (~Feb & ~Jul).

## Decision
**QUALIFIED**.
