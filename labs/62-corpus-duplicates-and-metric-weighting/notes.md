# Lab 62 — Corpus Duplicates and Metric Weighting

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

Lab 61 measured precision, recall and F1. Today compare repeated observations against unique content. Seven harmless text observations represent four distinct SHA-256 digests. A repeated positive sample can make observation-weighted recall appear higher without increasing coverage of unique content.

| Count | Observations | Unique bytes |
|---|---:|---:|
| TP | 3 | 1 |
| FP | 1 | 1 |
| TN | 2 | 1 |
| FN | 1 | 1 |

Observation-weighted precision and recall are both 75%; unique-content precision and recall are both 50%. Neither weighting is universally preferable: document the unit of analysis. Conflicting labels for identical bytes are flagged rather than silently discarded.

**Practice:** duplicate a benign negative observation, compute both tables again, and explain which metrics change. Add a conflicting label and check the rejection. Expected: seven scans and six checks. Requires local YARA CLI. Synthetic text only, not real malware or production detection.

## Run
```bash
python3 labs/62-corpus-duplicates-and-metric-weighting/evaluate.py
```
