---
name: NewYear_FirstSession_Drift
status: KILLED
round: 25
constraint: new_year_first_session_position_initiation
expected_win_rate: 0.55
expected_rr: 1.4
---

# NewYear_FirstSession_Drift

## 1. Generator
**Hypothesis.** On Jan 2 (or first trading day of January when Jan 1 is holiday), macro funds initiate new-year directional positions in the first London session. The direction is set by the previous year's themes (FOMC/ECB stance, growth differentials). Trade with the first hour of London (02:00–03:00 EST) on Jan 2.

## 2. RNG Critic
On RW, the "Jan 2" filter has no privilege. **PASS** RW.

## 3. Constraint Identifier — KILLED ON SAMPLE
**Sample is fatal.** 14 events in 14 years. Even with EV ~0.5R per trade, 14 trades gives 2σ confidence interval of ±0.6R — overlaps zero. The candidate cannot be validated to any meaningful confidence.

Additionally: the directional inference (last year's themes → new year direction) is qualitative and not encoded in any price-only rule. Without a quantitative trigger, the candidate becomes a discretionary call, which the framework cannot evaluate.

## 4. Testability Judge
Mechanically testable (calendar trivial), but N=14 is below the threshold for any meaningful inference. **KILL on sample.**

## 5. Devil's Advocate
- Devil tries: "Use prior-year EURUSD return as the direction signal — make it quantitative." Now testable. But N is still 14. Sample dominates.
- Devil tries: "Include first 5 days of January, not just Jan 2." Increases N to 70 — still small, and dilutes the mechanism (institutional position initiation is concentrated on Day 1, weakens by Day 5).
- **Devil cannot rescue from sample. KILL.**

## 6. RNG Test Result
RW PF = 1.00 ± massive noise on N=14.

## Verdict: KILLED
**Reason:** Sample size too small (N=14) to validate any effect of plausible magnitude. Annual-frequency triggers are fundamentally weak in this framework unless EV is enormous (≥1R per trade), which this mechanism doesn't credibly claim.
