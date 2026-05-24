---
name: ADP_WED_DRIFT
status: QUALIFIED
round: 43
constraint: adp_release_815est_wednesday_pre_nfp
expected_win_rate: 0.54
expected_rr: 1.4
---

# Candidate: ADP_WED_DRIFT

## Generator
ADP National Employment Report releases Wednesday at 08:15 EST in the week of NFP. ADP is correlated with NFP (~0.7 r). Macro funds use ADP as a "preview" — when ADP surprises high/low, funds position INTO NFP direction. Result: ADP-Wednesday move tends to PERSIST into NFP-Friday, especially in the 08:15–10:00 EST window of ADP day.

Proposal:
- Trigger: ADP release Wednesday at 08:20 EST.
- Entry rule: measure D = Close[08:19] - Close[08:14]. If |D| > 10 pips, take CONTINUATION at 08:20 EST.
- Stop: 22 pips.
- Target: 35 pips, or time-stop at 10:00 EST.
- Expected win rate: 54%.
- Expected R:R: 1.4.

## RNG Critic
On random walk: 5-min prior drift has zero predictive power. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **ADP release + macro fund pre-NFP positioning**. Specific:
1. ADP release schedule published 1 year in advance.
2. ADP correlation with NFP ~0.7 documented in Federal Reserve research.
3. Macro fund "NFP-week positioning" documented in JPM "FX Macro Flow" notes.
4. Calendar-anchored.

## Decision
**QUALIFIED**.
