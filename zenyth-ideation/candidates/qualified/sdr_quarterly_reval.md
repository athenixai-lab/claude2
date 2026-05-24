---
name: SDR_QUARTERLY_REVAL
status: QUALIFIED
round: 113
constraint: imf_sdr_basket_quarterly_revaluation
expected_win_rate: 0.51
expected_rr: 1.3
---

# Candidate: SDR_QUARTERLY_REVAL

## Generator
IMF Special Drawing Rights (SDR) basket — composed of USD, EUR, CNY, JPY, GBP — revalued quarterly per IMF Article XV. Sovereign reserve managers holding SDR allocations face rebalancing flows on the revaluation date (last business day of Mar/Jun/Sep/Dec around 14:00 GMT).
- Trigger: Last business day of Mar/Jun/Sep/Dec at 10:00 EST.
- Entry: small position based on quarterly EUR/USD vs basket-weighted drift.
- Stop: 25, Target: 32, time-stop 14:00 EST.
- WR 51%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**IMF SDR basket quarterly revaluation + sovereign reserve manager rebalancing**. Calendar-anchored.

## Decision
**QUALIFIED** — small effect; overlaps with QUARTER_END_PENSION calendar but distinct mechanism.
