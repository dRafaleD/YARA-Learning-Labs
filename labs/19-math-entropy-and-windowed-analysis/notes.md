# Lab 19 — YARA Math Module: Entropy, Byte Windows and Detection Confidence

[English](notes.md) · [Türkçe](notes.tr.md)

## Objective

Build on Lab 18's false-positive and testing work with **three connected skills**: byte-distribution/entropy analysis, structural **windowed conditions**, and a reproducible positive/negative test matrix. All files are harmless synthetic binaries.

**Main warning:** High entropy is not a malware verdict. Compression, encryption, images and entirely benign data can also produce high-entropy bytes.

## 1. What is byte entropy?

Shannon entropy describes uncertainty in a distribution. For byte values `0..255`, entropy is commonly reported in **bits per byte**, between 0 and 8:

```text
H = - Σ p(byte) × log₂(p(byte))
```

- A region full of the same byte, such as `AAAA...`, has entropy close to **0**.
- A roughly uniform distribution of all 256 byte values approaches **8**.
- A short sample is noisy: measured entropy depends on sample size and distribution.

**Entropy describes byte statistics, not intent.** It cannot tell you whether a region is encrypted, compressed, malicious, or harmless by itself.

## 2. Why analysts check local regions

A binary may contain low-entropy text, zero-filled padding and high-entropy assets in the **same file**. A single full-file score hides these differences.

```text
offset 0           256                4352               8448
| header + padding | first 4096 bytes | second 4096 bytes |
```

In our fixtures, every file starts with an artificial marker `LAB19_DEMO` and a padded header. The first measurement window starts at byte 256 and is 4096 bytes long. The mixed fixture adds a second window beginning at byte 4352.

You should be able to explain **why offset and size matter** before writing an entropy rule.

## 3. YARA math module

YARA's `math` module exposes functions for basic statistical analysis. Import it explicitly:

```yara
import "math"
```

This lab uses:

```yara
math.entropy(256, 4096)
```

where `256` is the **byte offset**, and `4096` is the **number of bytes** to analyze. It is not a percentage and does not refer to 4096 bytes from the end.

Before reading that region, check that `filesize` is sufficiently large. A rule should express its expected file boundaries.

## 4. Condition quality, not magic thresholds

The lab's high-entropy rule combines:

1. a synthetic header at offset 0;
2. a bounded filesize (4352 bytes to 20 KiB);
3. entropy above **7.5** in the first 4096-byte window.

The header intentionally distinguishes our fixtures from arbitrary documents, and the window makes the measurement interpretable. **7.5 is a teaching threshold**, not a validated production malware threshold.

The low-entropy rule uses `math.entropy(256,4096) < 1.0`. The third rule examines a second window of the mixed fixture.

These rules describe patterns in our training corpus only.

## 5. Build the sample corpus

From this lab directory:

```bash
python3 generate_samples.py
```

The script uses Python's standard library only and creates:

```text
samples/low-entropy.bin
samples/high-entropy.bin
samples/mixed-entropy.bin
```

The high-entropy region is produced deterministically from SHA-256 digest blocks. The bytes are **not secret** and this is not an encryption workflow.

Sample metrics should be roughly:

| Fixture | Bytes | Window at 256 | Window at 4352 |
| --- | ---: | --- | --- |
| low-entropy.bin | 4352 | ~0 | absent |
| high-entropy.bin | 4352 | ~7.9 | absent |
| mixed-entropy.bin | 8448 | ~0 | ~7.9 |

The generator prints actual computed entropy; use those numbers rather than assuming this table is exact.

## 6. Run YARA

Requires a YARA CLI with the `math` module:

```bash
yara --version
yara test_rules.yar samples/low-entropy.bin
yara test_rules.yar samples/high-entropy.bin
yara test_rules.yar samples/mixed-entropy.bin
```

Use `-s` to inspect which **string** contributed to a match:

```bash
yara -s test_rules.yar samples/high-entropy.bin
```

Note: `-s` prints string evidence such as the marker. It does **not** display an entropy calculation as a matched string. Use the Python generator's entropy output to compare numerical results.

## 7. Expected match matrix

| Fixture | High first window | Low first window | High second window |
| --- | --- | --- | --- |
| low-entropy.bin | No | Yes | No |
| high-entropy.bin | Yes | No | No |
| mixed-entropy.bin | No | Yes | Yes |

This matrix is an expected result for our generated files and rules—not a detection claim for unknown binaries.

## 8. Repeatable smoke test

```bash
python3 run_tests.py
```

The test script rebuilds fixtures, invokes the installed `yara` CLI and compares rule names **exactly** with the expected sets. A missing YARA executable produces a clear error. Save YARA version, source commit and test output with any detection report.

## 9. What can go wrong?

### False positives
Many benign formats have high entropy; matching only `math.entropy(...) > threshold` against arbitrary files generates weak signals.

### False negatives
An indicator stored in a different region can be missed by a fixed-offset rule. An entropy threshold can also be too strict for genuine variants.

### Small sample bias
Entropy estimates from a tiny region fluctuate; don't compare 16-byte and 4096-byte windows as if the results had equal statistical significance.

### Whole file vs window
A high-entropy section may be diluted by low-entropy padding in whole-file entropy. Conversely, a uniformly high file does not prove packing.

### Computational cost
Calculate statistics over bounded windows when appropriate. Performance and coverage should be measured, not assumed.

## 10. Relationship to Reverse Engineering

In Ghidra, identify a file's sections or meaningful byte ranges first. Ask whether an entropy spike corresponds to a resource, an archive, a compressed payload, embedded data, or simply a benign implementation choice. Combine entropy with **file format, imports, strings, execution behavior and context** before making a conclusion.

## Mini challenges

1. **Shifted region:** Modify the mixed fixture so its high-entropy block begins 512 bytes later. Adjust one YARA offset; explain the former false negative.
2. **Threshold experiment:** Change 7.5 to 7.99. Which generated files match? Why is a single threshold fragile?
3. **Short windows:** Compare entropy for windows of 32, 256 and 4096 bytes; explain sample-size effects.
4. **Counterexample:** Generate a benign compressed file (using Python `zlib`) and measure its entropy. Explain why entropy is not a malware label.

## Exercises

1. Generate the fixtures and note sizes.
2. Verify the 256-byte prefix.
3. Inspect `test_rules.yar` and identify all three guards.
4. Run each YARA rule against each fixture.
5. Verify expected match matrix.
6. Run `yara -s` and explain why entropy is not printed as a string match.
7. Run the smoke test.
8. Change the window size on a working copy.
9. Add a new near-miss fixture with the marker but only 512 bytes.
10. Confirm filesize excludes that fixture.
11. Compare full-file and first-window entropy in Python.
12. Document limitations and rule version.

## Review questions

1. What is Shannon entropy?
2. What do values near 0 and 8 suggest?
3. Does high entropy mean malware?
4. What does `math.entropy(offset,size)` measure?
5. Why require filesize bounds?
6. Why combine a marker with entropy?
7. Why might whole-file entropy mislead?
8. How can fixed offsets cause false negatives?
9. Why are small windows less reliable?
10. What does YARA `-s` reveal?
11. What makes a test corpus reproducible?
12. How would you correlate an entropy result with static/dynamic RE?

## Main takeaway

**Entropy is a supporting statistical feature.** A useful YARA rule depends on contextual indicators, known bounds, measured thresholds and tests against realistic benign and target material.
