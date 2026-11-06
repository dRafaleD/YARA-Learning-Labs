# Lab 43 — The fullword Modifier and Word Boundaries

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **The fullword Modifier and Word Boundaries** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `fullword` makes a string match only when it is not surrounded by alphanumeric characters.
2. It removes matches where the string is just a part of a longer word.
3. Underscores and punctuation count as boundaries only if they are not alphanumeric, so test the edge cases.

## Important distinctions
- `fullword` reduces false positives but can also hide a real match inside a longer token.
- Test a standalone word, a word inside a longer word and a word next to punctuation.
- Document why the boundary matters for this string.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/standalone.txt
~~~

~~~bash
yara rules.yar samples/embedded.txt
~~~

~~~bash
yara rules.yar samples/punctuated.txt
~~~


## Assignments
1. Predict which samples match.
2. Run the rule on each sample and record the result.
3. Remove `fullword` and describe which sample starts matching.
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
