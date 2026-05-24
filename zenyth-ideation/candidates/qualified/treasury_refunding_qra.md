---
name: TREASURY_REFUNDING_QRA
status: QUALIFIED
round: 53
constraint: treasury_quarterly_refunding_announcement_wednesday
expected_win_rate: 0.57
expected_rr: 1.5
---

# Candidate: TREASURY_REFUNDING_QRA

## Generator
US Treasury publishes Quarterly Refunding Announcement (QRA) on the first Wednesday of February, May, August, November at 08:30 EST. The QRA details total Treasury issuance for the upcoming quarter — directly affecting USD funding markets, foreign-buyer demand, and dollar liquidity. Large surprise increases in issuance signal more USD-supply → USD weakens; reductions signal scarcity → USD strengthens.

Proposal:
- Trigger: QRA day at 08:30 EST.
- Entry rule: measure 5-min reaction M = Close[08:35] - Close[08:29]. If |M| > 12 pips, CONTINUE direction (the Treasury supply implication for USD is multi-day; first-5-min move shows correct direction).
- Stop: 30 pips.
- Target: 50 pips, or time-stop at 14:00 EST.
- Expected win rate: 57%.
- Expected R:R: 1.5.

## RNG Critic
EV pre-cost zero on RNG.

**PASSES.**

## Constraint Identifier
Mechanism: **US Treasury QRA + foreign buyer FX demand adjustment**. Specific:
1. Treasury Refunding Press Releases (TreasuryDirect, first-Wednesday-of-Feb/May/Aug/Nov).
2. Documented in NY Fed Liberty Street "Why is the Refunding Announcement Important?"
3. Calendar-anchored.

## Decision
**QUALIFIED**.
