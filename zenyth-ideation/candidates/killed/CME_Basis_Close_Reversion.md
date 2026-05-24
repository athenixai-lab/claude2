---
name: CME_Basis_Close_Reversion
status: KILLED
round: 3
constraint: cme_pit_settle_basis
expected_win_rate: 0.51
expected_rr: 1.0
---

# CME_Basis_Close_Reversion

## 1. Generator
**Hypothesis.** CME 6E (EUR FX futures) pit settlement at 14:00 CT (15:00 EST) creates a basis-arbitrage rebalancing in EURUSD spot in the minutes following the settlement print. Spot is supposed to revert toward the post-settle basis-implied level.

- **Trigger.** Time = 15:01–15:15 EST.
- **Entry rule.** Measure last 15-min spot drift; fade if >1 std.
- **Stop.** 4 pips.
- **Target.** 4 pips.

## 2. RNG Critic
The hypothesized basis arb is supposed to operate via dealer cross-venue rebalancing. But the critic flags: M1 EURUSD spot in 14:45–15:30 EST is one of the quietest, most range-bound windows of the day (NY lunch tail). Any "fade after 1-std move" reduces, on a random walk, to a generic mean-reversion filter — which fails on RW (i.i.d. has zero mean reversion). The proposed entry rule does NOT actually condition on basis; the trigger is purely a spot-displacement filter. Under RW it would simulate identically to a random-displacement fade with EV ≤ 0 net of cost. The candidate as written does not encode the basis mechanism — it's a thin pretext over a generic reversion. **KILL on RNG basis: the rule is structurally indistinguishable from a generic fade and does not exploit the named constraint.**

## 3. Constraint Identifier
Mechanism named (CME pit settle basis) is real, but the generator failed to translate it into a price-only trigger. Without a futures basis feed (or at minimum the futures settlement print), there is no way the M1-spot-only rule can isolate the basis-driven flow from generic noise. The constraint is unobservable in the available data. **Concur with kill.**

## 4. Testability Judge
Would require CME 6E futures intraday + settlement prints, which are NOT in the 14y EURUSD M1 dataset. **Untestable as specified. KILL confirmed.**

## RNG Test Result
On synthetic RW the fade-1-std-displacement-at-15:01 rule produced PF = 0.99 ± noise, indistinguishable from random. No edge.

## Verdict: KILLED
**Reason:** Mechanism is real but unobservable in available data; price-only rule reduces to generic noise-fade with no constraint encoding.
