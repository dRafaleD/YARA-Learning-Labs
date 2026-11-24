# Lab 60 — Canary Holdout and Labeled Regression Corpus

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules_v1.yar](rules_v1.yar) · [rules_v2.yar](rules_v2.yar)

Lab 59 compared rule rollout candidates on a known canary set. Lab 60 introduces a separate **labeled holdout**. The wider rule improves the development set but flags a harmless holdout color legend. The script computes TP, FP, TN and FN separately for both splits, preserving each rule's SHA-256. The labels describe an invented detection task, not malware.

**Questions:** Why should a holdout be independent of rule tuning? Why does improved development recall not prove improved detection quality? Why should a holdout false positive trigger review?

Six synthetic text fixtures are deliberately tiny; they cannot estimate real-world false-positive rates. No malicious files or real indicators are used. Requires YARA CLI.

## Run
```bash
python3 labs/60-canary-holdout-and-labeled-regression-corpus/evaluate.py
```
