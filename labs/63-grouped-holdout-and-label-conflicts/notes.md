# Lab 63 — Grouped Holdout and Corpus Label Conflicts

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

Lab 62 examined duplicate weighting. Today check exact-content overlap between development and holdout before scanning. Identical SHA-256 content in both splits triggers SPLIT_OVERLAP, and inconsistent labels for identical bytes trigger LABEL_CONFLICT. The clean fixture has five rows; only the three holdout rows are evaluated with a harmless BLUE-TOKEN rule. Expected counts: TP=1, FP=0, TN=1, FN=1. Predict the four integrity scenarios and add a duplicate within one split. Explain why exact-hash grouping does not detect near duplicates or guarantee an independent holdout. The tiny toy corpus cannot estimate production performance. Requires YARA CLI for scanning; no real malware.

## Run
```bash
python3 labs/63-grouped-holdout-and-label-conflicts/evaluate.py
```
