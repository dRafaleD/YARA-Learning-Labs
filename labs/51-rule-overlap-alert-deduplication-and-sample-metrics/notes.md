# Lab 51 — Rule Overlap, Alert Deduplication and Sample-Level Metrics

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## From Day 50
Stratified evaluation reveals subgroup differences. A second reporting pitfall appears when **multiple YARA rules match the same sample**. Counting each matching rule as a separate infected file inflates apparent event volume.

## Training corpus
Three harmless rules search for `BLUE-TOKEN`, `GREEN-TOKEN`, or both. Five synthetic text samples have independently assigned *toy* labels:
- positive with both tokens → 3 rule matches;
- positive with BLUE only → 2;
- negative with BLUE only → 2 (false alarms);
- negative with GREEN only → 1;
- negative plain text → 0.

This gives **8 raw rule alerts** but only **4 unique flagged samples**. At the sample level, TP=2, FP=2, TN=1, FN=0. The labels are deliberately artificial, not proof of real malware.

## Reproduce
Requires YARA CLI in your PATH:
~~~bash
python3 labs/51-rule-overlap-alert-deduplication-and-sample-metrics/evaluate.py
~~~

## Questions
1. Why is the number of rule matches different from the number of affected files?
2. When would grouping by file hash fail to distinguish separate incidents?
3. Why do sample-level precision and recall require labels independent of the rules?
4. How can rule overlap cause alert fatigue in a SOC?

## Limitations
Only harmless synthetic text; no live malware, real detection claims or deployed SIEM.
