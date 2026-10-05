# Lab 16 — External Variables, Tags and Rule Organization / External Variable, Tag ve Rule Organizasyonu

## English

### Goal

Move from writing isolated rules toward organizing rules for larger workflows.

This lab combines several related topics:

1. external variables,
2. rule tags,
3. grouping and organization,
4. environment-aware rule logic,
5. recursive scanning,
6. selecting tagged rules,
7. keeping configuration separate from detection logic,
8. testing rule behavior under different external values.

## 1. Why external variables?

Sometimes a rule needs context that should come from outside the rule file.

For example:

- environment name,
- deployment mode,
- customer/lab identifier,
- scan profile,
- feature flag.

Instead of hardcoding everything, YARA can receive external variables from the command line.

The idea is:

```text
rule logic
   +
external context
   ↓
final condition
```

## 2. External variable example

The first rule uses:

```yara
environment == "lab"
```

This value is not defined in the rule file.

You provide it when running YARA:

```bash
yara -d environment=lab test_rules.yar samples/match-environment.txt
```

If the external variable is different:

```bash
yara -d environment=prod test_rules.yar samples/match-environment.txt
```

the rule condition changes.

## 3. Why this is useful

Imagine the same rule set used in different contexts.

Instead of maintaining separate copies:

```text
rules-lab.yar
rules-prod.yar
rules-test.yar
```

you may keep one rule set and pass controlled context externally.

This can improve maintainability.

But external variables should not become an excuse for unclear rule logic.

## 4. External variables are inputs too

Treat external values as part of the scan configuration.

Ask:

- Who sets the value?
- Is the value controlled?
- What happens if it is missing?
- Could an unexpected value disable a rule?
- Is the scan reproducible?

Detection engineering requires configuration discipline.

## 5. Tags

YARA rules can have tags:

```yara
rule Lab16_Tagged_Training_Rule : training linux
```

The tags are:

```text
training
linux
```

Tags help organize rules without changing the core detection condition.

They can describe categories such as:

- platform,
- malware family,
- confidence,
- workflow,
- purpose,
- lab grouping.

Do not overload tags with too many meanings.

## 6. Tags vs meta

These are related but different.

### Tags

Compact labels attached to the rule.

### Meta

Descriptive key/value information.

Example:

```yara
meta:
    description = "..."
    author = "..."
    purpose = "..."
```

A useful mental model:

```text
tags -> grouping/filtering labels
meta -> descriptive documentation
condition -> actual detection logic
```

## 7. Run the tagged rule

Use:

```bash
yara -d environment=lab test_rules.yar samples/match-environment.txt
```

Expected match:

```text
Lab16_Tagged_Training_Rule
```

Change the external variable:

```bash
yara -d environment=prod test_rules.yar samples/match-environment.txt
```

Expected: no match for that rule.

## 8. Show tags

Depending on YARA version/options, use output modes that display rule metadata/tags when available.

At minimum, inspect the rule source and understand that tags are attached to the rule identity, not to strings.

The point of this lab is rule organization, not memorizing one CLI output format.

## 9. Grouping related indicators

The second rule uses:

```yara
$a = "alpha16"
$b = "beta16"
$c = "gamma16"
```

with:

```yara
2 of them
```

This repeats threshold logic from earlier labs but now inside a more organized rule set.

The learning progression is:

```text
single rule syntax
   ↓
multiple related indicators
   ↓
thresholds
   ↓
helper rules
   ↓
tags + external context
   ↓
maintainable rule sets
```

## 10. Configuration vs detection logic

Good rule engineering tries to separate:

```text
what indicates the thing?
        from
where/how am I scanning?
```

Example:

```text
marker string + structural evidence
        -> detection logic

environment=lab
        -> scan configuration
```

Mixing deployment details deeply into every condition can make rules harder to reuse.

## 11. Missing external variables

A rule referencing an undefined external variable can fail to compile/run depending on how it is invoked.

This is useful because it forces you to think about reproducibility.

Document the required invocation:

```bash
yara -d environment=lab ...
```

If a rule set depends on external variables, the README/runbook should say so clearly.

## 12. Reproducibility

A detection result should ideally be reproducible.

Record:

- YARA version,
- rule file version,
- external variable values,
- scanned path/file,
- hashes of important samples,
- command used.

Example:

```text
YARA version:
Rule commit:
External variables:
Sample SHA-256:
Command:
Result:
```

This connects YARA work with forensic discipline.

## 13. Recursive scanning

For a lab directory:

```bash
yara -r -d environment=lab test_rules.yar samples/
```

Now multiple files are checked.

When using recursive scans, be careful interpreting large result sets.

A match count is not the same thing as incident count.

## 14. Rule naming conventions

As rule sets grow, naming becomes important.

Useful patterns:

```text
Lab16_...
Linux_...
Family_...
Behavior_...
```

Names should be:

- unique,
- descriptive,
- stable enough for automation,
- readable by humans.

Avoid names such as:

```text
rule1
test2
final_rule_new
```

in serious rule sets.

## 15. Tags as workflow filters

Imagine tags:

```text
linux
windows
training
high_confidence
experimental
```

These can help humans/tools decide which subsets are relevant.

But tags should not replace careful condition design.

A rule tagged `high_confidence` is only as good as the evidence and validation supporting that claim.

## 16. Environment-aware detection risk

External context can accidentally weaken detection.

Example:

```text
environment == "lab"
```

If a production scan mistakenly uses:

```text
environment=prod
```

the training rule will not match.

This is expected here, but it demonstrates a real engineering lesson:

> Configuration changes detection behavior.

Therefore config must be versioned/documented/tested.

## 17. Testing matrix

Instead of one test, create a matrix:

| Sample | environment=lab | environment=prod |
| --- | --- | --- |
| match-environment.txt | match | no match |
| no-match-environment.txt | depends on marker | no match |
| match-grouped.txt | grouped rule match | grouped rule match |

This catches mistakes better than a single happy-path test.

## 18. Mini challenge — add severity

Add a new external variable:

```text
minimum_level
```

Then design a harmless rule where a numeric meta-like threshold changes whether the rule matches.

Keep detection logic understandable.

The exercise is about external configuration, not real malware scoring.

## 19. Mini challenge — organize by tags

Add two more harmless rules:

- one tagged `windows training`
- one tagged `linux training`

Then document which rules belong to which category.

Think about how a future rule loader could select subsets.

## 20. Mini challenge — reproducible runbook

Create a short file:

```text
RUNBOOK.md
```

containing:

- required YARA version,
- exact command,
- required external variables,
- expected positive sample,
- expected negative sample,
- expected matches.

The goal is operational clarity.

## 21. Exercises

1. Run with `environment=lab`.
2. Run with `environment=prod`.
3. Explain why the result changes.
4. Identify the rule tags.
5. Explain tags vs meta.
6. Run recursive scanning.
7. Build the test matrix.
8. Add a new tagged harmless rule.
9. Add one extra external variable.
10. Document required command-line configuration.
11. Hash the sample files.
12. Explain how wrong configuration can create false negatives.

## Questions

1. What is an external variable?
2. Why use one instead of hardcoding?
3. How is an external variable supplied?
4. What are tags?
5. Tags vs meta?
6. Do tags change detection logic?
7. Why must external config be documented?
8. How can external config cause false negatives?
9. Why are naming conventions important?
10. Why is reproducibility important?
11. Why is recursive scan output not automatically an incident list?
12. What belongs in a detection runbook?

## Main takeaway

```text
rule logic
   +
external configuration
   +
tags / organization
   ↓
more maintainable rule set
   ↓
testing matrix
   ↓
reproducible detection workflow
```

---

## Türkçe

### Amaç

Tek tek rule yazmaktan daha büyük rule setlerini düzenleme mantığına geçmek.

Bu lab birbiriyle bağlantılı birkaç konuyu birlikte işler:

1. external variable,
2. rule tag,
3. rule organization,
4. environment-aware condition,
5. recursive scan,
6. configuration ile detection logic ayrımı,
7. farklı external değerlerle test,
8. reproducible runbook mantığı.

## 1. External variable neden var?

Bazı context bilgileri rule file'ın dışından gelmelidir.

Örnek:

- environment,
- deployment mode,
- lab/customer identifier,
- scan profile,
- feature flag.

Tek tek farklı rule file tutmak yerine controlled context dışarıdan verilebilir.

```text
rule logic
   +
external context
   ↓
final condition
```

## 2. External variable kullanımı

Rule:

```yara
environment == "lab"
```

kullanıyor.

Çalıştırırken:

```bash
yara -d environment=lab test_rules.yar samples/match-environment.txt
```

Farklı değer:

```bash
yara -d environment=prod test_rules.yar samples/match-environment.txt
```

condition sonucunu değiştirir.

## 3. Neden faydalı?

Ayrı ayrı:

```text
rules-lab.yar
rules-prod.yar
rules-test.yar
```

tutmak yerine tek rule set + controlled configuration kullanılabilir.

Ama external variable, karmaşık/okunmaz logic yazmak için bahane olmamalıdır.

## 4. External variable da input'tur

Sor:

- Değeri kim set ediyor?
- Controlled mı?
- Missing olursa ne olur?
- Yanlış value rule'u disable eder mi?
- Scan reproducible mı?

Detection engineering'de config discipline gerekir.

## 5. Tags

```yara
rule Lab16_Tagged_Training_Rule : training linux
```

Tag'ler:

```text
training
linux
```

Rule'ları organize etmeye yardım eder.

Platform, family, confidence, workflow veya purpose gibi kategoriler için kullanılabilir.

## 6. Tags vs meta

```text
tags -> grouping/filtering label
meta -> descriptive documentation
condition -> detection logic
```

Tag ile meta aynı şey değildir.

## 7. Rule'u çalıştır

```bash
yara -d environment=lab test_rules.yar samples/match-environment.txt
```

Beklenen match:

```text
Lab16_Tagged_Training_Rule
```

Sonra:

```bash
yara -d environment=prod test_rules.yar samples/match-environment.txt
```

Bu rule match olmamalı.

## 8. Indicator grouping

İkinci rule:

```yara
$a = "alpha16"
$b = "beta16"
$c = "gamma16"

condition:
    2 of them
```

kullanıyor.

Önceki threshold bilgisini daha organize rule set içinde tekrar kullanıyoruz.

Progression:

```text
single rule
   ↓
multiple indicator
   ↓
threshold
   ↓
helper rule
   ↓
tag + external context
   ↓
maintainable rule set
```

## 9. Configuration vs detection logic

Ayır:

```text
neyi detect ediyorum?
       vs
hangi ortamda nasıl scan ediyorum?
```

Örneğin marker/structure detection logic olabilir.

`environment=lab` ise scan configuration'dır.

## 10. Missing external variable

External variable isteyen rule uygun value verilmeden çalıştırılırsa compile/run problemi çıkabilir.

Bu yüzden invocation açıkça document edilmelidir.

```bash
yara -d environment=lab ...
```

## 11. Reproducibility

Kaydet:

- YARA version,
- rule version/commit,
- external variable,
- sample path,
- sample hash,
- exact command,
- result.

Bu YARA çalışmasını forensic discipline ile bağlar.

## 12. Recursive scan

```bash
yara -r -d environment=lab test_rules.yar samples/
```

Birden fazla file scan edilir.

Çok result görmek çok incident olduğu anlamına gelmez.

## 13. Naming convention

Rule name:

- unique,
- descriptive,
- stable,
- readable

olmalı.

```text
rule1
test_new
final_final2
```

gibi isimlerden kaçın.

## 14. Tag workflow

Örnek tag:

```text
linux
windows
training
experimental
high_confidence
```

Rule subset seçmeye yardım edebilir.

Ama tag quality, condition quality'nin yerine geçmez.

## 15. Config false negative üretebilir

`environment == "lab"` isteyen rule yanlış config ile çalıştırılırsa match kaçırılır.

Ders:

> Configuration detection behavior'ı değiştirir.

Bu yüzden config versioned/documented/tested olmalıdır.

## 16. Test matrix

| Sample | environment=lab | environment=prod |
| --- | --- | --- |
| match-environment.txt | match | no match |
| no-match-environment.txt | condition'a bağlı | no match |
| match-grouped.txt | grouped match | grouped match |

Tek happy-path testten daha güçlüdür.

## 17. Mini challenge — severity

Yeni external variable ekle:

```text
minimum_level
```

Harmless numeric threshold ile rule behavior değiştir.

Amaç config mantığını anlamak.

## 18. Mini challenge — tags

İki harmless rule ekle:

- `windows training`
- `linux training`

Sonra category'leri document et.

## 19. Mini challenge — runbook

`RUNBOOK.md` oluştur.

İçinde:

- YARA version,
- exact command,
- required external variable,
- positive sample,
- negative sample,
- expected match

olsun.

## 20. Alıştırmalar

1. `environment=lab` ile çalıştır.
2. `environment=prod` ile çalıştır.
3. Result neden değişiyor açıkla.
4. Rule tag'lerini bul.
5. Tag vs meta açıkla.
6. Recursive scan yap.
7. Test matrix oluştur.
8. Yeni tagged harmless rule ekle.
9. Bir external variable daha ekle.
10. CLI config'i document et.
11. Sample hash'lerini al.
12. Wrong config'in false negative üretmesini açıkla.

## Sorular

1. External variable nedir?
2. Neden hardcode yerine kullanılabilir?
3. Nasıl supply edilir?
4. Tag nedir?
5. Tag vs meta?
6. Tag detection logic'i değiştirir mi?
7. Config neden document edilmeli?
8. Config nasıl false negative üretir?
9. Naming convention neden önemli?
10. Reproducibility neden önemli?
11. Recursive result neden incident list değildir?
12. Runbook'ta ne olmalı?

## Ana çıkarım

```text
rule logic
   +
external configuration
   +
tag / organization
   ↓
maintainable rule set
   ↓
test matrix
   ↓
reproducible detection workflow
```
