# Lab 55 — Event-Time Watermarks and Late Alert Reconciliation

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## After Lab 54
Lab 54 separated **event time** from **ingestion time**, and detected duplicate/conflicting event IDs. The next question is: how late can an event arrive before the pipeline must revise an earlier conclusion?

## Synthetic watermark
Each fictional producer has a maximum observed **event timestamp**. A toy watermark is `max_event_time - 10`. If a *new* event arrives with event time below the previous watermark, it is labeled **LATE**—but **kept**, not dropped.

Deduplication happens **before** new-event watermark accounting, using `(producer, event ID)`. Identical repeated facts become **DUPLICATE**; contradictory facts under the same ID become **CONFLICT**.

| Quantity | Expected |
| --- | ---: |
| Raw YARA rule matches | 9 |
| Accepted unique event identities | 5 |
| Accepted events with rule matches | 4 |
| Late accepted events | 1 |
| Duplicate / conflicting observations | 1 / 1 |

## Run
Requires YARA command line:
```bash
python3 labs/55-event-time-watermarks-and-late-alert-reconciliation/evaluate.py
```

## Exercises
1. Why can an event arrive much later than its source event time?
2. Why should a late event still be preserved for investigation?
3. How can clock skew invalidate a naive watermark?
4. Why use per-producer rather than one global maximum time?
5. Would these YARA alert counts prove true-positive detection quality?

## Boundaries
Harmless text only, toy clock and synthetic sources. Real stream processing needs authoritative event-time semantics, durable state, window finalization and reconciliation policies.
