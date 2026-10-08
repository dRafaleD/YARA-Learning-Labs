# Lab 18 — Rule Quality, False Positives, Performance and Test Corpus Design

## English

### Goal

Move from “a rule matches” to “a rule is useful, explainable, testable, and reasonably efficient.”

This lab combines:

1. false positives and false negatives,
2. broad vs contextual indicators,
3. threshold conditions,
4. rule selectivity,
5. regex/string cost awareness,
6. early structural/size gates,
7. benign test corpora,
8. repeatable performance checks,
9. precision vs coverage,
10. documenting rule limitations.

## 1. A match is not enough

A YARA rule can be syntactically correct and still be poor.

Example:

~~~yara
strings:
    $a = "error"

condition:
    $a
~~~

The word "error" appears in countless benign files.

The rule works technically, but its detection value is weak.

## 2. False positives

A false positive is a benign object that satisfies a rule intended for something else.

In this lab, the broad rule intentionally matches ordinary benign files containing:

~~~text
error
~~~

This demonstrates why common strings are weak indicators.

## 3. False negatives

A false negative occurs when a target you intended to detect does not match.

Overly strict conditions can cause this.

Example:

~~~text
marker
AND exact version
AND exact filename
AND exact section count
~~~

may match one build and miss slightly different legitimate variants of the same target family.

## 4. Precision vs coverage

A useful detection trade-off:

~~~text
more restrictive
   ↓
usually fewer false positives
   +
possibly more false negatives
~~~

and:

~~~text
broader
   ↓
usually more coverage
   +
possibly more false positives
~~~

Good detection engineering chooses this balance intentionally.

## 5. Contextual indicators

The contextual training rule requires:

- a lab marker,
- a component marker,
- a version-shaped string,
- a small-file size gate.

Conceptually:

~~~text
one weak clue
   +
another independent clue
   +
expected context
   ↓
stronger match
~~~

Independent evidence is often more useful than repeating variations of one weak string.

## 6. Threshold conditions

The threshold rule uses:

~~~yara
3 of ($a, $b, $c, $d)
~~~

Thresholds can provide resilience when one indicator is absent.

They also let you tune coverage.

But arbitrary thresholds are not automatically good. They should be justified by testing.

## 7. Selectivity

A selective string occurs relatively rarely in unrelated files.

Compare:

~~~text
error
update
version
~~~

with a more specific training marker:

~~~text
YARA_LAB18_MARKER
~~~

Specific markers generally create fewer accidental matches.

In real detection work, selectivity should be measured against representative benign data.

## 8. Performance matters

Large rule sets may scan:

- many files,
- large files,
- memory,
- endpoint fleets,
- forensic collections.

A needlessly expensive rule can slow an entire workflow.

Rule quality therefore includes both detection behavior and operational cost.

## 9. Regex cost awareness

Regex is powerful, but do not use it when an exact string or simpler expression is enough.

Ask:

> Do I actually need variable matching here?

Simpler matching is often easier to understand, test, and maintain.

Do not optimize blindly; profile against your real corpus.

## 10. Structural gates

A condition such as:

~~~yara
filesize < 64KB
~~~

can express expected context and avoid matching obviously unrelated large files.

But only use such gates when they make sense for your target.

Bad optimization is a condition that makes scanning fast by silently excluding valid targets.

## 11. Test corpus

A rule should be tested on more than one positive sample.

Useful categories:

~~~text
positive samples
negative/benign samples
near-miss samples
variant samples
large unrelated samples
~~~

This lab generates a small benign corpus for practice.

## 12. Generate the samples

Run:

~~~bash
python3 create_samples.py
~~~

The script creates:

- positive contextual sample,
- common-error benign sample,
- marker-only near miss,
- threshold positive/negative samples,
- 30-file benign corpus.

All data is harmless text.

## 13. Run focused tests

~~~bash
yara test_rules.yar samples/positive-contextual.txt
yara test_rules.yar samples/negative-common-error.txt
yara test_rules.yar samples/negative-marker-only.txt
yara test_rules.yar samples/threshold-positive.txt
yara test_rules.yar samples/threshold-negative.txt
~~~

Record exactly which rules match.

## 14. Broad rule experiment

Scan the benign corpus:

~~~bash
yara -r test_rules.yar samples/benign-corpus/
~~~

Several files intentionally contain "error".

Count how many times the broad rule fires.

Then ask:

> Would this rule be usable in a real alerting pipeline?

## 15. Near-miss testing

The marker-only sample contains:

~~~text
YARA_LAB18_MARKER
~~~

but lacks the other contextual indicators.

The contextual rule should not match.

Near-miss tests are important because they show whether one weak indicator can accidentally trigger the whole rule.

## 16. Timing locally

Use:

~~~bash
time yara -r test_rules.yar samples/benign-corpus/
~~~

Do not over-interpret one timing result.

Performance depends on:

- CPU,
- filesystem cache,
- corpus size,
- YARA version,
- other system load.

Repeat measurements and compare relative changes on the same machine.

## 17. Optimize with evidence

Bad workflow:

~~~text
guess expensive part
   ↓
rewrite everything
   ↓
hope it is faster
~~~

Better:

~~~text
baseline
   ↓
change one thing
   ↓
retest correctness
   ↓
remeasure
   ↓
document result
~~~

Never sacrifice correctness without knowing the trade-off.

## 18. Rule readability

Performance is not the only maintainability concern.

Good rules should make it easy to answer:

- Why did this match?
- Which indicators mattered?
- What is the expected scope?
- What are known limitations?

Readable names and metadata matter.

## 19. Explainable matches

When possible, inspect matching strings:

~~~bash
yara -s test_rules.yar samples/positive-contextual.txt
~~~

This helps explain which evidence satisfied the rule.

Detection should be interpretable enough for another analyst to review.

## 20. Regression tests

When you change a rule, rerun old test cases.

A rule fix can accidentally break a previously correct case.

Conceptually:

~~~text
rule change
   ↓
positive tests
negative tests
near-miss tests
performance check
   ↓
accept/reject change
~~~

## 21. Version control

Record the rule-set commit together with test results.

A statement like:

> “Rule X produced 0 false positives in my test corpus”

is incomplete unless you know:

- which rule version,
- which corpus,
- which YARA version,
- which test procedure.

## 22. Mini challenge — improve the broad rule

Take the intentionally broad rule and improve it.

Requirements:

- do not simply delete it,
- add at least one independent contextual indicator,
- keep a positive test,
- reduce benign-corpus matches,
- document what coverage you may have lost.

## 23. Mini challenge — tune the threshold

Change:

~~~text
3 of 4
~~~

to:

~~~text
2 of 4
~~~

Run positive and negative samples again.

Explain how precision and coverage changed.

Then restore the original rule.

## 24. Mini challenge — performance experiment

Create 100 harmless text files.

Compare two rule variants:

- one with a simple exact marker,
- one using a regex for the same fixed text.

Measure locally.

Do not claim universal performance conclusions from one machine.

## 25. Detection-quality worksheet

For each rule, record:

~~~text
Rule name:
Purpose:
Positive samples:
Negative corpus:
Near misses:
False positives observed:
False negatives observed:
Expected scope:
Known limitations:
Local timing:
YARA version:
Commit:
~~~

## Exercises

1. Generate samples.
2. Run all focused tests.
3. Scan the benign corpus.
4. Count broad-rule matches.
5. Inspect matching strings with -s.
6. Explain why marker-only does not satisfy the contextual rule.
7. Tune the threshold to 2 of 4.
8. Compare results.
9. Improve the broad rule.
10. Re-run the corpus.
11. Time the scan before/after a change.
12. Fill the detection-quality worksheet.

## Questions

1. What is a false positive?
2. What is a false negative?
3. Precision vs coverage?
4. What makes an indicator selective?
5. Why can common strings be noisy?
6. Why use threshold conditions?
7. Why can regex be more costly/complex?
8. Why use structural gates carefully?
9. What is a near-miss sample?
10. Why do regression tests matter?
11. Why should performance be measured locally?
12. Why record rule version and corpus version?

## Main takeaway

~~~text
rule syntax
   ↓
positive behavior
   ↓
benign/near-miss testing
   ↓
precision vs coverage
   ↓
performance measurement
   ↓
documented limitations
   ↓
useful detection engineering
~~~

---

## Türkçe

### Amaç

“Rule match oluyor” seviyesinden, “rule gerçekten kullanışlı, test edilmiş ve açıklanabilir mi?” seviyesine geçmek.

Bu lab:

- false positive,
- false negative,
- broad vs contextual indicator,
- threshold,
- selectivity,
- performance,
- regex maliyeti,
- structural gate,
- benign corpus,
- regression testing,
- precision vs coverage

konularını birlikte işler.

## 1. Match olması yeterli değildir

~~~yara
$a = "error"
condition:
    $a
~~~

gibi rule teknik olarak çalışır ama birçok benign file'da match olabilir.

Bu nedenle syntax correctness ile detection quality aynı şey değildir.

## 2. False positive

Benign bir object'in yanlışlıkla target olarak match edilmesidir.

Labdaki broad rule bunu bilinçli olarak gösterir.

## 3. False negative

Detect etmek istediğin target'ın match olmamasıdır.

Aşırı strict condition coverage kaybettirebilir.

## 4. Precision vs coverage

~~~text
daha restrictive
   ↓
az FP olabilir
   +
fazla FN olabilir
~~~

Broad rule ise daha çok target yakalarken daha fazla benign match üretebilir.

## 5. Contextual indicator

Tek weak string yerine bağımsız context ekle:

~~~text
marker
+
component
+
version pattern
+
expected size
~~~

Bu daha anlamlı detection oluşturabilir.

## 6. Threshold

~~~yara
3 of ($a, $b, $c, $d)
~~~

bir indicator eksik olsa bile match sağlayabilir.

Threshold test ile justify edilmelidir.

## 7. Selectivity

"error", "update", "version" gibi common string'ler düşük selectivity taşır.

Specific marker daha az accidental match üretir.

Gerçek rule'da bunu representative benign corpus ile ölçmek gerekir.

## 8. Performance

Rule set endpoint fleet veya büyük evidence collection tarayabilir.

Gereksiz expensive condition bütün workflow'u yavaşlatabilir.

## 9. Regex awareness

Regex güçlüdür ama fixed text için gereksiz regex yazma.

Önce simple string yeterli mi sor.

Optimization tahminle değil measurement ile yapılmalı.

## 10. Structural gate

~~~yara
filesize < 64KB
~~~

gibi condition expected context'i ifade edebilir.

Ama valid target'ı dışlıyorsa kötü optimization olur.

## 11. Test corpus

Sadece positive sample kullanma.

~~~text
positive
benign/negative
near-miss
variant
unrelated
~~~

sample'lar ekle.

## 12. Sample üret

~~~bash
python3 create_samples.py
~~~

Harmless practice corpus oluşturur.

## 13. Test

~~~bash
yara test_rules.yar samples/positive-contextual.txt
yara test_rules.yar samples/negative-common-error.txt
yara test_rules.yar samples/negative-marker-only.txt
yara test_rules.yar samples/threshold-positive.txt
yara test_rules.yar samples/threshold-negative.txt
~~~

Hangi rule'un neden match olduğunu kaydet.

## 14. Benign corpus

~~~bash
yara -r test_rules.yar samples/benign-corpus/
~~~

Broad rule'un kaç benign file'da match olduğunu say.

## 15. Near-miss

Marker-only sample tek indicator içerir.

Contextual rule'un match olmaması gerekir.

Bu, weak indicator'ın tek başına trigger olmadığını test eder.

## 16. Local timing

~~~bash
time yara -r test_rules.yar samples/benign-corpus/
~~~

Tek result'i universal benchmark olarak sunma.

Aynı machine üzerinde relative comparison yap.

## 17. Evidence-based optimization

~~~text
baseline
   ↓
one change
   ↓
correctness retest
   ↓
remeasure
   ↓
document
~~~

## 18. Readability

Rule başka analyst tarafından açıklanabilir olmalı.

Name, meta ve string identifier'ları meaningful tut.

## 19. Matching strings

~~~bash
yara -s test_rules.yar samples/positive-contextual.txt
~~~

hangi indicator'ın match olduğunu gör.

## 20. Regression

Rule change sonrası eski positive/negative/near-miss testleri tekrar koş.

## 21. Version control

Test sonucu ile birlikte:

- rule commit,
- corpus,
- YARA version,
- command

kaydet.

## 22. Mini challenge — broad rule

Broad rule'a independent context ekle.

Benign match sayısını azalt ve kaybedilen coverage'ı açıkla.

## 23. Mini challenge — threshold

3/4 yerine 2/4 dene.

Precision/coverage etkisini gözlemle.

Sonra restore et.

## 24. Mini challenge — performance

100 harmless file üret.

Fixed string ile aynı pattern için regex variant'ı karşılaştır.

Local result olarak raporla.

## 25. Worksheet

~~~text
Rule:
Purpose:
Positive:
Negative corpus:
Near miss:
FP:
FN:
Scope:
Limitations:
Timing:
YARA version:
Commit:
~~~

## Alıştırmalar

1. Sample üret.
2. Focused testleri koş.
3. Benign corpus tara.
4. Broad match say.
5. -s kullan.
6. Near-miss'i açıkla.
7. Threshold değiştir.
8. Sonuç compare et.
9. Broad rule'u iyileştir.
10. Corpus'u tekrar tara.
11. Timing compare et.
12. Worksheet doldur.

## Sorular

1. False positive nedir?
2. False negative nedir?
3. Precision vs coverage?
4. Selective indicator nedir?
5. Common string neden noisy?
6. Threshold neden kullanılır?
7. Regex neden daha complex olabilir?
8. Structural gate neden dikkatli kullanılmalı?
9. Near-miss sample nedir?
10. Regression neden önemli?
11. Performance neden local ölçülmeli?
12. Rule/corpus version neden kaydedilmeli?

## Ana çıkarım

~~~text
rule
 ↓
positive test
 ↓
benign + near-miss
 ↓
precision / coverage
 ↓
performance
 ↓
limitations
 ↓
quality detection
~~~
