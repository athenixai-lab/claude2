---
name: Realized_Range_Bracket_Foresight
status: KILLED
round: 13
constraint: ohlc_range_exceeds_net_move_tautology
expected_win_rate: 0.50
expected_rr: 1.0
---

# Realized_Range_Bracket_Foresight

## 1. Generator (Class B — second moonshot)
**Hypothesis.** On any M1 bar, the realized range `H − L` is always ≥ `|C − O|` (it is a mathematical identity; range ≥ |net move|). Average ratio empirically on EURUSD M1: `E[(H-L)/|C-O|] ≈ 2.5` (extreme excursions are typically 2–3× the net move). This means a bracket around the bar open with stop=full range and target=half range would have a structurally favourable hit rate.

The "limiting-belief override" angle: pure martingale theorem doesn't forbid this because the bracket is on a single-bar future and uses the *range expectation*, not the directional drift.

Can we monetize this without foresight?

- **Trigger.** Every M1 bar at its open.
- **Entry rule.** Place a bracket: long-stop at `open − 0.5 × ATR(20)`, long-target at `open + 0.25 × ATR(20)`; mirror for short. Take BOTH sides simultaneously (a straddle around the open).
- **Stop / Target.** As above.
- **Expected win rate.** ~65% on each leg (target closer than stop in distance terms × range exceedance).
- **Expected R:R.** 0.5 per leg by construction.

## 2. RNG Critic
On i.i.d. Gaussian with zero drift, hitting probability of a level `d` away within one bar is approximately `2 · Φ(-d/σ)` (twice the tail). Stop at 0.5σ, target at 0.25σ → P(target) ≈ 0.62, P(stop) ≈ 0.38; expected payoff per leg = 0.62 × 0.25σ − 0.38 × 0.5σ = 0.155σ − 0.19σ = **−0.035σ per leg.**

The favourable hit rate is exactly cancelled by the unfavourable R:R. This is Doob's optional stopping in action: any symmetric bracket on a martingale gives EV ≤ 0; the asymmetry in distances destroys what the asymmetry in probabilities gives. The "range > net move" identity does NOT generate edge — it's a tautology that holds for every martingale path.

Now consider both legs simultaneously. The two-leg PnL is dominated by the outcome where ONE leg stops and the OTHER targets. Net per bar = `target − stop = 0.25σ − 0.5σ = −0.25σ` in expectation across the bar outcomes. The "edge" disappears entirely. **KILL.**

## 3. Constraint Identifier
The constraint name itself describes a tautology, not a mechanism. "Range exceeds net move" is true for every random walk and every actual price path; it cannot generate edge by itself. The generator confused a mathematical identity with a tradeable mechanism. This is the canonical "Looks like edge, isn't" trap.

## 4. Testability Judge
Trivially testable, but the test will confirm the critic's calculation: EV = −0.035σ per leg before cost; strictly more negative after cost. No simulation needed — the analytic result is conclusive for any symmetric (zero-drift) candle generator.

## 5. Devil's Advocate
- Devil tries to save: "What if we only enter the long leg in bars where prior bar's close > prior bar's open?" Now it's not the range tautology — it's a directional momentum filter, which is Round 9's territory. Different mechanism.
- Devil tries: "What if we use the OHLC of the prior bar to infer intrabar path?" Foresight problem — even Garman-Klass style estimators give you statistics about path, not the path itself; cannot place orders based on what you don't know.
- Devil tries: "What if we asymmetric-size based on prior bar's color?" Now it's a stack on Round 12 or Round 9 — not new.
- **Devil cannot save the pure range-tautology version. KILL stands.**

## 6. RNG Test Result
Analytic: EV = −0.035σ per leg (negative). No edge.

## Verdict: KILLED
**Reason:** Mistakes a mathematical identity (range ≥ |net move|) for a tradeable mechanism. Optional stopping enforces zero EV on any symmetric bracket on a martingale; the favourable hit rate is exactly cancelled by the unfavourable R:R.

**Lesson:** "Limiting belief override" must respect theorems. The right contrarian move is "X *can* be monetized in a way you didn't think of" (e.g., spread capture); the wrong move is "X violates a theorem because it feels like it should." This candidate fell into the second trap.
