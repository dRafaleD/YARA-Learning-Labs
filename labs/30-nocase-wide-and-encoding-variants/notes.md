# Lab 30 — nocase, wide and Encoding Variants in YARA

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **nocase, wide and Encoding Variants in YARA** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `nocase` ignores letter case; `wide` matches UTF-16LE text such as Windows strings.
2. Each modifier widens a rule; measure the false positives it adds.
3. The near-miss sample `LAB30-MARKER` must not match; confirm it with a negative test.

## Important distinctions
- Finding an indicator does not validate every inference about it.
- Identify the trust boundary and the party controlling each input.
- Use both positive and negative cases; document measurement limitations.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/ascii_upper.txt
~~~

~~~bash
yara rules.yar samples/wide.bin
~~~

~~~bash
yara rules.yar samples/near_miss.txt
~~~

## Assignments
1. Predict the output from the code.
2. Run the program and record inputs and outputs.
3. Change a harmless input and explain the resulting difference.
4. Add an assertion for one security property.
5. Describe a negative case and a potential false positive.
6. Propose an independent corroboration method.

## Knowledge check
1. Where does the input originate?
2. What was directly observed?
3. What assumptions might fail in production?
4. Which evidence would be insufficient?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
