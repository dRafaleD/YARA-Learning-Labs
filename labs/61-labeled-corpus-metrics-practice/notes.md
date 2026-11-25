# Lab 61 — Practice Day: Labeled Corpus and Detection Metrics

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules_v1.yar](rules_v1.yar) · [rules_v2.yar](rules_v2.yar)

Scan 12 harmless labeled text examples under each of two rule versions. The positive label means the fictional training task considers the sample relevant; it does not mean malware. Record every TP, FP, TN and FN.

| Metric | V1 | V2 |
|---|---:|---:|
| TP | 3 | 5 |
| FP | 1 | 2 |
| TN | 5 | 4 |
| FN | 3 | 1 |
| Precision | 75.0% | 71.4% |
| Recall | 50.0% | 83.3% |
| F1 | 60.0% | 76.9% |
| False positive rate | 16.7% | 33.3% |

Precision = TP/(TP+FP). Recall = TP/(TP+FN). FPR = FP/(FP+TN). F1 is the harmonic mean of precision and recall. Undefined ratios are represented by None rather than fabricated zeros.

**Exercises:** Build both confusion matrices by hand, predict each of the 24 sample evaluations, calculate F1, add two harmless negative fixtures and recompute counts. Compare the tradeoff in recall and false positives; explain why this tiny corpus cannot validate production detection. Do not change rules based on the evaluation set and then claim independent validation.

Expected final line: 24 sample evaluations + 7 metric checks passed. Requires local YARA CLI; no real malware, real indicators or network activity.

## Run
```bash
python3 labs/61-labeled-corpus-metrics-practice/evaluate.py
```
