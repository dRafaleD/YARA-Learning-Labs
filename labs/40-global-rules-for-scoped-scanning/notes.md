# Lab 40 — Global Rules for Scoped Scanning

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Global Rules for Scoped Scanning** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A `global rule` is evaluated for every file, and the other rules in the same set can match only if all global rules are satisfied.
2. It is a clean place for scope limits such as a maximum file size that should apply to every rule.
3. A global rule appears in the match list itself, so read the output as a filter result plus the rule that matched.

## Important distinctions
- A global rule changes every rule in the file; document it prominently.
- Test a small file and a large file with the same marker.
- Do not place unrelated scope conditions in the same ruleset by accident.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/small_marker.txt
~~~

~~~bash
yara rules.yar samples/large_marker.txt
~~~


## Assignments
1. Predict which sample matches.
2. Run the ruleset on both samples and record the result.
3. Remove the `global` keyword and describe what changes.
4. Add an assertion for one security property.
5. Describe a negative case and a potential false positive.
6. Propose an independent corroboration method.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
