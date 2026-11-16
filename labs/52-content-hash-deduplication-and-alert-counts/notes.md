# Lab 52 — Content-Hash Deduplication and Alert Counts

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA rules](rules.yar) · [Evaluator](evaluate.py)

## Continuing Lab 51
Lab 51 distinguished **raw rule matches** from **unique flagged files**. Lab 52 adds a third denominator: **unique byte contents**, identified by SHA-256. Separate files can contain identical bytes, and identical contents may appear in separate incidents.

## Fictional corpus
Six harmless text files are scanned by two simple YARA rules. Two files have **identical** content `BLUE-TOKEN GREEN-TOKEN`. Other files include BLUE-only, BLUE-plus-whitespace, GREEN-only and plain text. Labels are toy positives/negatives assigned **independently of the rule output**.

| Measurement | Count |
| --- | ---: |
| Raw rule matches | 7 |
| Files with any rule match | 5 |
| Distinct file contents (all six files) | 5 |
| Distinct contents that matched | 4 |

File-level confusion matrix: **TP=3, FP=2, TN=1, FN=0**. Deduplicating exactly identical contents gives **TP=2, FP=2, TN=1, FN=0**. Metrics change when the counting unit changes. Neither is inherently the correct SOC alert count.

## Reproduce
Install the YARA command line tool, then run:
~~~bash
python3 labs/52-content-hash-deduplication-and-alert-counts/evaluate.py
~~~
The script generates only temporary harmless text files.

## Questions
1. Why do two identical hashes not prove the same incident occurred?
2. When would file-path or event-ID deduplication be preferable?
3. How do false positives look different with sample-level versus unique-content metrics?
4. Why is a stable, independently labeled holdout set important?
5. What would happen if identical content had contradictory ground-truth labels?

## Limits
Only a tiny synthetic corpus. Hash equality is byte-equivalence evidence, not proof of malware, provenance or identical attacker activity. No live malware is included.
