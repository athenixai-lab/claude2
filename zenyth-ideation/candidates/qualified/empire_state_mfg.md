---
name: EMPIRE_STATE_MFG
status: QUALIFIED
round: 81
constraint: empire_state_manufacturing_15th_830est
expected_win_rate: 0.51
expected_rr: 1.3
---

# Candidate: EMPIRE_STATE_MFG

## Generator
NY Fed Empire State Manufacturing Survey releases 15th of each month (or first business day after) at 08:30 EST. First major US regional manufacturing release of the month; sets tone for subsequent Philly Fed and ISM.

Proposal:
- Trigger: Empire State release day at 08:30 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 15 pips.
- Target: 20 pips, time-stop at 09:30 EST.
- Expected win rate: 51%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**NY Fed Empire State Survey**. Calendar-anchored.

## Decision
**QUALIFIED** — weak but real.
