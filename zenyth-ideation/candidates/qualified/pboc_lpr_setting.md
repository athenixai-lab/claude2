---
name: PBOC_LPR_SETTING
status: QUALIFIED
round: 93
constraint: pboc_loan_prime_rate_20th_of_month
expected_win_rate: 0.51
expected_rr: 1.3
---

# Candidate: PBOC_LPR_SETTING

## Generator
PBOC sets the Loan Prime Rate (LPR) on the 20th of each month at 09:30 CST (20:30 EST prior day). Effective Aug 2019. Direct CNY impact; minor EURUSD spillover via dollar index and Asian risk sentiment.
- Trigger: PBOC LPR day at 20:30 EST prior day.
- Entry: first 5-min CONTINUATION if |M| > 4 pips.
- Stop: 10, Target: 13, time-stop 21:30 EST.
- WR 51%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**PBOC monthly LPR fixing**. Calendar-anchored.

## Decision
**QUALIFIED** — weak, post-2019 only.
