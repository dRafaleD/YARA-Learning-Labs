# Lab 18 Runbook

## Prepare

```bash
python3 create_samples.py
yara --version
```

## Focused tests

```bash
yara test_rules.yar samples/positive-contextual.txt
yara test_rules.yar samples/negative-common-error.txt
yara test_rules.yar samples/negative-marker-only.txt
yara test_rules.yar samples/threshold-positive.txt
yara test_rules.yar samples/threshold-negative.txt
```

## Corpus test

```bash
yara -r test_rules.yar samples/benign-corpus/
```

Record how many files match the broad rule.

## Timing exercise

Use your shell's timing command on the same local corpus:

```bash
time yara -r test_rules.yar samples/benign-corpus/
```

Timing results depend on machine, YARA version, filesystem cache, and corpus size. Treat them as local observations, not universal benchmarks.
