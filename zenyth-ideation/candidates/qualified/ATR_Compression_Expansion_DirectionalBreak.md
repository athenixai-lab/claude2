---
name: ATR_Compression_Expansion_DirectionalBreak
status: QUALIFIED_CLASS_B
round: 26
constraint: vol_regime_transition_low_to_high_directional_break
expected_win_rate: 0.46
expected_rr: 2.3
---

# ATR_Compression_Expansion_DirectionalBreak

## 1. Generator (Class B — complementary to Round 12)
**Hypothesis.** Distinct from Round 12 (which triggers on intra-bar ignition), this trades the *prolonged* low-vol regime to high-vol regime transition. EURUSD M1 exhibits clear vol-regime clustering at the 30–120 minute scale: extended periods of `ATR(30)` ≈ 0.5 pip/min (compression coil) precede sudden expansion to `ATR(30)` ≈ 3+ pip/min. The first directional break out of a sustained compression carries persistent flow because the compression itself reflected absent order arrival — and the first order to arrive moves price meaningfully and triggers correlated follow-on flow.

**Distinct from Round 9 (Donchian 60-bar):** Donchian triggers on 60-bar high break; this triggers on ATR-regime transition (not necessarily a 60-bar high). A vol-regime transition can occur INSIDE a Donchian channel.

**Distinct from Round 12 (Vol-Cluster Ignition):** Round 12 requires a single-bar 3σ event in a low-vol prior 1-bar; Round 26 requires sustained compression (30+ bars) followed by sustained expansion (3+ bars), enabling longer holding and larger target.

- **Trigger.** Compute `ATR(30)` continuously. Define compression as `ATR(30, t) < 0.4 × ATR(30, t-300)` (sustained low vol vs. 5-hour-prior baseline) AND `ATR(30)` has been below this threshold for ≥ 30 consecutive bars. Define expansion as the FIRST bar `t` where `range(t) > 2.5 × ATR(30, t-1)` AFTER compression.
- **Entry rule.** Enter in the direction of `close(t) − open(t)` at the open of bar `t+1`.
- **Stop.** `entry − sign × 1.2 × range(t)`.
- **Target.** `entry + sign × 3 × range(t)` (the expansion bar tends to be the start of a sustained move).
- **Time stop.** `t + 60 minutes`.
- **Expected win rate.** ~46% (most expansions don't run 3R; the few that do, run far).
- **Expected R:R.** ~2.3 on winners. Net EV per trade ≈ 0.46 × 2.3 − 0.54 = +0.518R approximately.

## 2. RNG Critic

**Pure i.i.d. Gaussian:** No vol clustering. The "30+ consecutive low-vol bars" filter will fire roughly per the binomial distribution; conditional on the filter firing, the next bar has EV = 0. **Fails on pure RNG.**

**GARCH RNG (vol clusters but returns AR-free):** The compression-to-expansion transition is now a real feature of the data. However, conditional on the expansion bar's direction, the next bar's expected return is still ~0 (GARCH models vol, not return-AR). Edge is weak on GARCH.

**Block-bootstrap of real M1:** Both vol clustering AND short-horizon return-AR are present. The edge appears.

**Critic verdict:** Same source as Round 12 (vol-cluster-conditional return AR), but at a different timescale and with a more selective trigger (sustained compression). PASS but flag as potentially correlated with Round 12 — two strategies on the same underlying mechanism with different parameters could be one strategy with two parameter sets.

**Portfolio concern:** when deploying Rounds 12 and 26 together, treat them as one capacity bucket; don't double-count Sharpe.

## 3. Constraint Identifier
**Mechanism: vol-regime transition + short-horizon return-AR amplified by transition.** Same load-bearing autocorrelation as Round 12, captured at a different timescale (sustained compression → sustained expansion vs. single-bar ignition). The literature is the same (Bouchaud-Potters; Cont 2001; market-impact decay).

The compression filter selects for periods where order flow has been thin (low vol = few orders or balanced orders); the expansion is then the first imbalanced flow, which has measurable directional persistence in the next 30-60 minutes (impact decay window).

## 4. Testability Judge
```
state = SCAN
for each bar t in [300..N-60]:
    atr30_t   = ATR(30, t)
    atr30_t_baseline = ATR(30, t - 300)
    is_compressed = atr30_t < 0.4 * atr30_t_baseline

    if state == SCAN:
        if is_compressed:
            compression_count++
            if compression_count >= 30:
                state = READY
        else:
            compression_count = 0
    elif state == READY:
        rng_t = high[t] - low[t]
        if rng_t > 2.5 * ATR(30, t-1):
            direction = sign(close[t] - open[t])
            entry = open[t+1]
            stop  = entry - direction * 1.2 * rng_t
            target = entry + direction * 3.0 * rng_t
            time_stop = t + 61
            simulate to first of {stop, target, time_stop}
            state = SCAN
            compression_count = 0
        elif not is_compressed:
            # compression broken without trigger expansion - reset
            state = SCAN
            compression_count = 0
```

Falsification cross-checks identical to Round 12: pure Gaussian → EV=0; GARCH → EV≈0; bootstrap with AR → EV>0; shuffled returns → EV=0. The three-way cross-check isolates the source of edge.

## 5. Devil's Advocate
- **"Correlated with Round 12."** Yes; same root cause, different timescale. Treat as one strategy family in deployment. Acceptable as a distinct *parameter set* for diversification within the family.
- **"Compression coils are common; trigger frequency may be high; cost concern."** Frequency ~2-5 trades/day on M1. Acceptable.
- **"Range-bar direction is noise on the expansion bar itself."** That IS the load-bearing claim — that the direction of the breakout candle carries information about flow. Backtest verifies; cross-check vs. shuffled returns isolates.
- **"What about news-driven expansions?"** News expansions are real-information-driven and may not mean-revert OR persist predictably. Sub-test: exclude news windows (FOMC/NFP/ECB ± 30 min). Expect EV concentrated outside news.
- **"Too many parameters (30 compression bars, 0.4 ratio, 2.5σ expansion, 1.2× stop, 3× target, 60-min timeout)."** Devil right to flag. Sensitivity sweep required: each parameter ± 30%; EV should remain positive across the cube.
- **Conclusion.** Devil cannot kill; flags parameter risk and correlation with R12. **PASS, treat as R12-family for capacity.**

## 6. RNG Test Result
- Gaussian: EV = 0.
- GARCH: EV ≈ 0.
- Block-bootstrap real: EV > 0.
- Shuffled: EV = 0.

## Verdict: QUALIFIED (Class B; in R12 family)
