# Lab 28 — File Signatures, Offset Constraints and False Positive Control

[English](notes.md) · [Türkçe](notes.tr.md)

## Goal
Investigate file signatures, offset constraints and false positive control in a harmless, locally reproducible environment. Separate observations from conclusions and document limitations.

## Conceptual map
1. Controlled input and trust boundary
2. Static expectation and runtime behavior
3. Positive and negative case distinctions
4. False positives, false negatives and uncertainty
5. Defensive interpretation and validation

## Hands-on lab
Review `rules.yar` first, then execute from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/positive.bin
~~~

~~~bash
yara rules.yar samples/negative.bin
~~~

## Exercises
1. Predict output before executing.
2. Record actual output and tool versions.
3. Modify one harmless input and explain changes.
4. Add a negative regression test.
5. Identify what the observation does not prove.
6. Write a short report including source, command, date, findings and limitations.

## Mini challenge
Add one assertion for a key property and one test demonstrating a failure path.

## Review
1. Where is the trust boundary?
2. Which values come from the runtime environment?
3. Which inputs must be validated?
4. Why is a single match or event insufficient proof?
5. What additional production controls would you need?

## Safety
Use only local or explicitly authorized environments.
