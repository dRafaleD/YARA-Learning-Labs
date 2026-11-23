# Lab 59 — YARA Canary Rule Rollout and Regression Gates

[English](notes.md) · [Türkçe](notes.tr.md) · [V1](rules_v1.yar) · [V2](rules_v2.yar) · [V3](rules_v3.yar) · [Evaluator](evaluate.py)

## After Lab 58
Day 58 compared alert counts from pinned YARA rule versions on a **fixed test corpus**. Day 59 adds a deliberate **canary approval gate**: a new ruleset should be accepted only when its changes match the documented expectations.

## Exercise
Four fictional text events are scanned using three harmless rulesets:
- **V1** finds BLUE-TOKEN in events `e1,e3`.
- **V2** additionally finds GREEN-TOKEN in `e2`.
- **V3** additionally flags a benign `TRAINING-NOTE` event `e4`, an intentional regression.

A host-defined gate allows only **the expected new event ID `e2`**, with no removed baseline alerts. It labels V2 `PROMOTE_CANDIDATE` and V3 `QUARANTINE`. It prints a rule-file digest prefix to associate results with the exact ruleset bytes.

## Reproduce
YARA CLI required:
```bash
python3 labs/59-yara-canary-rule-rollout-and-regression-gates/evaluate.py
```

## Questions
Why compare the *identity* of added alerts rather than only totals? Why can rule rollout create false positives? Why should rule-file digests be included in reports? Why does a four-file canary not establish a statistically meaningful false-positive rate?

## Limits
Harmless synthetic strings, not real malware indicators. The gate is a toy deployment decision and is not a general YARA production policy.
