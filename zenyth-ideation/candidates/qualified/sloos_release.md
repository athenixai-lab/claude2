---
name: SLOOS_RELEASE
status: QUALIFIED
round: 111
constraint: senior_loan_officer_opinion_survey_quarterly_monday
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: SLOOS_RELEASE

## Generator
Federal Reserve Senior Loan Officer Opinion Survey (SLOOS) — quarterly release Monday afternoon (14:00 EST) BEFORE each FOMC meeting. Tracks credit-tightening conditions; closely watched by FOMC participants. Strong leading indicator for Fed reaction function.
- Trigger: SLOOS Monday at 14:00 EST.
- Entry: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 15, Target: 19, time-stop 15:00 EST.
- WR 53%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Fed quarterly SLOOS publication**. Calendar-anchored.

## Decision
**QUALIFIED**.
