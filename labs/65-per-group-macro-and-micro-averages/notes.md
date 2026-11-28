# Lab 65 — Per-Group Macro and Micro Detection Averages

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

Lab 64 compared detection performance per group. Today six invented text records give unequal group sizes. Group a recall is 1/1, group b recall is 1/3. Macro recall gives each defined group equal weight: 2/3. Micro recall pools positive examples: 2/4 = 1/2. Undefined group recall is excluded from macro and reported conceptually as missing, not zero. Six arithmetic checks precede the CLI scan. Practice: calculate both averages by hand, add a group with no positives and add another missed positive to b. Explain how the averages change and why tiny toy groups cannot estimate real performance. No real malware.

## Run
```bash
python3 labs/65-per-group-macro-and-micro-averages/evaluate.py
```
