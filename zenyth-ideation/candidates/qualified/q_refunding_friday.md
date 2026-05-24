---
name: Q_REFUNDING_FRIDAY
status: QUALIFIED
round: 129
constraint: post_treasury_refunding_friday_drift_after_qra_wednesday
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: Q_REFUNDING_FRIDAY

## Generator
The Friday after the Treasury Refunding Announcement (Wednesday) — markets digest the QRA over Wed-Thu, and Friday positioning often reflects the consensus interpretation. Specifically, foreign indirect bidders (per TIC data) finalize their FX hedging for incoming auction settlements over Wed-Fri.
- Trigger: Friday after QRA Wednesday at 09:00 EST.
- Entry: same direction as QRA-day initial reaction (compound the Wednesday signal).
- Stop: 30, Target: 42, time-stop 15:00 EST.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Treasury QRA + Friday foreign indirect bidder hedge completion**. Calendar-anchored.

## Decision
**QUALIFIED** — compound strategy.
