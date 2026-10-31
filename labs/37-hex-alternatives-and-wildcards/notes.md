# Lab 37 — Hex Alternatives and Wildcards

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Hex Alternatives and Wildcards** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `( 41 | 42 )` matches one of the listed byte values at that position.
2. `??` matches any single byte, which tolerates a value that changes between builds.
3. Every wildcard widens the rule, so keep the fixed bytes long enough to stay distinctive.

## Important distinctions
- A wildcard that covers the only variable byte is fine; one that covers most of the pattern is not.
- Alternatives multiply the number of patterns the engine must check.
- Test a matching sample, a near miss and an unrelated file.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/match_a.bin
~~~

~~~bash
yara rules.yar samples/match_b.bin
~~~

~~~bash
yara rules.yar samples/near_miss.bin
~~~


## Assignments
1. Predict which samples match.
2. Run the rule on each sample and record the result.
3. Allow a third alternative and add a sample that proves it.
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
