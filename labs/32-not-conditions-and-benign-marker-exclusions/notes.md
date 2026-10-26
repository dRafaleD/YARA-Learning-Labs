# Lab 32 — not Conditions and Benign-Marker Exclusions

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **not Conditions and Benign-Marker Exclusions** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `not $benign` makes a rule fail when a marker string that identifies known-good files is present.
2. Exclusions cut false positives but add a bypass: an attacker who plants the marker evades the rule.
3. Pair exclusions with a second independent signal and test the excluded case explicitly.

## Important distinctions
- A benign marker proves nothing about the rest of the file; it is only a convention.
- Keep the exclusion as narrow as possible, for example tied to a header or a file size range.
- Document why each exclusion exists so it can be removed when it stops being true.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/suspicious.txt
~~~

~~~bash
yara rules.yar samples/suspicious_with_benign.txt
~~~

~~~bash
yara rules.yar samples/benign_only.txt
~~~


## Assignments
1. Predict which of the three samples the rule matches.
2. Run the rule against each sample and record the result.
3. Remove the `not $benign` clause and describe which sample starts matching.
4. Add a test that proves a file carrying only the benign marker does not match.
5. Describe how an attacker could abuse the exclusion and one way to harden it.
6. Propose an independent check, such as a hash allow-list or a signed-file check.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
