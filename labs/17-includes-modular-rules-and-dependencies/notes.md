# Lab 17 — Include Files, Modular Rule Sets and Dependency Management / Include Dosyaları ve Modüler Rule Setleri

## English

### Goal

Learn how YARA rule sets can be split across files without losing clarity or testability.

This lab combines:

1. `include`,
2. helper-rule files,
3. private helper rules,
4. multi-file dependencies,
5. naming conventions,
6. relative-path awareness,
7. reproducible runbooks,
8. rule-set versioning,
9. testing dependencies,
10. avoiding hidden coupling.

## 1. Why split rule files?

As a rule set grows, one file can become difficult to maintain.

Instead of:

```text
all_rules.yar
  ├─ 100 helper rules
  ├─ 200 public rules
  └─ mixed responsibilities
```

you can separate concerns:

```text
helpers.yar
main_rules.yar
platform_linux.yar
platform_windows.yar
```

The goal is not “more files.”

The goal is clearer ownership and reuse.

## 2. include

YARA supports:

```yara
include "helpers.yar"
```

This makes rules from the included file available to the including rule set.

Lab 17 uses:

```text
main_rules.yar
    ↓ includes
helpers.yar
```

## 3. Helper rules

`helpers.yar` contains private helper rules.

One checks:

```text
LAB17 at offset 0
```

Another requires two of:

```text
alpha17
beta17
gamma17
```

The final public rule combines them.

## 4. Private helpers + includes

This creates a clean pattern:

```text
helpers.yar
  -> internal reusable logic

main_rules.yar
  -> public detection rule
```

The helpers participate in detection but do not need to be normal top-level reported matches.

## 5. Final rule

```yara
rule Lab17_Composed_From_Include : training modular
{
    condition:
        Lab17_Helper_Training_Header and
        Lab17_Helper_Two_Markers
}
```

This reuses concepts from:

- Lab 12 offsets,
- Lab 13 thresholds,
- Lab 14 private helpers,
- Lab 16 tags/organization.

The new concept is **cross-file composition**.

## 6. Run from the lab directory

Use:

```bash
yara main_rules.yar samples/match.txt
```

Expected:

```text
Lab17_Composed_From_Include
```

Negative tests:

```bash
yara main_rules.yar samples/no-header.txt
yara main_rules.yar samples/no-markers.txt
```

Expected: no match.

## 7. Include-path awareness

Multi-file rule sets introduce path dependencies.

If YARA cannot find the included file, the rule set may fail to compile.

That means your detection package now depends on:

- directory layout,
- invocation location,
- include configuration,
- deployment packaging.

This is an operational concern, not only syntax.

## 8. Hidden coupling

A rule file can become fragile if it secretly depends on many helpers.

Ask:

- Which file defines this helper?
- Can I understand the dependency chain?
- Is the helper name stable?
- Will renaming it break many rules?

Good modularity makes dependencies easier to see.

Bad modularity hides them.

## 9. Naming conventions

Prefer names that show role/purpose:

```text
Helper_Header_...
Helper_PE_...
Linux_...
Behavior_...
Family_...
```

Avoid generic names:

```text
helper1
test
rule_new
final2
```

Stable names matter if rules reference each other.

## 10. Include trees

Small projects may have:

```text
main.yar
  -> helpers.yar
```

Larger projects might have:

```text
main.yar
  -> common/helpers.yar
  -> formats/pe.yar
  -> formats/elf.yar
```

Keep the tree understandable.

A deeply nested include graph can become difficult to debug.

## 11. Cyclic dependency thinking

Even without intentionally building cycles, rule-set design should avoid structures where files conceptually depend on each other in confusing ways.

Prefer one-directional dependency:

```text
public rules
     ↓
shared helpers
```

rather than:

```text
A depends on B
B depends on C
C depends on A
```

Operational simplicity matters.

## 12. Versioning

If `main_rules.yar` depends on `helpers.yar`, you should version them together.

A commit hash is useful evidence of exactly which rule package was used.

Record:

```text
Repository:
Commit:
YARA version:
Command:
Sample SHA-256:
Result:
```

This connects YARA engineering with reproducibility.

## 13. Testing dependency failures

A good test is not only:

> Does the positive sample match?

Also test:

- included file missing,
- helper renamed,
- negative sample,
- path changed,
- rule duplicated,
- syntax error in helper.

This helps catch packaging/configuration problems.

## 14. Rule duplication

Large rule sets can accidentally create duplicate names.

Unique naming avoids ambiguity and compilation issues.

Think of rule names as identifiers used by humans and automation.

## 15. Why not copy/paste helpers everywhere?

Copy/paste creates drift.

Example:

```text
helper copied into 8 files
        ↓
bug fixed in 1
        ↓
7 stale versions remain
```

Shared helper files can reduce this risk.

But reuse should be intentional.

## 16. Reuse vs over-abstraction

Not every two-line condition deserves a shared helper.

Create a helper when it improves:

- clarity,
- consistency,
- reuse,
- testing.

Do not create abstraction only to make the repository look “enterprise.”

## 17. Runbook

This lab includes:

```text
RUNBOOK.md
```

It documents:

- files,
- exact commands,
- expected positive result,
- expected negative results,
- YARA version check.

A rule package is easier to trust when another analyst can reproduce the result.

## 18. Packaging concept

A deployable rule package might contain:

```text
rules/
  main_rules.yar
  helpers.yar
samples/
tests/
RUNBOOK.md
README.md
VERSION
```

The point is to treat detection logic as maintained software.

## 19. Change-impact thinking

Suppose you change:

```text
Lab17_Helper_Two_Markers
```

from `2 of them` to `all of them`.

Which public rules depend on it?

This is why dependency awareness matters.

A helper change can alter several detections at once.

## 20. Mini challenge — add a third helper

Add:

```text
Lab17_Helper_Small_File
```

requiring:

```yara
filesize < 1KB
```

Then update the public rule to require it.

Retest all three samples.

## 21. Mini challenge — split by platform

Create:

```text
linux_helpers.yar
windows_helpers.yar
```

Use only harmless marker-based rules.

Then decide whether one top-level `main_rules.yar` should include both.

Explain the trade-off.

## 22. Mini challenge — dependency map

Draw:

```text
main_rules.yar
   ↓
helpers.yar
   ├─ Helper_Header
   └─ Helper_Two_Markers
```

Then extend the map when you add a third helper.

This is basic dependency documentation.

## 23. Exercises

1. Run the positive sample.
2. Run both negative samples.
3. Read `helpers.yar`.
4. Explain why helpers are private.
5. Explain how include works.
6. Rename a helper in a working copy and observe the error.
7. Move `helpers.yar` temporarily and observe include-path failure.
8. Restore the files and rerun.
9. Add the small-file helper.
10. Update the dependency map.
11. Record YARA version and commit.
12. Hash the samples.

## Questions

1. What does `include` do?
2. Why split a rule set?
3. Why can include paths fail?
4. What is hidden coupling?
5. Why are stable helper names useful?
6. Why version included files together?
7. Why test missing dependencies?
8. Why avoid copy/paste helper logic?
9. When is a helper worth creating?
10. Why can a helper change affect many rules?
11. What belongs in a runbook?
12. Why treat YARA rules like maintained software?

## Main takeaway

```text
large rule set
    ↓
separate responsibilities
    ↓
include shared helpers
    ↓
track dependencies
    ↓
test packaging + logic
    ↓
reproducible detection package
```

---

## Türkçe

### Amaç

YARA rule set büyüdüğünde logic'i birden fazla dosyada düzenli şekilde yönetmeyi öğrenmek.

Bu lab:

1. `include`,
2. helper-rule file,
3. private helper,
4. multi-file dependency,
5. naming convention,
6. include path,
7. runbook,
8. versioning,
9. dependency test,
10. hidden coupling

konularını birlikte işler.

## 1. Neden rule file bölünür?

Tek dev file:

```text
all_rules.yar
```

zamanla zor yönetilebilir.

Daha düzenli:

```text
helpers.yar
main_rules.yar
platform_linux.yar
platform_windows.yar
```

Amaç file sayısını artırmak değil, responsibility'yi ayırmak.

## 2. include

```yara
include "helpers.yar"
```

included file'daki rule'ları kullanılabilir hale getirir.

## 3. Helper rule

`helpers.yar`:

- header kontrolü,
- marker threshold

yapan private helper'lar içeriyor.

Final public rule ikisini combine ediyor.

## 4. Önceki lablarla bağlantı

Bu lab:

- Lab 12 offset,
- Lab 13 threshold,
- Lab 14 private helper,
- Lab 16 organization/tag

bilgisini tekrar kullanır.

Yeni konu cross-file composition'dır.

## 5. Çalıştır

```bash
yara main_rules.yar samples/match.txt
```

Beklenen:

```text
Lab17_Composed_From_Include
```

Negative:

```bash
yara main_rules.yar samples/no-header.txt
yara main_rules.yar samples/no-markers.txt
```

match olmamalı.

## 6. Include path

Included file bulunamazsa rule set compile olmayabilir.

Artık detection package:

- directory layout,
- invocation location,
- packaging

gibi operational dependency'lere sahiptir.

## 7. Hidden coupling

Sor:

- Helper nerede define?
- Dependency chain net mi?
- Helper name stable mi?
- Rename kaç rule'u bozar?

Good modularity dependency'yi görünür yapar.

## 8. Naming convention

İyi:

```text
Helper_Header_...
Linux_...
Behavior_...
```

Kötü:

```text
helper1
newrule
final2
```

Rule reference varsa stable name daha da önemlidir.

## 9. Include tree

Basit:

```text
main.yar
  -> helpers.yar
```

Büyük:

```text
main.yar
  -> common/helpers.yar
  -> formats/pe.yar
  -> formats/elf.yar
```

Tree anlaşılır kalmalı.

## 10. Versioning

`main_rules.yar` ve `helpers.yar` birlikte version edilmeli.

Kaydet:

```text
Commit:
YARA version:
Command:
Sample hash:
Result:
```

Bu reproducibility sağlar.

## 11. Dependency failure test

Sadece positive match test etme.

Şunları da test et:

- included file missing,
- helper rename,
- syntax error,
- negative sample,
- moved path.

## 12. Copy/paste problemi

Helper 8 dosyaya copy edilirse bug fix drift oluşabilir.

Shared helper bunu azaltabilir.

Ama reuse gereksiz abstraction'a dönüşmemeli.

## 13. Runbook

Labdaki `RUNBOOK.md` exact command ve expected result içerir.

Başka analyst aynı sonucu reproduce edebilmelidir.

## 14. Change impact

Helper condition değişirse ona bağlı birden fazla public rule etkilenebilir.

Bu yüzden dependency map önemlidir.

## 15. Mini challenge

Üçüncü helper ekle:

```yara
filesize < 1KB
```

Final rule'a bağla ve tüm sample'ları tekrar test et.

## 16. Mini challenge — platform split

```text
linux_helpers.yar
windows_helpers.yar
```

oluşturup harmless marker rule'ları ayır.

Tek main file'ın ikisini include edip etmemesi gerektiğini tartış.

## 17. Alıştırmalar

1. Positive sample çalıştır.
2. Negative sample'ları çalıştır.
3. helpers file'ı incele.
4. Private neden açıkla.
5. Include mantığını açıkla.
6. Working copy'de helper rename edip error gözlemle.
7. Include file'ı taşıyıp path failure gözlemle.
8. Restore et.
9. Small-file helper ekle.
10. Dependency map çiz.
11. YARA version/commit kaydet.
12. Sample hash al.

## Sorular

1. Include ne yapar?
2. Rule set neden bölünür?
3. Include path neden fail olabilir?
4. Hidden coupling nedir?
5. Stable helper name neden önemli?
6. Included files neden birlikte version edilmeli?
7. Missing dependency neden test edilmeli?
8. Copy/paste helper neden risklidir?
9. Helper ne zaman mantıklıdır?
10. Helper change neden birçok rule'u etkileyebilir?
11. Runbook ne içermeli?
12. YARA rule neden maintained software gibi ele alınmalı?

## Ana çıkarım

```text
large rule set
    ↓
responsibility ayır
    ↓
shared helper include et
    ↓
dependency takip et
    ↓
logic + packaging test et
    ↓
reproducible detection package
```
