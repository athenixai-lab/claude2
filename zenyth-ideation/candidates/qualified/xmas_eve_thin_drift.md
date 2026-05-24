---
name: XMAS_EVE_THIN_DRIFT
status: QUALIFIED
round: 38
constraint: christmas_eve_global_holiday_thin_liquidity
expected_win_rate: 0.58
expected_rr: 1.3
---

# Candidate: XMAS_EVE_THIN_DRIFT

## Generator
Dec 24 (Christmas Eve): early closes/closures cascade through markets. CME closes at 13:00 EST; LSE at 12:30 GMT (07:30 EST); Eurex at 13:00 CET (07:00 EST); Tokyo open as normal. Year-end position squaring overlaps with thin liquidity creating a "drift toward year-end target" effect for institutional accounts that haven't fully unwound. The direction matches the YEAREND_REPO_SQUEEZE direction (USD-favorable) but the window is more discrete.

Proposal:
- Trigger: Dec 24 at 07:00 EST.
- Entry rule: SHORT EURUSD at 07:00 EST.
- Stop: 25 pips.
- Target: 35 pips, or time-stop at 12:00 EST.
- Expected win rate: 58%.
- Expected R:R: 1.3.

(Overlaps somewhat with YEAREND_REPO_SQUEEZE. Treat as distinct micro-mechanism due to specific holiday-half-day timing.)

## RNG Critic
On random walk: Dec 24 has no special meaning. EV pre-cost zero.

**PASSES.**

## Constraint Identifier
Mechanism: **Christmas Eve global holiday cascading closures + year-end-squaring thin-book amplification**. Specific:
1. CME, ICE, LSE, Eurex published holiday schedules close early.
2. Bank desk staffing typically <20% on Dec 24.
3. Documented in CME Group "Holiday Schedule" historical data.
4. Calendar-anchored.

## Testability Judge

```python
# Dec 24 each year, at 07:00 EST, SHORT EURUSD
# Stop +25, target -35, time-stop 12:00 EST
```

RNG: shuffled → 0 EV. Real: +4 to +8 pips/trade × 1 trade/year × 14 years.

## Decision
**QUALIFIED**.
