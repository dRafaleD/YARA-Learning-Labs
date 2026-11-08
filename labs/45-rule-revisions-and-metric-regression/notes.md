# Lab 45 — Rule Revisions and Metric Regression

[English](notes.md) · [Türkçe](notes.tr.md) · [Rule v1](rules_v1.yar) · [Rule v2](rules_v2.yar) · [Evaluator](evaluate.py)

## Why this lab?
Lab 44 introduced labeled positive and negative samples. A detection rule may appear better after editing, yet the only defensible improvement is a **measured difference on the same labeled corpus**. This lab compares two revisions using harmless text fixtures.

## Rule design
The first revision matches `DOC-ALPHA` anywhere. That is deliberately broad; a benign guide mentioning this label will also match. The second revision requires both `DOC-ALPHA` **and** `ACTION-VERIFY`. Requiring correlated strings reduces this specific false positive but could miss future legitimate positive variations. More conditions do not guarantee a better real-world rule.

## Reproducible experiment
Prerequisite: install the YARA CLI separately and ensure `yara` is on PATH.

```bash
python3 evaluate.py
```

The evaluator creates **four temporary synthetic files**, runs each rule version against the **same files**, and prints the confusion matrix:
- TP: positive sample matched; FP: negative sample matched.
- TN: negative sample not matched; FN: positive sample missed.
- Precision = TP / (TP + FP), recall = TP / (TP + FN). A zero denominator is **undefined**, not zero.

For these four intentionally designed examples, expected counts are **v1: TP=2, FP=1, TN=1, FN=0** and **v2: TP=2, FP=0, TN=2, FN=0**. The script asserts the expected outcomes.

## Your investigation
1. Explain why a benign file containing `DOC-ALPHA` triggers v1.
2. Add a positive case that contains only the first marker. How does v2 recall change?
3. Record your test corpus labels, rule versions and tool version.
4. Why is the tiny curated set unfit for real malware detection claims?
5. Propose a blind holdout corpus and version-control review policy.

## Safety and limitations
No malware, live targets or third-party binaries. Metrics describe only these synthetic examples; never interpret a YARA match as proof of maliciousness.
