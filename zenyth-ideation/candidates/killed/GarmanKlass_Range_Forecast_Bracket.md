---
name: GarmanKlass_Range_Forecast_Bracket
status: KILLED
round: 20
constraint: range_forecast_using_garman_klass_estimator
expected_win_rate: 0.55
expected_rr: 1.0
---

# GarmanKlass_Range_Forecast_Bracket

## 1. Generator (Class B — fourth moonshot)
**Hypothesis.** The Garman-Klass volatility estimator uses (O, H, L, C) to estimate next-bar volatility more efficiently than close-to-close alone. Using `σ̂_GK(t)` as a forecast of `σ(t+1)`, place a bracket on the next bar where the stop is at `entry ± 2σ̂_GK` and target is at `entry ± 0.7σ̂_GK`. The favorable target-vs-stop hit probability (since target is closer) combined with vol clustering (the GK estimate is informative because vol is persistent) produces positive EV.

## 2. RNG Critic
**Pure i.i.d. Gaussian RNG, mu=0:** The GK estimator is consistent for volatility, but volatility on this RNG is *constant* and known — no forecasting gain. The bracket then has stop=2σ, target=0.7σ; on a martingale, EV per bar:
- P(target hit before stop) ≈ 2σ / (2σ + 0.7σ) = 74%
- EV = 0.74 × 0.7σ − 0.26 × 2σ = 0.518σ − 0.520σ ≈ **−0.002σ** (essentially zero before cost, negative after).

Optional stopping confirms: EV = 0 exactly on a brownian-motion bracket. **No edge on i.i.d.**

**Bootstrap with vol clustering:** The GK estimator gives a better-than-constant forecast of next-bar σ. But the bracket then *scales* to the new σ; the hit-probability arithmetic is unchanged (it's relative to the scaled bracket). The forecast quality does not generate EV in a bracket strategy — it only changes the scale of the per-trade PnL, not the sign of EV.

**Critic verdict:** This is Round 13's range-tautology trap in slightly disguised form. Better volatility forecasting does NOT produce directional EV when the bracket is symmetric. **KILL.**

## 3. Constraint Identifier
The "constraint" (GK is a more efficient vol estimator) is real and useful for risk-management (position sizing, VaR), but it is NOT a directional edge. The generator conflated "better forecast" with "tradeable forecast." A volatility forecast monetizes only via:
- Selling volatility (options — not available).
- Asymmetric position sizing on a strategy with positive directional EV (i.e., as Kelly-style sizing on top of Round 9 or Round 12).
- Vol-of-vol arbitrage (requires cross-section, not single instrument).

None of these are what the candidate proposed. **KILL.**

## 4. Testability Judge
Testable trivially. Result will confirm the analytic calculation: EV per bar ≈ 0 before cost; negative after. The volatility forecast provides no edge in a symmetric bracket on a single instrument.

## 5. Devil's Advocate
- Devil tries: "Asymmetric bracket — target equals stop in EV terms; tilt slightly." That's the same as Round 13; tilt destroys the hit-rate advantage exactly.
- Devil tries: "Use GK to size positions in a Class A or Class B strategy with real edge." That's a different strategy (sizing layer on top of an edge). Not what was proposed.
- Devil tries: "GK is biased for non-zero drift; maybe the bias generates edge?" Bias is tiny (~1%) and uniformly in the direction of *under*-estimating realized vol — that makes the bracket conservative, not directionally biased.
- **Devil cannot save it as a standalone bracket strategy. KILL stands.**

## 6. RNG Test Result
Analytic: EV ≈ 0 on RW; strictly negative after cost.

## Verdict: KILLED
**Reason:** Better volatility estimation is a sizing/risk tool, not a directional edge. Symmetric brackets on a martingale always have EV ≤ 0 regardless of how good the volatility forecast is.

**Lesson:** Information about volatility ≠ information about direction. Strategies need both for EV.
