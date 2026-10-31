# Lab 41 — Integer Reads and Endianness

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Integer Reads and Endianness** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `uint32(0)` reads four bytes at offset 0 as little-endian, while `uint32be(0)` reads them as big-endian.
2. The bytes `4C 41 42 34` read little-endian give `0x3442414C`, and read big-endian give `0x4C414234`.
3. Pick the form that matches how the file format documents its fields.

## Important distinctions
- Reading beyond the end of a file yields an undefined value and the condition fails; check `filesize` too.
- The ASCII text is the same either way; only the number differs.
- Write the constant in hex so the bytes stay readable.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/lab4.bin
~~~

~~~bash
yara rules.yar samples/short.bin
~~~


## Assignments
1. Predict which of the three rules match the sample.
2. Run the ruleset on both samples and record the results.
3. Swap the constants between the two rules and explain the result.
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
