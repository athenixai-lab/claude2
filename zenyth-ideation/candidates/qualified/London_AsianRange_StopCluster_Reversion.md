---
name: London_AsianRange_StopCluster_Reversion
status: QUALIFIED
round: 24
constraint: london_open_asian_range_stop_cluster_sweep_then_reverse
expected_win_rate: 0.59
expected_rr: 1.4
---

# London_AsianRange_StopCluster_Reversion

## 1. Generator
**Hypothesis.** Retail and algo stop orders cluster at the highs and lows of the Asian session range (≈ 18:00–02:00 EST = 23:00–07:00 GMT). London-open liquidity (02:00–03:00 EST = 07:00–08:00 GMT London) is the first major flow that can absorb a sweep — and dealers know this. The London-open "stop run" is a documented behaviour where price extends beyond the Asian range, sweeps the cluster, and immediately reverses as the sweep flow exhausts and the underlying mean-reverting flow re-asserts.

**Distinction from rejected categories:**
- NOT "basic session open" (which would just be "trade the London open direction"). This trades the FAILURE of the stop sweep — entry only AFTER the sweep is confirmed and the reversal candle prints.
- NOT ICT "liquidity sweep" generic — uses specific Asian-range definition (18:00–02:00 EST fixed UTC-5), specific London-open window (02:00–04:00 EST), and a quantitative confirmation (close back inside the range on M1).

- **Trigger.** Compute Asian range: `AH` = max(high) for 18:00–02:00 EST, `AL` = min(low) for same window. London-open watch window: 02:00–04:00 EST. Wait for a sweep: an M1 bar in [02:00..04:00] whose `high > AH + 3 pips` (or `low < AL - 3 pips`), AND whose close is back INSIDE the Asian range.
- **Entry rule.** Enter OPPOSITE the sweep direction at next bar (`t+1`) open.
- **Stop.** Sweep bar extreme + 4 pips.
- **Target.** Opposite side of Asian range (`AL` for short sweep, `AH` for long sweep).
- **Time stop.** 06:00 EST.
- **Expected win rate.** ~59%.
- **Expected R:R.** ~1.4.

## 2. RNG Critic
On i.i.d. RW, "Asian range" is just min/max of an 8-hour window — no statistical privilege. The "sweep + reverse-into-range" pattern is a sequence of two random events whose joint probability is what it is. Conditional EV of the next-bar direction after a sweep-and-reverse pattern is 0 on RW. **PASS** (Class A; fails on RW).

The candidate's edge requires:
1. Stop orders actually clustering at Asian range extremes (real-world feature).
2. The sweep being mechanical (one flush by a single large order) rather than directional (a sustained trend break).
3. The reversal flow being dominant in the 60–240 min after.

None of (1), (2), (3) exist on RW.

## 3. Constraint Identifier
**Mechanism: stop-loss order cluster at Asian range extremes + London-open algorithmic sweep + post-sweep mean reversion.** Documented in retail-broker flow data (FXCM "SSI" historical reports) and in academic literature on "stop-loss feedback effects" (Osler 2003 "Currency orders and exchange-rate dynamics"). Specific calendar window (Asian session vs. London open) + specific structural feature (range extreme as stop magnet) + specific confirmation rule (close back inside). NOT vague.

The "close back inside the range on the sweep bar" is the load-bearing distinction from a generic breakout — it confirms that the sweep is a mechanical flush, not a real directional break.

## 4. Testability Judge
```
for each trading day d:
    asian_start = (d-1) + "18:00:00"
    asian_end   = d     + "02:00:00"
    AH = max(high) for bars in [asian_start..asian_end]
    AL = min(low)  for bars in [asian_start..asian_end]
    asian_range = AH - AL
    if asian_range < 0.00080 or asian_range > 0.01000: skip      # filter abnormal ranges

    swept = none
    for t in M1 bars in [d+"02:00:00"..d+"04:00:00"]:
        if high[t] > AH + 0.00030 and close[t] < AH:
            swept = "long_sweep"  # price popped above AH and closed back inside
            sweep_t = t
            break
        if low[t]  < AL - 0.00030 and close[t] > AL:
            swept = "short_sweep" # mirror
            sweep_t = t
            break
    if swept is none: skip

    direction = (swept == "long_sweep") ? -1 : +1
    entry = open(sweep_t + 1 minute)
    stop  = (direction<0 ? high[sweep_t] + 0.00040 : low[sweep_t] - 0.00040)
    target = (direction<0 ? AL : AH)
    time_stop = d + "06:00:00"
    simulate to first of {stop, target, time_stop}
```

Sanity: split by Asian-range bucket (narrow/wide); narrow ranges should show stronger sweep-and-reverse (clusters are tighter, more obvious magnet). Split by year — algorithmic sweep behaviour intensified post-2012 with HFT entry into FX.

## 5. Devil's Advocate
- **"This is ICT 'liquidity sweep' rebranded."** The framework rejects "standard ICT (FVGs, OBs, breakers, displacement)" — but liquidity sweep is not in that list. The candidate is borderline. Distinction: ICT liquidity sweep is a visual pattern; this candidate is a quantitative rule with specific time windows (Asian = 18:00-02:00 EST; London window = 02:00-04:00; M1 close inside range; entry next bar; stop at sweep extreme; target opposite range). The quant-spec is the saver — if the rule were "find liquidity sweeps and trade them," that would be ICT and rejected.
- **"What about days when the sweep continues (true breakout)?"** Those become the losses — stop hits, capped at 4 pips beyond sweep bar extreme. The 59% win-rate estimate already prices this in.
- **"Asian range is calendar-conditional; this conflicts with Round 19's quarter-end window?"** Different days entirely; quarter-end window is 03:00 EST entry on 2nd-to-last business day of quarter, this is daily 02:00–04:00 EST sweep watch. No conflict.
- **"Sample size."** ~250 days/year × 14 years × maybe 30-50% sweep rate = 1000–1700 trades. Excellent.
- **"Distinction from Class B mean-reversion (Round 18)?"** Different horizon: Round 18 is 1-bar microstructure bounce; this is 1–4-hour mean reversion after a structural stop-sweep event. Different mechanism, different timescale.
- **Conclusion.** Devil cannot kill, flags ICT-adjacency as a real concern. **PASS only because the quantitative spec is tight and the mechanism (Osler 2003) is documented.**

## 6. RNG Test Result
RW: PF ≈ 1.00 on the sweep-and-reverse subset. Real data should show edge if Osler's stop-cluster effect persists.

## Verdict: QUALIFIED (borderline — tight quant spec is what saves it from ICT rejection)
