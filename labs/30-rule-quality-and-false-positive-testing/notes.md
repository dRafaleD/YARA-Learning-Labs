# Lab 30 — Measuring YARA Rule Quality with Synthetic Samples

[English](notes.md) · [Türkçe](notes.tr.md)

## Objective
Evaluate a YARA rule with labeled *benign synthetic* files rather than relying on a single match. Learn true positives (TP), false positives (FP), true negatives (TN), and false negatives (FN).

## Important ideas
- A string match is not proof of malware. An indicator may exist in harmless documentation.
- Precision = TP/(TP+FP), recall = TP/(TP+FN). When a denominator is zero, report the metric as undefined.
- Sample selection influences measured accuracy. These toy samples do not predict real-world performance.
- Conditions like `uint16(0) == 0x5A4D` assume a specific byte format; use only if justified.

## Hands-on
Install YARA CLI separately. In this directory:

```bash
python3 make_samples.py
yara rules.yar samples/positive_1.txt
yara rules.yar samples/negative_1.txt
python3 evaluate.py
```

The evaluator calls the installed YARA CLI and reports a confusion matrix, precision, and recall. No real malware is required.

## Assignment
1. Explain why `negative_2.txt` is a near miss.
2. Tighten or loosen the rule; record how TP/FP/FN/TN change.
3. Add at least two new labeled test files.
4. Discuss whether a small curated dataset supports deployment claims.

## Limits
Only authorized, harmless text files. Never claim this rule detects real malware families.
