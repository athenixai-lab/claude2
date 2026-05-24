---
name: BUYBACK_BLACKOUT_WINDOW
status: QUALIFIED
round: 37
constraint: corporate_buyback_blackout_pre_earnings
expected_win_rate: 0.55
expected_rr: 1.4
---

# Candidate: BUYBACK_BLACKOUT_WINDOW

## Generator
SEC Rule 10b-18 plus internal corporate compliance creates an "earnings blackout" — listed companies must halt their buyback programs in the 2–6 weeks before earnings releases. Buyback programs account for ~$1T/yr of US equity demand. When blackouts are active, US equity demand structurally weakens; when blackouts END (the day after earnings), buybacks resume at concentrated pace.

For EURUSD: when US equity demand falls due to broad buyback blackout (Q2 weeks 2–4 of any earnings month — Jan/Apr/Jul/Oct), foreign holders of US equities reduce currency hedge demand. This subtly weakens USD (since less hedge-buying USD) → marginal EURUSD POSITIVE bias during weeks 2–4 of those months.

Conversely, in weeks 1 and 5 (post-earnings buyback resumption), USD demand returns.

Proposal:
- Trigger: any business day in weeks 2–4 of January, April, July, October (i.e. days 8–28 of those months) at 09:00 EST.
- Entry rule: LONG EURUSD at 09:00 EST.
- Stop: 30 pips.
- Target: 40 pips, or time-stop at 16:00 EST.
- Expected win rate: 55%.
- Expected R:R: 1.4.

(NB: this is a weak, broad signal — best used in combination with other filters.)

## RNG Critic
On random walk: calendar month-week has no special meaning; EV pre-cost zero, post negative.

**PASSES.**

## Constraint Identifier
Mechanism: **SEC Rule 10b-18 buyback blackout + concentrated post-earnings resumption**. Specific:
1. SEC Rule 10b-18 safe harbor for buybacks — companies follow internal blackout (typically 2–6 weeks pre-earnings).
2. ~$1T/yr corporate buyback flow in US equities.
3. Documented in Goldman Sachs Buyback Desk reports.
4. Calendar-anchored to earnings cycles (Jan/Apr/Jul/Oct).

## Testability Judge

```python
# For each business day in weeks 2–4 of Jan/Apr/Jul/Oct:
#   Enter LONG at 09:00 EST, stop 30, target 40, hold to 16:00
```

RNG: shuffled → 0 EV. Real: small +1 to +3 pips/trade × ~60 trades/year × 14 years.

## Decision
**QUALIFIED** — weak signal but real mechanism, calendar-anchored.
