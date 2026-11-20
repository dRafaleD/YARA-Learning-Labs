# Lab 56 — Watermark Finalization and Late-Evidence Reconciliation

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## After Lab 55
A **watermark** identifies how far a stream processor believes event-time processing has progressed. A late event can arrive *after a time bucket has been marked complete*. A forensic/SOC system should preserve it and may need to **revise prior counts**.

## Toy evaluation
The synthetic stream has per-producer maximum event time, a 10-second allowed-lateness setting and 20-second event-time buckets. It scans harmless `BLUE-TOKEN` and `GREEN-TOKEN` strings using two simple YARA rules.

When producer A advances its watermark to 120 seconds, bucket `[100,120)` is considered finalized. A new event timestamped 110 then arrives. The evaluator calls it **RECONCILE**, retaining the evidence and noting that a prior count needs review. A forwarded duplicate is not treated as a new accepted event.

| Metric | Expected |
| --- | ---: |
| Raw rule matches | 8 |
| Accepted distinct event IDs | 5 |
| Accepted flagged events | 4 |
| Late accepted events | 1 |
| Duplicates / reconciliations | 1 / 1 |

## Reproduce
YARA CLI must be installed:
```bash
python3 labs/56-watermark-finalization-and-late-evidence-reconciliation/evaluate.py
```

## Questions
1. Why can event time differ from ingestion time?
2. Why must finalized time windows sometimes be revised?
3. Why do duplicated log deliveries not create new unique events?
4. How does clock skew affect a watermark?
5. Why is a time bucket not necessarily a security incident?

## Boundaries
Synthetic text and toy timing only. This does not implement production watermarks, durable incident revisions or authentic event provenance.
