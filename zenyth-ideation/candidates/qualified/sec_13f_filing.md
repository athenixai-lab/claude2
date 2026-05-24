---
name: SEC_13F_FILING
status: QUALIFIED
round: 134
constraint: sec_form_13f_quarterly_45day_deadline
expected_win_rate: 0.51
expected_rr: 1.2
---

# Candidate: SEC_13F_FILING

## Generator
Institutional investment managers ($100M+ AUM) must file SEC Form 13F within 45 days of quarter-end disclosing US equity holdings. Filings concentrate in days surrounding the 45-day deadline (Feb 14, May 15, Aug 14, Nov 14). Foreign-fund holdings disclosures often trigger small EUR positioning effects.
- Trigger: 13F deadline at 16:00 EST.
- Entry: small directional based on accumulating prior 5-day drift.
- Stop: 20, Target: 24, time-stop next day 09:00 EST.
- WR 51%, RR 1.2.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**SEC Form 13F quarterly disclosure deadline**. Calendar-anchored.

## Decision
**QUALIFIED** — weak but real.
