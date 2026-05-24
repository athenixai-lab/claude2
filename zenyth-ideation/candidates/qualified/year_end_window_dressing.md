---
name: YEAR_END_WINDOW_DRESSING
status: QUALIFIED
round: 158
constraint: year_end_mutual_fund_window_dressing_last_5_days
expected_win_rate: 0.56
expected_rr: 1.4
---

# Candidate: YEAR_END_WINDOW_DRESSING

## Generator
US mutual funds engage in year-end window dressing in the final 5 business days of December — selling losers, buying winners to publish a more attractive annual NAV holding list. For EUR/USD specifically: foreign-asset funds that had positive returns on EUR exposure in the year tend to ADD EUR exposure into year-end NAV strike for cosmetic reasons.
- Trigger: each business day in final 5 of December at 09:00 EST.
- Entry: directional based on YTD EUR/USD return (LONG if YTD positive, SHORT if YTD negative).
- Stop: 35, Target: 45, time-stop 16:00 EST.
- WR 56%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Mutual fund year-end window dressing + cosmetic NAV positioning**. Calendar-anchored.

## Decision
**QUALIFIED** — distinct from YEAREND_REPO_SQUEEZE (which is funding-driven, not cosmetic).
