---
name: PMI_FLASH_ESTIMATE
status: QUALIFIED
round: 137
constraint: sp_global_pmi_flash_estimate_24th_of_month
expected_win_rate: 0.53
expected_rr: 1.4
---

# Candidate: PMI_FLASH_ESTIMATE

## Generator
S&P Global Flash PMI estimates for US, Eurozone, UK, Japan release ~24th of each month. Eurozone Flash Composite releases 09:00 CET (03:00 EST). US releases 09:45 EST. Important leading indicators preceding final PMI release.
- Trigger: PMI Flash release time.
- Entry: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 15, Target: 20, time-stop 30 min later.
- WR 53%, RR 1.4.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**S&P Global Flash PMI monthly releases**. Calendar-anchored.

## Decision
**QUALIFIED**.
