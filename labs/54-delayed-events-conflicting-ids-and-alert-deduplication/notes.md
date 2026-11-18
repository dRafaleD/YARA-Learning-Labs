# Lab 54 — Delayed Events, Conflicting IDs and Alert Deduplication

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## After Lab 53
Day 53 compared raw YARA rule matches with unique alert IDs and time buckets. A logging pipeline adds **ingestion delay** and **conflicting event IDs**: the same identifier can arrive twice with different data, either due to a faulty producer or a data integrity problem.

## Model
Seven fictional observations include two identical copies of one event, a late-arriving observation, the same event ID from a *different* producer, and two contradictory payloads with one `(producer, event ID)` identity.

The evaluator scans harmless `BLUE-TOKEN`/`GREEN-TOKEN` text with two toy rules. It records 9 raw rule matches, 4 accepted unique flagged event identities, one duplicate and one conflict. One accepted flagged event arrives **more than 20 seconds** after its recorded event time.

**A conflicting ID is quarantined, not counted as a new incident**. For a real pipeline, keep the raw contradictory records and a trustworthy provenance trail. An apparent producer label can be forged; a late arrival need not be malicious.

## Run
Requires the `yara` command:
~~~bash
python3 labs/54-delayed-events-conflicting-ids-and-alert-deduplication/evaluate.py
~~~

## Questions
1. Why is arrival time different from event time?
2. What makes a record a duplicate versus a conflicting reuse of an ID?
3. Why should a late event not automatically be discarded?
4. Can one event ID be globally unique across different producers?
5. Why are these counts **not** precision/recall or incident numbers?

## Limits
Temporary harmless text only; no live malware, active hunting or real incident data.
