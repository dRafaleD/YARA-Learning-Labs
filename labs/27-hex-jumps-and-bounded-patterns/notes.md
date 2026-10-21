# Lab 27 — Hex Patterns, Bounded Jumps and Negative Testing

[English](notes.md) | [Türkçe](notes.tr.md)

## Objective
Study bounded hexadecimal jumps, offsets, near misses, and why generic signatures can be noisy. Keep observation, inference, assumptions and uncertainty separate.

## Core concepts
- Predict expected behavior and record a baseline.
- Identify trusted inputs and validation boundaries.
- Change one variable, then compare results.
- Consider negative cases, false positives and false negatives.
- Record commands, versions, outputs and limitations.

## Local practice
```bash
python3 fixtures.py
```

```bash
yara bounded.yar samples/match.bin
```

```bash
yara bounded.yar samples/no_match.bin
```

## Exercises
1. Predict output from the source code.
2. Run each command and record actual output.
3. Change a harmless input.
4. Compare positive and negative tests.
5. Propose an independent validation method.
6. Write a short findings and limitations report.

## Mini challenge
Add an automated regression assertion for one property and explain what it detects.

## Review questions
1. Where is the trust boundary?
2. Which result is observed versus inferred?
3. Why is negative testing useful?
4. How might versions or environment change results?
5. What additional production controls are needed?

## Safety
Use only local or authorized systems.
