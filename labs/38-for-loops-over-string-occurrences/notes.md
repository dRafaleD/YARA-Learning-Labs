# Lab 38 — for Loops over String Occurrences

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **for Loops over String Occurrences** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `#a` is the number of occurrences of `$a`, and `@a[i]` is the offset of the i-th occurrence (starting at 1).
2. `for any i in (1..#a) : ( @a[i] < 16 )` asks whether at least one occurrence is in the first 16 bytes.
3. Loops let one rule express position-based logic without separate strings.

## Important distinctions
- `for all` is stricter than `for any`; pick the one that matches your intent.
- Offsets are zero-based and in bytes.
- Test a hit at the start, a hit late in the file, and no hit at all.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/early.txt
~~~

~~~bash
yara rules.yar samples/late.txt
~~~

~~~bash
yara rules.yar samples/both.txt
~~~


## Assignments
1. Predict which sample matches.
2. Run the rule on each sample and record the result.
3. Change `any` to `all` and describe which sample stops matching.
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
