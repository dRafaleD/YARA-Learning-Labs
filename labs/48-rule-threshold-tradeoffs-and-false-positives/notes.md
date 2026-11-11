# Lab 48 — YARA Thresholds, Recall and False Positives

[English](notes.md) · [Türkçe](notes.tr.md) · [Rules](rules.yar) · [Offline evaluator](evaluate.py)

## Why thresholds matter
Lab 47 exposed near-duplicate leakage between training and holdout sets. After fixing evaluation hygiene, another design choice remains: **how many independent-looking strings should a rule require?** A broad rule may find more positives but generate false alerts; a strict rule may reduce false alerts yet miss positives. More conditions do not magically prove maliciousness.

## The synthetic rule family
Every fixture is a harmless text document containing some of the markers BLUE-TOKEN, GREEN-TOKEN and ORANGE-TOKEN. The rules are variants of the *same indicator family*:
- **Any-marker:** 1 of the 3 strings.
- **Two-marker:** at least 2 strings.
- **All-marker:** all 3 strings.

Two documents are labeled positive for the **fictional test concept**. Three documents are negative, including one negative that deliberately contains two indicators. We test all three rules on the **same** fixed cases.

## Interpreting results
A positive means the fixture label was defined as positive for this exercise; it **does not** mean malware.

- Any-marker: TP=2 FP=2 TN=1 FN=0.
- Two-marker: TP=2 FP=1 TN=2 FN=0.
- All-marker: TP=1 FP=0 TN=3 FN=1.

Precision = TP/(TP+FP), recall = TP/(TP+FN). A zero denominator should be reported as undefined. The counts illustrate tradeoffs only; tiny, deliberately constructed corpora do **not** measure general-world detection quality.

## Run
Install the official YARA command-line program first, then run:

~~~bash
yara --version
python3 evaluate.py
~~~

The Python script creates five temporary synthetic files, runs all three rules against every file, prints TP/FP/TN/FN, precision and recall, and checks the expected matrices with assertions. All sample material is deleted when the script ends.

## Tasks
1. Explain why the two-marker rule has a false positive on this corpus.
2. If the all-marker rule has the highest measured precision, why isn't it automatically the best deployment choice?
3. Add a negative file with all three markers. How do the three precision values change?
4. Add a positive file with one marker. Which rules lose recall?
5. Design train/validation/holdout splits **before** tuning thresholds; document label provenance, family grouping and rule versions.
6. Which extra signals beyond strings (file format, offsets, source and behavior) could improve an investigation without making a match equal a verdict?

## Safety
No malware files, attacker infrastructure, network traffic or malicious payloads. Rule hits are evidence of matching patterns only. This lab is a reproducible *teaching* experiment, not a detection benchmark.
