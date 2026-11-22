# Lab 58 — Rule-Version Pinning and Alert Comparison

[English](notes.md) · [Türkçe](notes.tr.md) · [Version 1 rules](rules_v1.yar) · [Version 2 rules](rules_v2.yar) · [Evaluator](evaluate.py)

## After Lab 57
Day 57 maintained explicit **revision numbers** for late-arriving events in finalized time buckets. But alert counts can also change for a different reason: **the detection rule changed**. Mixing these causes produces misleading reports.

## Controlled comparison
Four identical, harmless sample texts are scanned under two separately named YARA rulesets:
- **v1:** match `BLUE-TOKEN` only.
- **v2:** match `BLUE-TOKEN` or `GREEN-TOKEN`.

The event IDs and sample batch stay fixed. The evaluator prints an SHA-256 fingerprint of the input batch and shows **2 flagged events under v1** versus **3 under v2**. Only fictional event `e2` changes status.

A production analyst should preserve `(ruleset version, evaluated batch identity, evaluation time)` with alert snapshots. A ruleset upgrade is not the same thing as late evidence or a newly infected host.

## Run
Requires a locally installed YARA CLI:
```bash
python3 labs/58-rule-version-pinning-and-alert-comparison/evaluate.py
```

## Questions
Why must old and new rule results be labeled separately? Why hold the same corpus fixed in a comparison? Why does one additional rule match not prove improved precision? What happens if a source file changes between evaluations?

## Limits
Synthetic text tokens only; not real indicators or malware detection rules. This script does not claim test execution without a local YARA CLI.
