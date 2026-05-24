---
name: NFP_INITIAL_SPIKE_FADE
status: KILLED
round: 7
constraint: nfp_release_830est
expected_win_rate: 0.50
expected_rr: 1.0
---

# Candidate: NFP_INITIAL_SPIKE_FADE

## Generator
NFP release is the first Friday of each month at 08:30 EST. The release is a "scheduled event constraint". Hypothesis: the M1 candle from 08:30 to 08:31 EST contains a wild initial reaction, but the next 10 minutes often reverse a significant portion (consensus surprise + initial liquidity sweep).

Proposal: fade the direction of the 08:30 M1 candle if range > 25 pips, entering at 08:31, target back to 08:29 close.

## RNG Critic
On a random walk, large-magnitude single-bar moves have ZERO predictive direction for the next bars in expectation; if anything, momentum (positive autocorrelation in extremes from volatility clustering in real data) would slightly favor CONTINUATION not fade.

BUT — on random walks, **a "large move" followed by partial mean reversion is also a natural property** of any process with mean-reverting tick noise relative to a transient liquidity shock. Even in i.i.d. data, a 25-pip single-minute move (which represents a huge tail) is followed on average by a smaller subsequent 10-min move in the same magnitude (regression to mean of |move|), but DIRECTIONAL fade ≈ zero.

So zero raw EV on RNG. After spread, NEGATIVE. PASSES RNG check on EV grounds.

HOWEVER — directional fade of news spikes is exactly the kind of edge that:
1. Has been heavily arbitraged since 2010 (HFT news algos).
2. Has variance >> mean — sample noise dominates.
3. Real fundamental surprise direction can persist for hours (Fed hike pricing).
4. Slippage on the entry candle (08:31 open is often gapped vs 08:30 close) destroys the entry price.

## Constraint Identifier
NFP IS a scheduled event constraint — VALID.
BUT the proposed exploitation (directional fade) is NOT a mechanical flow consequence. It's a behavioral guess about retail vs. algo positioning, which is fuzzy.

## Testability Judge
Backtestable, but the M1 NFP candle is extreme noise on 14-yr data: ~168 events, of which maybe 60 have >25 pip M1 candle. After spread+slippage drag (slippage on news minute ≈ 5–8 pips), the system likely has barely-positive raw expectancy and very high variance.

## Decision
**KILLED** — too noisy, the "edge" is not from a mechanical flow but from a behavioral guess that has been arbitraged. Variance >> expected mean; cannot achieve "immune to RNG" status because the directional component IS effectively coin-flip after costs.
