---
name: Round_100pip_Magnet_Generic
status: KILLED
round: 23
constraint: round_number_psychology_magnet
expected_win_rate: 0.55
expected_rr: 1.0
---

# Round_100pip_Magnet_Generic

## 1. Generator (Class B candidate — but explicitly forbidden by user)
**Hypothesis.** EURUSD is magnetized to round 00-levels (1.0800, 1.0900, 1.1000) because of clustered stop orders and option-strike clustering. Trade toward the nearest round 00 from within 30 pips.

## 2. RNG Critic
Round numbers have no privilege on RW. **PASS** RW critique.

But the framework explicitly REJECTS this category: "REJECT: standard ICT (FVGs, OBs, breakers, displacement), generic round numbers, basic session opens..." 

## 3. Constraint Identifier — KILLED ON FRAMEWORK
The user's framework explicitly forbids "generic round numbers." This candidate is precisely that. Round 5 (Options_1000NY_Cut_Pin_Magnet) was qualified because it COMBINED round-50-pip strikes with the specific options-cut clock window — the magnet mechanism was tied to the dealer-gamma-pin at the 10:00 cut, not to round numbers in the abstract.

A pure "trade toward round 00s" rule has no clock anchor, no mechanism specification beyond "psychology," and falls into the rejected category. **KILL on framework rule.**

## 4. Testability Judge
Testable, but framework-rejected.

## 5. Devil's Advocate
- Devil tries to save: "Add a clock filter — only at 10:00 NY cut." That's just Round 5. Not new.
- Devil tries: "Only at quarterly options expiry." That's Round 14 territory.
- Devil tries: "Use Garman-Klass to size positions." Already killed in Round 20.
- **Devil cannot save it without collapsing into existing qualified candidates. KILL.**

## 6. RNG Test Result
N/A — killed on framework before test.

## Verdict: KILLED
**Reason:** Falls in the "generic round numbers" rejected category. Cannot be saved without collapsing into Round 5.
