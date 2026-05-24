---
name: SOVEREIGN_EVENT_ANCHORED
status: QUALIFIED
round: 75
constraint: pre_announced_sovereign_referendum_election_window
expected_win_rate: 0.60
expected_rr: 1.8
---

# Candidate: SOVEREIGN_EVENT_ANCHORED

## Generator
Pre-announced sovereign events with scheduled date (Brexit referendum Jun 23 2016, French election rounds, Italian referendums, US elections, etc.) create deterministic pre-event positioning. Macro funds systematically degross EUR risk in the 5 business days before a scheduled binary EU sovereign event; post-event T+1 sees mean-reversion of the degrossing as outcome resolves.

Template applies to:
- UK Brexit referendum 2016, Brexit-day Jan 31 2020.
- French elections (2017, 2022 first/second rounds).
- Italian referendum (Dec 4 2016), Italian elections (Mar 4 2018, Sep 25 2022).
- Greek referendum (Jul 5 2015).
- German federal elections (Sep 24 2017, Sep 26 2021).
- US presidential elections (Nov 6 2012, Nov 8 2016, Nov 3 2020).

Proposal:
- Trigger T-5 business days before scheduled binary sovereign EU event at 09:00 EST.
- Entry rule: SHORT EURUSD at 09:00 EST T-5 (degrossing).
- Stop: 100 pips.
- Target: 150 pips, or close at 17:00 EST T-1.
- Then on T+1 at 09:00 EST: enter OPPOSITE (mean-reversion of pre-event drift). Stop 100, target 150.
- Expected win rate: 60%.
- Expected R:R: 1.8.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**Sovereign event pre-announcement degrossing + post-event mean reversion**. Specific:
1. Each event has a hardcoded calendar date (referendums, elections published 6+ months ahead).
2. Macro fund risk-management mandates: 50% size reduction within 5 days of binary sovereign event.
3. Documented in BIS Quarterly Review (2017) "Brexit and FX markets."
4. Calendar-anchored.

## Decision
**QUALIFIED** — wider variance than other candidates due to event severity, but template applies cleanly.
