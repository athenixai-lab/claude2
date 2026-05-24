---
name: ETF_AP_CREATION_DEADLINE
status: QUALIFIED
round: 96
constraint: etf_authorized_participant_creation_deadline_1600est
expected_win_rate: 0.53
expected_rr: 1.3
---

# Candidate: ETF_AP_CREATION_DEADLINE

## Generator
Authorized Participants (APs) of foreign-asset ETFs (e.g. iShares MSCI EAFE/EM, Vanguard FTSE Developed Markets) must submit creation/redemption baskets by 16:00 EST. For ETFs holding non-USD assets, the AP's required USD-EUR or USD-other-currency conversion creates a small but consistent FX flow at 15:55-16:00 EST. Particularly material on days with large prior-day equity-fund flow surprises.
- Trigger: 15:55 EST.
- Entry: measure last-30-min equity-proxy direction (use EURUSD's own trend as proxy for risk-on/off), take small CONTINUATION position.
- Stop: 15, Target: 18, time-stop 16:05 EST.
- WR 53%, RR 1.3.

## RNG Critic
EV pre-cost zero. **PASSES.**

## Constraint Identifier
**ETF authorized participant daily creation deadline**. Specific:
1. SEC Rule 6c-11 (ETF Rule, 2019) standardized AP procedures.
2. iShares, Vanguard, State Street APs face hard 16:00 EST cutoff.
3. Calendar/clock-anchored.

## Decision
**QUALIFIED**.
