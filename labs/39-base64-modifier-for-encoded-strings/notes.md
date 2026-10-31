# Lab 39 — The base64 Modifier for Encoded Strings

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **The base64 Modifier for Encoded Strings** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `$s = "text" base64` matches the string as it would appear Base64-encoded at any of the three possible alignments.
2. The modifier generates the encoded variants for you, so the rule stays readable.
3. Also keep a plain `ascii` variant if you want to catch both forms.

## Important distinctions
- The modifier matches only standard Base64, not custom alphabets or other encodings.
- Short strings give many accidental matches after encoding.
- A match shows the encoded text exists, not that anything decodes or uses it.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/b64.txt
~~~

~~~bash
yara rules.yar samples/plain.txt
~~~

~~~bash
yara rules.yar samples/unrelated.txt
~~~


## Assignments
1. Predict which samples match.
2. Run the rule on each sample and record the result.
3. Add a hex-encoded sample and explain why it does not match.
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
