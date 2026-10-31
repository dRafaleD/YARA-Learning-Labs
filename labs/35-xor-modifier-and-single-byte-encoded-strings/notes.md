# Lab 35 — The xor Modifier and Single-Byte Encoded Strings

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **The xor Modifier and Single-Byte Encoded Strings** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. `$s = "text" xor` matches the string encoded with any single-byte XOR key from 0 to 255.
2. `xor(0x01-0xff)` excludes the zero key, which would otherwise match the plain string as well.
3. Short strings produce many accidental matches across all 256 keys, so keep them long and distinctive.

## Important distinctions
- xor handles single-byte keys only; multi-byte keys, rolling XOR and other encodings need different approaches.
- A match shows the encoded string is present, not what the program does with it.
- Test with the plain, encoded and unrelated samples so you know the rule's boundaries.

## Hands-on lab
Read `rules.yar` before running the following from this lab folder:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/plain.txt
~~~

~~~bash
yara rules.yar samples/xor_0x41.bin
~~~

~~~bash
yara rules.yar samples/unrelated.txt
~~~


## Assignments
1. Predict which of the three samples the rule matches.
2. Run the rule against each sample and record the result.
3. Change the modifier to `xor(0x01-0xff)` and describe which sample stops matching.
4. Add a sample encoded with a two-byte key and explain why the rule misses it.
5. Describe a false-positive risk for a very short xor string.
6. Propose an independent check, such as entropy or a decoded-content scan.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
