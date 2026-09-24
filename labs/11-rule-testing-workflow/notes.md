# Lab 11 — Rule Testing Workflow

## Goal

Build a small repeatable workflow for testing YARA rules with harmless positive and negative samples.

Previous labs focused mainly on writing conditions. This lab focuses on a different question:

> How do we check that a rule matches what we expect without matching everything else?

## Files

```text
11-rule-testing-workflow/
├── notes.md
├── test_rules.yar
└── samples/
    ├── match-marker.txt
    ├── match-two.txt
    └── no-match.txt
```

All samples are plain harmless text created specifically for this exercise.

## Rule 1 — exact marker

```yara
rule Lab11_Exact_Marker
{
    strings:
        $marker = "YARA_LAB_11_MARKER"

    condition:
        $marker
}
```

Expected behavior:

- `match-marker.txt` → match
- `match-two.txt` → no match
- `no-match.txt` → no match

Run:

```bash
yara test_rules.yar samples/match-marker.txt
yara test_rules.yar samples/no-match.txt
```

## Rule 2 — two indicators

The second rule contains:

```yara
condition:
    all of them
```

Both strings must exist in the same scanned file.

Expected behavior:

- `match-two.txt` → match
- `match-marker.txt` → no match
- `no-match.txt` → no match

## Scan the sample directory

YARA can recursively scan the directory:

```bash
yara -r test_rules.yar samples/
```

Now compare the output with the expected results above.

## Positive and negative tests

A **positive test** is a sample that should match.

A **negative test** is a sample that should not match.

Both matter.

If we test only positive samples, we learn whether a rule can detect something, but not whether it is too broad.

For example, changing:

```yara
all of them
```

to:

```yara
any of them
```

makes the second rule less strict. Testing both matching and non-matching files helps us see the effect.

## Useful command

To display matching strings:

```bash
yara -s test_rules.yar samples/match-two.txt
```

This is useful while learning because it shows which string identifiers produced the match.

## Testing checklist

Before considering a practice rule finished:

1. Does the intended sample match?
2. Do unrelated samples stay unmatched?
3. Which string or condition caused the match?
4. Is the condition stricter or broader than intended?
5. Can the test be repeated after changing the rule?

## Main takeaway

A YARA rule is not finished just because its syntax is valid.

A simple workflow is:

```text
write rule
   ↓
create expected-match sample
   ↓
create expected-no-match sample
   ↓
run YARA
   ↓
inspect matching strings
   ↓
adjust condition
   ↓
test again
```

This habit becomes increasingly important as rules become more complex.
