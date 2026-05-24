---
name: DIVIDEND_EX_DATE_WINDOW
status: QUALIFIED
round: 97
constraint: sp500_quarterly_dividend_ex_date_window
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: DIVIDEND_EX_DATE_WINDOW

## Generator
S&P 500 dividend payments concentrate in late February/May/August/November (quarterly cycle). Foreign holders of US equities receive USD dividends and frequently convert to home currency. This creates a small but consistent USD-selling flow in the ex-date + 5-business-day window.
- Trigger: business days within first week of quarterly dividend month (Feb/May/Aug/Nov first week) at 10:00 EST.
- Entry: LONG EURUSD (USD-selling pressure from dividend repatriation).
- Stop: 25, Target: 32, time-stop 16:00 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**S&P 500 quarterly dividend cycle + foreign-holder repatriation**. Specific:
1. S&P Dow Jones publishes dividend calendar quarterly.
2. Foreign holders (per BEA TIC data) of ~25% of US equities; dividend repat to EUR/JPY/GBP.
3. Calendar-anchored.

## Decision
**QUALIFIED**.
