---
name: M1_BarSkew_Asymmetry_Directional
status: KILLED
round: 28
constraint: ohlc_intrabar_skew_predicts_next_bar_direction
expected_win_rate: 0.53
expected_rr: 1.1
---

# M1_BarSkew_Asymmetry_Directional

## 1. Generator (Class B — fifth and final RNG-impossible attempt)
**Hypothesis.** The intra-bar position of close relative to (high+low)/2 — call it `BarSkew = (close - (high+low)/2) / (high-low)` — carries information about *unfinished* directional flow. If close is in the top quartile of the bar's range, the buying flow was strong at the bar's end and likely continues; if in the bottom quartile, selling. Trade in direction of BarSkew on the next bar.

This is the "directional" variant of the Round 13 range tautology — instead of using range as a tradeable, use the *position within the range* as a signal.

## 2. RNG Critic

**Pure i.i.d. Gaussian:** On a Brownian path within a single bar, the position of the close relative to the high-low midpoint is symmetric — the conditional probability that the path ends in the top half given it visited both extremes is 50%, and there is zero predictive value for the next bar's direction. This is the *reflection principle* result: conditional on (open, high, low, close) being what they are, the next bar is independent. **EV = 0 on i.i.d.**

**Bootstrap of real M1:** Here the situation is subtle. Empirically, M1 bars with high-skew close (close near high) are followed by:
- 1-bar later: slight NEGATIVE expected return (bid-ask bounce; this is the Round 18 mechanism, opposite direction to the bar-skew prediction).
- 5-30 bars later: slight POSITIVE expected return (momentum; this is the Round 9/12/26 mechanism).

So at 1-bar horizon (which is what this candidate proposes), the edge is *opposite* to the bar-skew direction. The candidate gets the direction WRONG at the proposed horizon.

**Critic verdict:** On real data, this strategy systematically loses because it predicts continuation at the 1-bar horizon where the empirical effect is reversion. **KILL.**

This is a useful kill because it shows the failure mode of "limiting belief override" applied without empirical anchoring: the intuition "strong close = continuation" is folk-finance; the empirical reality at 1-bar M1 is the opposite.

## 3. Constraint Identifier
The proposed "constraint" (intrabar skew predicts next bar direction) is empirically false at the 1-bar horizon and only correct at the 5-30 bar horizon — at which point it is already captured by Round 9 (Donchian breakout, which conditions on multi-bar trend).

## 4. Testability Judge
Testable. The expected result: 1-bar EV is slightly NEGATIVE (consistent with Round 18 / Roll bid-ask bounce). Confirms kill.

## 5. Devil's Advocate
- Devil tries to save: "Use the 5-bar horizon instead." That collapses into Round 9 / Round 12 territory and is not new.
- Devil tries: "Use bar-skew as a *secondary* filter on top of a Class A calendar candidate." Plausible — but that's a refinement, not a standalone strategy. Could be a useful sizing/conditioning layer on Round 1 or Round 11.
- Devil tries: "Reverse the rule — trade OPPOSITE bar-skew at 1-bar (i.e., fade the strong close)." That's Round 18 rephrased; not new.
- **Devil cannot save it as a standalone 1-bar continuation rule. KILL stands.**

## 6. RNG Test Result
- Pure Gaussian: EV = 0.
- Real data, 1-bar horizon: EV < 0 (loses due to bid-ask bounce dominance at 1-bar).
- Real data, 5-30 bar horizon: EV > 0 (but that's Round 9 territory).

## Verdict: KILLED
**Reason:** Empirically wrong direction at the proposed 1-bar horizon. The folk-intuition "strong close = follow-through" is reversed on M1 EURUSD where bid-ask bounce dominates at 1-bar lag. The correct strategy at 1-bar is the OPPOSITE (Round 18, already qualified).

**Lesson:** "Ignore limiting beliefs" must be tested against empirical reality, not assumed. Sometimes the limiting belief is the empirically correct one and the "override" is the wrong direction.
