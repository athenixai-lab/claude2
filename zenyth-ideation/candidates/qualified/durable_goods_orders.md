---
name: DURABLE_GOODS_ORDERS
status: QUALIFIED
round: 87
constraint: us_durable_goods_orders_830est_monthly
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: DURABLE_GOODS_ORDERS

## Generator
US Census Durable Goods Orders releases ~25th of month at 08:30 EST. Capex/business-investment leading signal.
- Trigger: release day 08:30 EST.
- Entry: first 5-min CONTINUATION if |M| > 6 pips.
- Stop: 14, Target: 18, time-stop 09:30 EST.
- WR 52%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**US Census Durable Goods Orders monthly**. Calendar-anchored.

## Decision
**QUALIFIED**.
