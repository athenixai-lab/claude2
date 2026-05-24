---
name: NORGES_NOK_CONVERSION
status: KILLED
round: 46
constraint: norges_bank_daily_oil_revenue_nok_conversion
expected_win_rate: 0.51
expected_rr: 1.1
---

# Candidate: NORGES_NOK_CONVERSION

## Generator
Norges Bank converts daily oil revenue USD to NOK on behalf of the Norwegian state (Petroleum Fund mechanism). Daily amount published monthly in advance. Hypothesis: this creates NOK-side flow with marginal EURUSD spillover.

## RNG Critic / Constraint Identifier
The directional effect on EURUSD is too small to overcome spread. NOK-leg flow doesn't materially move EURUSD because:
1. NOK is a thin currency relative to EUR/USD; cross-arbitrage is minimal.
2. The flow is announced in advance and arbitraged out.
3. Even on real data, expected per-trade EV is probably <0.5 pips after spread.

## Decision
**KILLED** — too weak signal, cross-arbitrage already arbed.
