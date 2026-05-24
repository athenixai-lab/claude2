---
name: PRE_LUNAR_DRIFT
status: QUALIFIED
round: 151
constraint: pre_lunar_new_year_chinese_corporate_positioning
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: PRE_LUNAR_DRIFT

## Generator
In the 5 business days BEFORE Lunar New Year, Chinese corporates accelerate FX conversions to close positions before week-long closure. Net flow tends to be CNY-buy / USD-sell, but for EUR/USD the secondary effect through Asian risk-on positioning is small EUR-positive.
- Trigger: 5 business days before Lunar New Year at 06:00 EST.
- Entry: LONG EURUSD.
- Stop: 25, Target: 32, time-stop 14:00 EST.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Pre-Lunar-New-Year Chinese corporate FX squaring**. Calendar-anchored.

## Decision
**QUALIFIED**.
