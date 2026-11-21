# Lab 57 — Versioned Alert Snapshots and Late Corrections

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## After Lab 56
Day 56 found a late YARA observation that required **reconciliation** of a finalized time bucket. Day 57 adds a **snapshot revision** so the corrected report does not silently overwrite the earlier result.

## Toy model
A synthetic stream groups harmless text matches by `(producer, 20-second bucket)`. Each group tracks its **alert count**, **revision** and **finalized** state. A watermark (maximum observed event time minus 10 seconds) finalizes older buckets.

When a new event arrives for a finalized bucket, the evaluator retains the evidence, updates the count and increments its snapshot revision. A forwarded duplicate or conflicting reuse of an existing event ID does **not** automatically increment accepted counts; conflicts are reported separately.

| Measurement | Expected |
| --- | ---: |
| Raw rule matches | 9 |
| Unique accepted events | 5 |
| Accepted flagged events | 4 |
| Late accepted events | 1 |
| Duplicates / conflicts / corrections | 1 / 1 / 1 |
| Snapshot for producer A, window 100–120 | 2 alerts, revision 2 |

## Reproduce
Requires the YARA CLI:
```bash
python3 labs/57-versioned-alert-snapshots-and-late-corrections/evaluate.py
```

## Questions
1. Why preserve the previous version of a finalized report?
2. What evidence would distinguish a late event from a forwarded duplicate?
3. Why shouldn't a contradictory ID overwrite the first observation?
4. How would a real SOC correlate bucket revisions to incident tickets?
5. Why do these rule-match counts not represent detection precision or recall?

## Limits
No real malware or SIEM. Snapshots, timestamps and source IDs are fictional and in-memory; this is not a durable audit trail.
