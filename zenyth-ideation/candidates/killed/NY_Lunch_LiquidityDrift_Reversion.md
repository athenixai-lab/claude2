---
name: NY_Lunch_LiquidityDrift_Reversion
status: KILLED
round: 21
constraint: ny_lunch_thin_liquidity_revert_to_morning_vwap
expected_win_rate: 0.51
expected_rr: 1.1
---

# NY_Lunch_LiquidityDrift_Reversion

## 1. Generator
**Hypothesis.** Between 12:00–13:30 EST (NY lunch), liquidity thins as senior traders step away. Smaller orders cause exaggerated drift away from the morning VWAP. After 13:30 EST when desks repopulate, price tends to revert toward the morning VWAP. Trade the reversion at 13:30 EST.

- **Trigger.** Time = 13:30 EST. Compute VWAP from 09:30–12:00 EST. Compute drift = close(13:30) − VWAP_morning.
- **Entry rule.** Fade if `|drift|` > 0.8 × ATR(20 daily) / 6.5.
- **Stop.** 12:00–13:30 extreme + 4 pips.
- **Target.** VWAP_morning.
- **Time stop.** 15:00 EST.

## 2. RNG Critic
On i.i.d. RW, the 13:30 EST timestamp filter has no privilege. The "drift away from morning VWAP" filter is a percentile-of-distance rule that has EV = 0 on RW. The "revert to morning VWAP" target has no RW basis — RW has no anchor. **PASS** RW critique (Class A, fails on RW).

But Critic and Constraint Identifier converge on a different problem...

## 3. Constraint Identifier — **THIS IS WHERE IT FAILS**
**The named mechanism (NY lunch thin liquidity) is real, but the implied *direction* (drift away then revert) is not coherent.** If lunchtime liquidity is thin, then:
- Any large order moves price disproportionately (this IS happening).
- After 13:30 EST when liquidity returns, price moves to wherever the *new* flow takes it — not necessarily back to where it was. The mechanism does NOT predict mean-reversion to the morning VWAP. It predicts that whatever drift happened at 12:00–13:30 is now subject to the next round of order flow, which is independent of the lunch drift.

The "revert to morning VWAP" is a *prior* of the trader, not a *mechanism*. Without a flow-based reason for the reversion, the rule reduces to a generic mean-reversion fade — which fails on RW and has no calendar advantage on real data either (the calendar gates the WINDOW but not the DIRECTION).

**KILL.** The mechanism (thin lunch liquidity) is real but the directional claim (post-lunch revert to morning VWAP) is unsupported. Without the directional anchor, the rule is generic noise-fade dressed up in calendar clothing.

## 4. Testability Judge
Testable trivially. Expected result: PF near 1.0 (slightly above or below); no meaningful EV after cost. The kill is on mechanism coherence, not testability.

## 5. Devil's Advocate
- Devil tries to save: "Use 30-day rolling proof that drift mean-reverts on real data." If empirically true, the candidate could be QUALIFIED-pending-test. But the *mechanism* is still vague; you'd just be calendar-conditioning a generic fade with no flow story.
- Devil tries: "What if morning desks return at 13:30 with a 'unwind the noise' bias?" Plausible but not documented; speculative.
- Devil tries: "Combine with options pin (Round 5)?" Different window, not naturally compatible.
- **Devil cannot articulate a tight, documented mechanism. KILL stands.**

## 6. RNG Test Result
RW: PF ≈ 1.00. Real data: likely similar (no documented mechanism predicts otherwise).

## Verdict: KILLED
**Reason:** Mechanism (thin lunch liquidity) is real but doesn't directionally bias post-lunch flow. The "revert to morning VWAP" rule is a trader prior, not a flow mechanism. Reduces to generic mean-reversion with calendar dressing — exactly the type the framework was designed to reject.
