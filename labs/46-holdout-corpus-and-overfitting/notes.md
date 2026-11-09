# Lab 46 — Holdout Corpora and Rule Overfitting

[English](notes.md) · [Türkçe](notes.tr.md) · [Rules](rules.yar) · [Evaluator](evaluate.py)

## Why a training score can mislead
Lab 45 compared two YARA revisions on the **same** small labeled corpus. Now separate cases used during rule design (**training**) from previously unseen cases (**holdout**). A perfect training score is not a promise of generalization.

We use invented document markers, not malware samples. One rule matches `TEST-CANARY` alone; the other requires `TEST-CANARY` plus `ACTION-CHECK`. The strict rule fits the training positives exactly. A new positive holdout variant with `ACTION-REVIEW` illustrates why its recall may fall despite looking excellent on training data.

## Read the confusion matrix
- **TP:** positive labeled sample matches.
- **FP:** negative labeled sample matches.
- **TN:** negative labeled sample does not match.
- **FN:** positive labeled sample does not match.
- **Precision:** TP / (TP + FP); **recall:** TP / (TP + FN). If a denominator is zero, the metric is undefined.
- Labels are **synthetic ground truth for this exercise only**; they are not a malware verdict.

## Run locally
Install the YARA command-line tool separately. The evaluator uses Python's standard library, a temporary directory, and locally generated harmless text.

```bash
yara --version
python3 evaluate.py
```

The script executes **both rules against both sets** and prints their confusion matrices and precision/recall. It also checks that the strict rule fits all training examples but misses one holdout positive. No network calls, real suspicious files, or persistent sample directory are involved.

## Questions and changes
1. Why can a rule with higher training precision still be brittle?
2. List the feature shared by both holdout positives. Which feature is missing from one?
3. Add a holdout negative containing both markers in quoted documentation. What happens to precision?
4. Propose a third revision **without editing the holdout labels to flatter the result**.
5. How would you build a larger, independently collected, deduplicated corpus and prevent train/test leakage?
6. Why is using only four holdout items insufficient to claim deployment quality?

## Limitations
The dataset was intentionally constructed to teach overfitting. Real YARA detection requires representative data, independent labels, provenance, versioning, and much larger validation. A YARA match alone never proves that a file is malicious.
