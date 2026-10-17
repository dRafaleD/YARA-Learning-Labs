# Lab 23 — ASCII and Wide String Detection with Regression Fixtures

[English](notes.md) · [Türkçe](notes.tr.md)

## Goal
Understand ascii and wide string detection with regression fixtures through a fully local, harmless experiment. Keep observation separate from inference.

## Core concepts
1. **ASCII versus UTF-16LE** — document the boundary, expected behavior and limitations.
2. **ascii and wide modifiers** — document the boundary, expected behavior and limitations.
3. **byte-level verification** — document the boundary, expected behavior and limitations.
4. **false positives and false negatives** — document the boundary, expected behavior and limitations.
5. **independent indicators** — document the boundary, expected behavior and limitations.
6. **negative sample regression** — document the boundary, expected behavior and limitations.

## Procedure
The included `encoding_rules.yar` is a synthetic training example. From the lab directory:

```bash
python3 make_samples.py
```

```bash
yara encoding_rules.yar samples/ascii.txt
```

```bash
yara encoding_rules.yar samples/wide.bin
```

```bash
yara encoding_rules.yar samples/negative.txt
```

**Expected:** ASCII and UTF-16LE positive fixtures match; negative fixture does not.

## Observations to record
Write down the machine/tool versions, exact command, input, actual output, unexpected behavior, and interpretation. Explain which results are facts and which remain hypotheses.

## Exercises
1. Run the baseline and save the observed output.
2. Change one harmless input and predict what happens before running.
3. Add a negative test and distinguish a rejection from a failure to observe.
4. Restore the original, rerun it, and explain why regression tests matter.
5. Identify two realistic false-positive explanations.
6. Identify a useful independent corroborating observation.
7. Draft a short report stating limitations explicitly.

## Review questions
1. What does ASCII versus UTF-16LE mean, why does it matter, and what does it not guarantee?
2. What does ascii and wide modifiers mean, why does it matter, and what does it not guarantee?
3. What does byte-level verification mean, why does it matter, and what does it not guarantee?
4. What does false positives and false negatives mean, why does it matter, and what does it not guarantee?
5. What does independent indicators mean, why does it matter, and what does it not guarantee?
6. What does negative sample regression mean, why does it matter, and what does it not guarantee?
7. What would improve the confidence of your result?
8. Which regression test should be automated first?

## Ethics and scope
Use only locally generated data and infrastructure you own or are authorized to study. Findings from an individual signal are not proof of an incident.
