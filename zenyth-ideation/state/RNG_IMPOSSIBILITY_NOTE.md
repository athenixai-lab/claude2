# Round 8 — Meta: What "Impossible to Lose on RNG" Actually Means

This is not a candidate. It is the framing we use for every round after round 7.

## The hard theorem
Let `S_t` be a martingale (i.i.d. mean-zero returns, finite variance). Let `τ` be any stopping time using only the natural filtration of `S_t`, with `E[τ] < ∞` and `S_τ` bounded. Then by Doob's optional stopping:
`E[S_τ] = S_0`.

In words: **on a pure i.i.d. RNG, no strategy using only past prices can have EV ≠ 0**. This is a theorem, not an opinion. "Ignoring limiting beliefs" cannot override it — but it can stop us from misapplying it.

## Where the theorem doesn't apply (i.e., where edge can live)
1. **Convex payoffs.** Options, variance swaps. Not available on spot.
2. **Negative-cost actions.** Bid/offer spread capture (market making), swap interest, exchange rebates. EV > 0 *before* any path information. The cost is execution risk and adverse selection.
3. **Autocorrelated returns.** Trend-following on momentum, mean-reversion on overextension. Requires the RNG to NOT be i.i.d.
4. **Vol clustering (GARCH).** Volatility is forecastable even when direction is not. Enables asymmetric position sizing (Kelly with vol-targeting).
5. **Heavy tails with autocorrelation.** Trend-following captures fat-tail winners with capped losers. Requires both fat tails AND momentum.
6. **Discrete tick / finite precision.** Microstructure pin/repulsion near round levels.
7. **External state (calendar, news, flows).** The original framework's domain.

## What this means for the ideation loop going forward
Two classes are now valid:

- **CLASS A (calendar/mechanism).** Original spec: must FAIL on i.i.d. RNG. Edge lives in real-world flow mechanics on a clock.
- **CLASS B (structural RNG-beating).** New: edge must SURVIVE i.i.d. RNG and also produce reasonable EV on realistic candle generators (bootstrap-of-real-candles, GARCH-with-jumps).

A Class B candidate that claims to beat *pure* i.i.d. RNG is, by theorem, wrong somewhere. Either:
- it uses external state it isn't admitting to (it's secretly Class A),
- it relies on bankroll structure (Martingale doubling — not a real edge),
- it uses a negative-cost action available in real markets but invisible on M1 OHLC (market making — not testable here),
- it has a fat-tail or vol-clustering claim that secretly assumes non-i.i.d. RNG.

The devil's advocate's job is to figure out which.

## On law-of-large-numbers and M1
LLN convergence is a statistical fact, not an edge generator. With per-trade edge `e` and N trades, the standard error of mean PnL scales as `σ / √N`. To distinguish edge from noise at 3σ:
- `e = 0.05R` (1 pip on 20-pip risk): `N ≈ (3 σ_R / 0.05R)² ≈ 3600` trades minimum.
- `e = 0.20R`: `N ≈ 225` trades.

M1 gives volume — perhaps 5–20 trades/day per system on a clean trigger — so a year of M1 trading collects 1000–5000 trades, enough to validate `e ≥ 0.05R`. **This works for Class A; for Class B it depends on the trigger frequency.**

## Acknowledged limiting belief I am NOT going to override
"Pure i.i.d. RNG cannot be beaten by a price-only strategy." This is a theorem. Going to ignore it would not be open-minded — it would be wrong.

## Limiting beliefs I AM going to challenge in this loop
- "M1 spread costs eat all M1 edge" — false if e is large enough relative to spread; testable empirically.
- "Trend-following can't work on M1" — only true if M1 has zero autocorrelation, which it empirically does not for short horizons (microstructure mean-reversion) or long horizons (multi-bar momentum).
- "Round levels don't matter" — empirically there is a tiny but persistent magnet effect documented in BIS papers; worth retesting with proper controls.
- "You need DOM data to do anything useful on M1" — not true; OHLC has high/low which contain a subset of DOM information.
- "Calendar edges are already arbitraged out" — partially true for the most famous (Asian session breakout, NFP) but not for the niche ones (Gotobi, EURIBOR fix, mid-month BoJ refixing).

## Procedure going forward
- Generator proposes; tag class A or B.
- Critic runs an i.i.d. RNG simulation in their head; kills if Class A passes RNG or Class B fails it.
- Constraint identifier names mechanism precisely; kills if vague.
- Testability judge writes the loop in pseudocode against the EURUSD M1 dataset; kills if untestable.
- Devil's advocate (new explicit role): tries to construct a counterexample, find data-snooping, find structural overlap with prior candidates, find sample-size concerns. Only if devil's advocate fails does it qualify.

Now continuing with candidates.
