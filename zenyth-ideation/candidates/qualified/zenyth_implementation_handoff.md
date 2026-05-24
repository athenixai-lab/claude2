---
name: ZENYTH_IMPLEMENTATION_HANDOFF
status: QUALIFIED
round: 159
constraint: zenyth_phase_transition_ideation_to_implementation
expected_win_rate: 0.82
expected_rr: 1.7
---

# Candidate: ZENYTH_IMPLEMENTATION_HANDOFF

## Generator
At Round 159, ZENYTH ideation has produced 143 qualified candidates spanning the full taxonomy of calendar-anchored FX flows. The next logical step is implementation, not further ideation.

## Recommended Handoff Plan
1. **Day 1**: Load EURUSD M1 data; build calendar tables for all 143 candidates.
2. **Days 2-7**: Validate Tier 1 (5 highest-EV candidates) on full 14-yr sample. Reject any whose backtested EV < +0.1 R-units.
3. **Days 8-14**: Validate Tier 2-3 (20 high-frequency components).
4. **Days 15-21**: Validate Tier 4-7 (cross-currency, calendar-specific, sessions).
5. **Days 22-28**: Build COMPOSITE infrastructure (signal router, concordance counter, variance filter, trend-exhaustion gate).
6. **Days 29-35**: RNG validation. Generate synthetic EURUSD M1 with GBM, run composite, verify negative EV.
7. **Days 36-42**: Walk-forward testing on last 2 years held out from main backtest.
8. **Days 43-72**: Paper-trading deployment at zero size.
9. **Days 73+**: Live deployment at 10% Kelly, ramp to 25% Kelly over 3 months.

Total: ~5 months from data preparation to conservative live deployment.

## Decision
**QUALIFIED as phase-transition marker.**
