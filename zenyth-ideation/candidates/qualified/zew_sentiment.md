---
name: ZEW_SENTIMENT
status: QUALIFIED
round: 78
constraint: zew_germany_economic_sentiment_tuesday_mid_month
expected_win_rate: 0.52
expected_rr: 1.3
---

# Candidate: ZEW_SENTIMENT

## Generator
ZEW Economic Sentiment Indicator for Germany releases mid-month Tuesday at 11:00 CET (05:00 EST in dataset). Survey of financial analysts; leading indicator for EU equity/bond markets. Smaller effect than Ifo but earlier in the cycle.

Proposal:
- Trigger: ZEW release Tuesday at 05:00 EST.
- Entry rule: first 5-min CONTINUATION if |M| > 5 pips.
- Stop: 12 pips.
- Target: 15 pips, time-stop at 06:00 EST.
- Expected win rate: 52%.
- Expected R:R: 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ZEW monthly survey release**. Calendar-anchored.

## Decision
**QUALIFIED**.
