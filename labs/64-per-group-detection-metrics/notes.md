# Lab 64 — Per-Group Detection Metrics and Aggregate Bias

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

Lab 63 audited dataset split integrity. Today compare group-level recall and false-positive rates against pooled metrics. The harmless BLUE-TOKEN rule perfectly classifies group A but fails both examples in group B. Expected pooled recall is 2/3 and FPR 1/3; group B recall is zero and FPR is one. Undefined denominators return None. Compute the two confusion matrices by hand and add a harmless negative example to group A. Explain why a strong aggregate can conceal a weak subgroup. Six invented text samples do not establish real detection quality. Requires YARA CLI; no malware or real indicators.

## Run
```bash
python3 labs/64-per-group-detection-metrics/evaluate.py
```
