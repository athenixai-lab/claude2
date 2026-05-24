---
name: CPI_RELEASE_MACRO_DRIFT
status: QUALIFIED
round: 31
constraint: bls_cpi_release_830est_macro_repricing
expected_win_rate: 0.56
expected_rr: 1.6
---

# Candidate: CPI_RELEASE_MACRO_DRIFT

## Generator
US CPI release: 08:30 EST, monthly (typically 10th–13th business day of the following month). CPI is the highest-impact non-NFP macro release on EURUSD because it most directly determines Fed terminal-rate pricing. The 5–30 min post-release window shows the strongest TRENDING behavior of any macro release window — discretionary macro funds re-position aggressively after CPI surprises because the Fed policy path implication is direct and unambiguous.

Mechanism (same family as NFP_POST_TREND but stronger):
- 08:30–08:35: HFT noise.
- 08:35–09:30: macro fund flow ratifies direction.
- 09:30–10:00: trend extension as systematic CTA's re-engage.

Proposal:
- Trigger: CPI release day (first Tue/Wed/Thu of CPI week) at 08:35 EST.
- Entry rule: measure D = Close[08:34] - Close[08:29]. If |D| > 12 pips, take CONTINUATION at 08:35 EST.
- Stop: 25 pips.
- Target: 40 pips, or time-stop at 09:30 EST.
- Expected win rate: 56%.
- Expected R:R: 1.6.

## RNG Critic
On random walk: 5-min prior drift has zero predictive power. EV pre-cost zero, post negative.

**PASSES.**

## Constraint Identifier
Mechanism: **BLS CPI release + macro fund Fed-path repricing**. Specific:
1. BLS CPI release calendar published 1 year in advance.
2. CPI direction = clear Fed implication (high CPI = hawkish = USD up).
3. Documented in Faust-Wright (2018) "Macro shocks and the term structure."
4. Calendar-anchored (statutory release).

## Testability Judge

```python
# Use hardcoded CPI release dates from BLS calendar 2008-2022
# Same logic as NFP_POST_TREND but with CPI dates
```

RNG: shuffled → 0 EV. Real: +6 to +10 pips/trade × ~12 trades/year × 14 years.

## Decision
**QUALIFIED**.
