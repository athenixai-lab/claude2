---
name: PreECB_SpreadVacuum_Drift
status: KILLED
round: 6
constraint: scheduled_event_pre_release_vacuum
expected_win_rate: 0.50
expected_rr: 1.0
---

# PreECB_SpreadVacuum_Drift

## 1. Generator
**Hypothesis.** In the 5 minutes before ECB rate decisions (07:45 EST on ECB Thursdays, ~8 per year), liquidity providers pull quotes, spreads widen, and price drifts in the direction of the previous 30-minute trend. Trade with the drift into the release.

- **Trigger.** ECB rate decision day, 07:40 EST. 30-min prior trend > some threshold.
- **Entry rule.** Enter with the trend at 07:40 EST.
- **Exit.** 07:45 EST hard exit (before release).

## 2. RNG Critic
The "drift in direction of prior 30-min trend" is a momentum filter — on i.i.d. RW it has EV = 0. The ECB-day filter restricts the sample but does not change the conditional EV of the next 5-min path. The generator has NOT proposed a mechanism by which liquidity vacuum biases the *direction* of price movement — only that it widens spreads. Wider spreads make execution worse, not direction biased. **The candidate does not explain why the drift would CONTINUE rather than mean-revert during the vacuum. The rule is a momentum filter on a near-zero-vol window. KILL.**

## 3. Constraint Identifier
Mechanism (scheduled event pre-release liquidity vacuum) is real, but the generator conflated "liquidity drops" with "directional drift continues." These are independent claims. The liquidity-vacuum constraint is real for spread/cost analysis but does NOT generate directional alpha by itself — it AMPLIFIES whatever order arrives. To trade it, you need a separate directional signal from the same window, which the generator did not provide.

Sub-issue: the sample is tiny (~8 ECB days/year × 14 years = ~112 events). Way too small to ever validate even if the rule worked.

## 4. Testability Judge
The rule is testable mechanically (ECB calendar dates can be hard-coded), but the sample size (~112) is insufficient for any meaningful conclusion, and the proposed rule does not encode a real directional mechanism — it just filters to a tiny calendar subset and fades or rides a trend. **Untestable in the sense of producing a statistically meaningful conclusion.**

## RNG Test Result
On a synthetic RW restricted to the same number of "ECB-like" days, the prior-trend continuation rule has PF = 1.00 ± wide noise. Indistinguishable from random. The candidate fails the RNG test in the sense that any "edge" you saw on real data with N=112 is statistically indistinguishable from noise — meaning if you DID find a positive backtest, you couldn't reject the null.

## Verdict: KILLED
**Reason:** (a) Mechanism (vacuum → directional drift) is not coherent — vacuums amplify, they don't direct. (b) Sample size too small to ever validate. (c) Rule reduces to a momentum filter on a tiny calendar subset.
