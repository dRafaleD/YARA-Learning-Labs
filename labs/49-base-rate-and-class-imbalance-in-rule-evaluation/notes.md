# Lab 49 — Class Imbalance and Base Rates in YARA Rule Evaluation

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## From thresholds to prevalence
Lab 48 compared permissive and strict rule thresholds on a fixed corpus. Lab 49 shows why **class balance** matters. Even with similar false-positive behavior, precision can change sharply when actual positives are rare.

**Prevalence (base rate):** share of truly positive samples in the evaluated population.
**Precision (PPV):** TP / (TP + FP), or the share of alerts that are true positives.
**Recall (TPR):** TP / (TP + FN), or the fraction of positives caught.
**False-positive rate (FPR):** FP / (FP + TN), or the fraction of negatives incorrectly flagged.
If a denominator is zero, the metric is *undefined*, not zero.

## Fictional corpus and rules
No malware. The YARA rules only look for harmless `BLUE-TOKEN` and `GREEN-TOKEN` markers:
- `Training_Any_Token`: matches one or both markers, higher recall.
- `Training_Both_Tokens`: requires both, lower recall and fewer alerts.

Two positive fixtures contain both tokens or only BLUE. Eighteen negative fixtures contain three BLUE-only cases and fifteen plain-text cases. The **balanced** view evaluates the two positives plus the first two negatives; the **rare-positive** view uses all twenty records.

| Population | Rule | TP | FP | TN | FN | Precision | Recall |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Balanced (2/4 positive) | Any | 2 | 2 | 0 | 0 | 0.50 | 1.00 |
| Balanced | Both | 1 | 0 | 2 | 1 | 1.00 | 0.50 |
| Rare-positive (2/20) | Any | 2 | 3 | 15 | 0 | 0.40 | 1.00 |
| Rare-positive | Both | 1 | 0 | 18 | 1 | 1.00 | 0.50 |

These are **toy samples**, not realistic threat rates. The exact counts depend on deliberately chosen strings. A rule must be evaluated on independently labeled, representative holdout data before drawing deployment conclusions.

## Run
Requires the open-source YARA command-line tool in PATH:
~~~bash
python3 labs/49-base-rate-and-class-imbalance-in-rule-evaluation/evaluate.py
~~~
The script writes only temporary harmless text files and evaluates both rules with the real YARA CLI.

## Exercises
1. Compute precision and recall from a confusion matrix without reading the table.
2. Why does a low base rate make false positives costly?
3. What would change if all 18 negatives contained a single trigger token?
4. Why must the evaluation corpus be separate from the one used to design the rule?
5. Why does an alert or no alert never establish malware presence or absence?

## Safety and limits
No live malware, external systems or realistic signatures. Counts measure only the synthetic training corpus.
