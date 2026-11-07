# Day 44 — YARA Regression with Negative Corpus and Near Misses

[English](notes.md) · [Türkçe](notes.tr.md) · [Practical](rules.yar)

## Learning objective

This exercise uses only harmless, authorized local samples to study **YARA Regression with Negative Corpus and Near Misses**. Distinguish direct observations from unsupported conclusions.

## Core concepts

1. Rule testing needs positive and negative fixtures; a detection without negative controls cannot estimate false positives.

2. A near-miss example is deliberately similar to a positive but should not satisfy the rule.

3. Precision and recall depend on the labeled dataset; toy corpus results cannot establish real malware detection quality.

## Hands-on

Read the source and predict the output before running:

```bash
python fixtures.py && yara rules.yar samples/positive.txt && yara rules.yar samples/near_miss.txt
```

Generate synthetic corpus with `fixtures.py`. Positive must match; near_miss and negative must not.

## Assignments

1. Compare expected and observed results.
2. Document one positive and one negative case.
3. Explain why a single indicator cannot establish intent or safety.
4. Change a harmless boundary input and repeat the test.

## Knowledge check

- Which trust boundary is relevant?
- Which evidence may be missing or misleading?
- What independent validation would production require?

## Safety and limitations

No live malware, unauthorized systems or offensive targets. This toy exercise is not a production detector or safety guarantee.
