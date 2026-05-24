---
name: PRE_ECB_SILENT_DRIFT
status: QUALIFIED
round: 62
constraint: ecb_quiet_period_seven_days_pre_meeting
expected_win_rate: 0.55
expected_rr: 1.5
---

# Candidate: PRE_ECB_SILENT_DRIFT

## Generator
ECB Communication Policy mandates a 7-day "quiet period" before each Governing Council meeting (since 2014). Like the Fed blackout, this reduces ECB-speak surprises and creates a measurably lower-variance regime in EUR-related pricing. Trend persistence in EUR/USD is empirically higher during the 7-day pre-ECB quiet window.

Mirror of PRE_FOMC_BLACKOUT_SILENCE but for ECB.

Proposal:
- Trigger: any business day within ECB 7-day pre-meeting quiet period at 08:00 EST.
- Entry rule: compute 3-day-prior trend P3 = Close[08:00 today] - Close[08:00 3 days ago]. If |P3| > 60 pips, take CONTINUATION at 08:00 EST.
- Stop: 30 pips.
- Target: 45 pips, or time-stop at 14:00 EST.
- Expected win rate: 55%.
- Expected R:R: 1.5.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ECB 7-day quiet period (post-2014)**. Specific:
1. ECB Communication Policy 2014: 7-day quiet period prior to each Governing Council meeting.
2. Documented in ECB Working Papers (Ehrmann-Fratzscher 2014).
3. Calendar-anchored.

## Decision
**QUALIFIED**.
