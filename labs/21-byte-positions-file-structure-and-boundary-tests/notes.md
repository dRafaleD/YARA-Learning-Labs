# Day 21 — Byte Positions, File Structure and Boundary-Case Testing

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

This hands-on day builds on earlier labs, using only local harmless training data. Verify assumptions, distinguish observation from inference, and do not treat tool output as automatic security proof.

## Learning objectives

- Offset-sensitive detection
- Bounded region
- Size gates
- Boolean composition
- Positive and negatives
- Matching evidence
- Regression automation
- Portability

## Data flow and threat model

```text
controlled training input
        ↓
parser / evaluator / analyst
        ↓
security or evidence check
        ↓
observable result
        ↓
review assumptions and limits
```

## 1. Offset-sensitive detection

Use header at 0 instead of searching anywhere; compare against shifted-header samples.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 2. Bounded region

The section marker must occur in the defined offset window, not arbitrarily late.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 3. Size gates

Test minimum and maximum boundaries and why filesize alone never proves format validity.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 4. Boolean composition

Combine header, section and version markers to reduce accidental matches.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 5. Positive and negatives

Record explicit expected outcomes for valid, shifted, truncated and missing-section samples.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 6. Matching evidence

Inspect matching string offsets with yara -s and distinguish observed match from maliciousness.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 7. Regression automation

Run all cases after editing conditions; fail tests if actual result differs from expectation.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 8. Portability

Record YARA version and command line; synthetic signatures are educational only.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## Local exercise

Use only the files in this repository. This example is not a production security service.

```bash
python3 create_samples.py
yara -s test_rules.yar samples/positive.txt
yara test_rules.yar samples/late-header.txt
python3 verify_samples.py
```

## Test matrix

| Scenario | Expected | Reason |
|---|---|---|
| Valid training input | Accept / match | Baseline |
| Wrong owner or header | Reject / no match | Scope / structure |
| Truncated or missing field | Controlled failure | Input validation |
| Unrelated benign sample | No accidental claim | False-positive awareness |

## Exercises

1. Run and record the example.
2. Write an initial hypothesis.
3. Verify the positive case.
4. Add one negative case.
5. Add another negative case.
6. Test a boundary value.
7. Find the responsible source-level check.
8. Separate observations from inferences.
9. Change one control in a working copy.
10. Rerun the whole test matrix.
11. Document limitations.
12. Write a one-page analysis report.

## Review questions

1. What is the primary trust boundary?
2. Which inputs are untrusted?
3. What does the positive test establish?
4. What does the negative test establish?
5. What does the observed output support?
6. What does it not support?
7. Which input is the most important?
8. Give an example boundary value.
9. What is fail-closed behavior?
10. Why is the demo not production-ready?
11. Describe one potential false positive.
12. Describe one potential false negative.
13. Which fields belong in an audit log?
14. What personal data is unnecessary?
15. Why record tool versions?
16. Which regressions need retesting?

## Mini challenges

1. Add a new negative test and document its expected and actual results.
2. Break one assumption in a working copy and identify which test catches it.
3. Write a short report containing source, hash, tool version, command, observation and limitations.

## Takeaway

Measure actual behavior rather than overgeneralizing from synthetic cases. Security decisions, authorization and forensic inferences require independent checks.
