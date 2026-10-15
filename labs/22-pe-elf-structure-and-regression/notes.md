# Day 22 — PE/ELF Format Detection, Structural Indicators and Regression

[English](notes.md) · [Türkçe](notes.tr.md)

This lab uses only harmless, authorized local training scenarios. It is not a production control or a real-world evidence conclusion.

## Objectives and connected topics

### 1. Magic bytes versus valid formats

Identify its trust boundary, input, expected behavior and common failure mode. Distinguish what the exercise observes from what it cannot prove.

Review prompt: Which negative test fails if this control is removed?

### 2. PE section conditions

Identify its trust boundary, input, expected behavior and common failure mode. Distinguish what the exercise observes from what it cannot prove.

Review prompt: Which negative test fails if this control is removed?

### 3. ELF structure and module checks

Identify its trust boundary, input, expected behavior and common failure mode. Distinguish what the exercise observes from what it cannot prove.

Review prompt: Which negative test fails if this control is removed?

### 4. String and structure composition

Identify its trust boundary, input, expected behavior and common failure mode. Distinguish what the exercise observes from what it cannot prove.

Review prompt: Which negative test fails if this control is removed?

### 5. Negative samples and false positives

Identify its trust boundary, input, expected behavior and common failure mode. Distinguish what the exercise observes from what it cannot prove.

Review prompt: Which negative test fails if this control is removed?

### 6. Rule regression and versioning

Identify its trust boundary, input, expected behavior and common failure mode. Distinguish what the exercise observes from what it cannot prove.

Review prompt: Which negative test fails if this control is removed?

## Local practical exercise

File: `rules.yar`

```bash
yara rules.yar samples/control.txt
yara rules.yar samples/fake-header.txt
```

## Experiment and negative-test plan

1. Run the baseline example and record output.
2. Identify an accepted input.
3. Construct a rejected input.
4. Test a boundary value.
5. Compare expected and actual outcomes.
6. State what remains unproven.
7. Locate the relevant code branch.
8. Change one control in a working copy.
9. Run the regression cases again.
10. Record tool version and artifact hashes.
11. Discuss a false-positive and false-negative scenario.
12. Prepare a short evidence-based report.

## Mini challenges

1. Add one new negative regression case.
2. Evaluate possible information leakage in error reporting.
3. Draw a concise trust-boundary diagram.

## Review questions

1. What is the principal trust boundary?
2. Which input is untrusted?
3. What does a positive case prove?
4. What does a negative case prove?
5. Describe a boundary value.
6. When is tool output insufficient evidence?
7. Give a false-positive example.
8. Give a false-negative example.
9. What production controls are absent?
10. Why record artifact hashes?
11. How do authentication and authorization differ?
12. What uncertainty remains?
13. What should an audit log contain?
14. Which sensitive data is unnecessary?
15. Which regressions must run after a change?
16. What is the key takeaway?

## Limitations

Passing a synthetic lab does not establish resilience to real attacks. Verify assumptions, permissions and environmental differences independently.
