# Lab 53 — Event Identity, Time Windows and Alert Deduplication

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## After Lab 52
Deduplicating by content SHA-256 answers **how many distinct byte strings** matched. It cannot answer **how many security incidents** occurred: the same file may appear on different hosts or at different times.

## Three counting dimensions
The harmless sample stream deliberately contains a relayed duplicate with the same event ID, another event for the same content on the same host, an event on a different host, a later observation, and a BLUE-only alert. Two fictional rules scan each observation.

| Counting unit | Result |
| --- | ---: |
| Raw rule match rows | 11 |
| Distinct flagged event IDs | 5 |
| Distinct matching byte contents (SHA-256) | 2 |
| Illustrative `(host, hash, 60-second bucket)` groups | 4 |

The buckets are a **teaching heuristic**, NOT real incident identities. A fixed time boundary can split one real event, or merge unrelated events in the same bucket. Source event IDs can collide, be spoofed or be reused; the evaluator rejects conflicting representations of the same ID.

## Run
Requires the `yara` command in PATH:
~~~bash
python3 labs/53-event-identity-time-windows-and-alert-deduplication/evaluate.py
~~~

## Questions
1. Why shouldn't two matching files on different hosts be merged into one incident merely by hash?
2. Why doesn't a repeated event ID prove the events are identical?
3. How could window boundaries create overcount or undercount?
4. Which original timestamps, collector IDs and host identities would be needed for case management?
5. Why do these counts say nothing by themselves about rule precision or recall?

## Scope
Only fictional YARA training strings. No malware, production detection rules or operational incident identifiers.
