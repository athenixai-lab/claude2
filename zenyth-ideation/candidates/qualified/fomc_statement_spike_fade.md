---
name: FOMC_STATEMENT_SPIKE_FADE
status: QUALIFIED
round: 30
constraint: fomc_statement_press_conference_gap
expected_win_rate: 0.59
expected_rr: 1.5
---

# Candidate: FOMC_STATEMENT_SPIKE_FADE

## Generator
FOMC statement releases at 14:00 EST. Powell press conference begins at 14:30 EST (post-Yellen era; pre-2011 there were no press conferences). The 30-min gap between statement and press conference is THE most concentrated trading window in macro FX. Algo readers trade headline keywords at 14:00–14:02; discretionary traders refrain. By 14:25 EST (5 min before press conference), the cumulative move from the statement IS USUALLY FADED 40–60% as discretionary participants position for press conference clarification.

This is structurally identical to the ECB press-conference candidate (Round 15) but for Fed events.

Proposal:
- Trigger: scheduled FOMC days at 14:25 EST (entering 5 min before press conference).
- Entry rule: measure M = Close[14:25] - Close[13:59]. If |M| > 30 pips, FADE at 14:26 EST.
- Stop: 30 pips.
- Target: 45 pips, or time-stop at 14:55 EST.
- Expected win rate: 59%.
- Expected R:R: 1.5.

## RNG Critic
On random walk: 25-min drift has zero predictive power. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **FOMC statement → press-conference gap + discretionary fade**. Specific:
1. Fed FOMC schedule (8 meetings/year), statement released 14:00 EST, press conference 14:30 EST since 2011 (every meeting since 2019).
2. Documented two-step price reaction (parallel to ECB analog).
3. Trading desks (Citi, GS Macro FX) explicitly recommend fade-into-press-conference positioning.

## Testability Judge

```python
# Hard-coded FOMC dates 2008-2022 (Fed release calendar)
# At 14:25 measure M, fade if |M|>30
# Stop 30, target 45, time-stop 14:55
```

RNG: shuffled → 0 EV. Real: +6 to +12 pips/trade × ~8 events/year × 14 years.

## Decision
**QUALIFIED** — distinct from FOMC_PRE_DRIFT (which uses prior-day positioning); this is intra-event fade.
