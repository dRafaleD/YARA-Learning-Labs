# Lab 36 — Cheap Conditions First: filesize and Header Gates

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Cheap Conditions First: filesize and Header Gates** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Put cheap checks such as `filesize` and a header comparison before string conditions so most files are rejected quickly.
2. `uint16(0) == 0x5A4D` reads the first two bytes and tests for the `MZ` header.
3. A gate narrows the rule's scope, so test both the gated file and the same marker without the gate.

## Important distinctions
- Order affects speed, not the result of the logical expression.
- A header gate hides the marker in non-MZ files by design.
- Measure on a real corpus before claiming a speedup.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/mz_with_marker.bin
~~~

~~~bash
yara rules.yar samples/text_with_marker.txt
~~~

~~~bash
yara rules.yar samples/mz_without_marker.bin
~~~


## Assignments
1. Predict which sample matches.
2. Run the rule on every sample and record the result.
3. Move the string check first and confirm the matches stay the same.
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
