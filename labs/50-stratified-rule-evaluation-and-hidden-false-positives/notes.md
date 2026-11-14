# Lab 50 — Stratified YARA Evaluation and Hidden False Positives

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## Day 49 follow-up
Class prevalence changes precision. Another problem: an **overall score** can hide weak performance for a subgroup. **Stratification** means reporting a separate confusion matrix for each meaningful category.

The synthetic corpus has alpha and beta groups. Two harmless YARA rules match either of two colored text tokens, or both tokens. In alpha, the permissive rule yields TP=2, FP=1, TN=1, FN=0; in beta, TP=2, FP=3, TN=1, FN=0. The stricter rule gets TP=1, FP=0 in both groups, but misses one positive per group.

## Run
Requires the `yara` command in PATH:
```bash
python3 labs/50-stratified-rule-evaluation-and-hidden-false-positives/evaluate.py
```
The evaluator creates temporary harmless text and uses the real YARA CLI. No malware is included.

## Exercises
Why might pooled precision hide a noisy subgroup? What changes when categories have different sizes? How would you avoid group leakage between training and evaluation? What is a suitable independent holdout set?

## Limits
Deliberately tiny, fictional corpus. This is an evaluation-method lesson, not a claim about production detection performance.
