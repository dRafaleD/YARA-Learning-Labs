# Lab 47 — Near-Duplicate Leakage in YARA Evaluation

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rule](rules.yar) · [Offline evaluator](evaluate.py)

## Connection to Lab 46
We split **training** from **holdout** data to measure generalization. But a split can still be misleading when essentially the **same sample appears in both groups** under different filenames or trivial metadata changes. That is called *data leakage*. Test results may look stronger because the allegedly unseen input is a copy of what informed development.

## How the small experiment works
Our synthetic YARA rule asks for both `DOC-CANARY` and `ACTION-CHECK`. The evaluator creates harmless text files in a temporary directory, applies the rule to each file, and computes TP/FP/TN/FN on labeled training and holdout examples.

One holdout positive is a near-duplicate of a training positive: it contains the same meaningful lines but changes the `case=` metadata. The script:
1. Checks **exact SHA-256 hashes** (identical file bytes).
2. Computes a **teaching-only normalized fingerprint**, ignoring `case=` metadata.
3. Reports when a normalized holdout fingerprint is present in the training group.
4. Compares raw holdout metrics to metrics after removing the known overlapping holdout item.

This demonstrates why **deduplication must happen before evaluating**. It is *not* a license to edit the test set after seeing results; in real research, document a predefined deduplication procedure and retain the untouched source data.

## Run locally
Install the YARA CLI. No malware, network connection or third-party services are required:
```bash
yara --version
python3 evaluate.py
```

The dataset is tiny and deliberately constructed. The code prints both confusion matrices and enforces expected counts with assertions. Zero denominators are reported as `undefined`, not silently treated as zero.

## Questions
1. Why doesn't merely putting files into different directories guarantee independence?
2. Why is an **exact** SHA-256 check insufficient for near-duplicate content?
3. What can go wrong if normalization removes meaningful differences or conflates different labels?
4. In real malware corpora, how might samples with common packers, templates or related families affect train/test separation?
5. Compare **deduplication**, **group-based splitting**, and **time-based holdouts**.
6. What fields should a reproducible evaluation report save (hashes, split policy, rule version, labels, tool version, limitations)?

## Safety and scope
The fingerprints are for synthetic documents, not authentic sample clustering. A YARA match is not proof of malware. Never infer field performance from this exercise.
