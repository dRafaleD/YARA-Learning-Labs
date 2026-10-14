# Lab 20 — Detection Metrics, Corpus Labels and Regression Testing

[English](notes.md) · [Türkçe](notes.tr.md)

**Goal:** connect Labs 18–19's detection-quality ideas to measurable and reproducible regression testing.

Prerequisites: Python 3.9+ and YARA CLI. Only harmless generated text files are used.

## 1. Ground truth must be explicit

Testing requires labels that are defined before running the rule. Our fixture manifest records intended positives and negatives. Labels describe only this invented training problem and are not real-world analyst verdicts.

## 2. Confusion matrix

True positive means an intended positive matched; false positive is a labeled negative matching; false negative is an intended positive missed; true negative is a negative correctly ignored. Counts depend on the defined evaluation set.

## 3. Precision versus recall

Precision is TP/(TP+FP); recall is TP/(TP+FN). If a denominator is zero, the ratio is undefined rather than automatically perfect. Precision answers how often alerts are correct within the dataset; recall answers how much labeled-positive coverage we achieved.

## 4. Broad markers and alert noise

A rule that only searches LAB20_SIGNAL will match benign training notes that mention the marker. This creates measurable false positives. Broad indicators can be useful for exploration, but do not equate their alerts with strong detection.

## 5. Contextual conditions

The stricter rule requires marker, component and active mode within a bounded file. This improves precision in our dataset. It might miss variants lacking those fields. More conditions improve a narrow test result, not universal detection quality.

## 6. Regression testing

Every rule edit must be tested against positives, benign negatives and near-misses. The script exits nonzero if expected strict-rule counts change. Automating the test reduces accidental rule drift, while representative real corpora remain necessary before deployment.

## 7. Dataset leakage

If every positive sample contains the same artificial string, a rule can overfit it and appear perfect. Independent sources, families, versions and benign backgrounds are needed for realistic validation. Here overfitting is intentionally visible.

## 8. Measurement limitations

A tiny synthetic corpus produces easy-to-understand metrics, not a deployable confidence estimate. Define scope, version, YARA engine, labels and procedure whenever reporting precision or recall.

## 9. Investigation workflow

A YARA match should trigger triage and contextual investigation, not an automatic malware verdict. Preserve artifact hashes, explain matching strings and correlate with file format, origin, behavior and other evidence.

## 10. CI discipline

A simple CI job could install an explicit YARA version and invoke the regression script; lock dependencies and store results. Avoid publishing real suspicious files. Keep corpus labels under version control.

## Local test

From this directory:

```bash
python3 generate_corpus.py
yara --version
yara -s test_rules.yar samples/positive-01.txt
yara -s test_rules.yar samples/negative-marker.txt
python3 evaluate_rules.py
```

The generator creates 3 labeled positives, 5 labeled negatives, plus `labels.json`. The evaluator invokes installed YARA, computes TP/FP/TN/FN for both rules and exits nonzero if the strict-rule regression fails. It reports missing YARA clearly.

### Expected matrix on the synthetic corpus

| Rule | TP | FP | TN | FN |
| --- | ---: | ---: | ---: | ---: |
| Lab20_Contextual_Detection | 3 | 0 | 5 | 0 |
| Lab20_Broad_Marker | 3 | 2 | 3 | 0 |

These are **not** real-world malware detection rates; they describe exactly eight fabricated training samples.

## Mini challenges

1. Change mode=active to mode=idle in a positive sample. Decide whether to relabel it, and observe the regression failure.
2. Add a second independent signal to the broad rule and measure its false-positive/recall trade-off.
3. Add a benign near miss and update the labels manifest; rerun the regression script.
4. Extend the evaluator with F1, retaining undefined-denominator handling.

## Exercises

1. Inspect both YARA rules.
2. Generate the corpus.
3. Hash each fixture with SHA-256.
4. Read the JSON labels.
5. Scan a positive with each rule.
6. Find the broad-rule false positives.
7. Calculate the confusion matrix by hand.
8. Calculate precision.
9. Calculate recall.
10. Run the automated regression.
11. Add a novel benign variant.
12. Document detection limitations in five sentences.

## Review questions

1. What is ground truth?
2. Define TP.
3. Why are false positives costly?
4. Why can false negatives be dangerous?
5. What is a true negative?
6. Precision formula?
7. Recall formula?
8. What if the denominator is zero?
9. What is corpus overfitting?
10. When is a broad indicator acceptable?
11. Why regression testing?
12. Why does corpus representativeness matter?
13. Why is a YARA match not proof of malware?
14. Why record the rule commit?
15. What is needed before production deployment?

**Takeaway:** Detection quality requires labeled data, repeatable measurement and clearly documented limitations, not merely a syntactically valid matching rule.
