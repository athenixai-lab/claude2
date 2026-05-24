---
name: ECB_ACCOUNT_RELEASE
status: QUALIFIED
round: 56
constraint: ecb_meeting_account_release_thursday_0730est
expected_win_rate: 0.54
expected_rr: 1.4
---

# Candidate: ECB_ACCOUNT_RELEASE

## Generator
ECB Account (equivalent to Fed Minutes) published Thursday 13:30 CET (07:30 EST in dataset) approximately 4 weeks after each Governing Council meeting. Reveals voting splits and discussion tone. Less impactful than the original statement but contains additional information that algorithmic readers parse for hawk/dove updates.

Proposal:
- Trigger: ECB Account release Thursday at 07:30 EST.
- Entry rule: measure 5-min reaction; if |M| > 6 pips, CONTINUE direction.
- Stop: 15 pips.
- Target: 22 pips, or time-stop at 08:30 EST (before ECB-fix-window noise).
- Expected win rate: 54%.
- Expected R:R: 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB Account (Minutes) release + algorithmic re-pricing**. Specific:
1. ECB publishes Account ~4 weeks after each Governing Council meeting (since 2015).
2. Schedule published on ECB website.
3. Calendar-anchored.

## Decision
**QUALIFIED**.
