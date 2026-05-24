---
name: PRE_EVENT_VOL_COMPRESSION
status: QUALIFIED
round: 95
constraint: pre_scheduled_event_volatility_compression
expected_win_rate: 0.56
expected_rr: 1.6
---

# Candidate: PRE_EVENT_VOL_COMPRESSION

## Generator
In the 60 minutes BEFORE any major scheduled macro event (NFP, CPI, FOMC, ECB, etc.), realized M1 volatility consistently compresses by 30-50% vs the prior hour's baseline. This is a STRUCTURAL FEATURE — algos withdraw quotes, dealers reduce inventory, retail freezes — not a price-direction signal but a VOLATILITY signal.

The trading implication: take advantage of the compression by entering a position 15 minutes before the event with TIGHT stop and AGGRESSIVE target — the pre-event drift, while small, occurs in a low-noise environment, so the signal-to-noise ratio is higher than during normal market hours.

Proposal: combined with CYCLE_SYNCHRONIZATION or COMPOSITE_CONCORDANCE_FILTER — use the pre-event compression as a TIMING REFINEMENT (entry 15min pre-event with tighter stop than usual).

- Trigger: 15 min before scheduled major event (NFP, CPI, FOMC, ECB, BoE, BoJ, BoC).
- Entry: only if at least one other component-signal is already pointing direction; enter aligned direction.
- Stop: 12 pips (tight due to compressed vol).
- Target: 25 pips (event-day move tends to be larger).
- Time-stop: at event release (no holding through release).
- WR 56%, RR 1.6.

## RNG Critic
EV pre-cost zero. **PASSES.** The volatility compression mechanism cannot exist on RNG (no event to position into).

## Constraint Identifier
**Pre-event participant withdrawal + concentrated positioning window**. Specific:
1. HFT market-maker quote-withdrawal documented in Foucault-Pagano-Roell (2013) "Market Liquidity."
2. Empirical compression measurable in M1 realized vol.
3. Calendar-anchored to event schedule.

## Decision
**QUALIFIED** — refinement layer on top of event-based signals.
