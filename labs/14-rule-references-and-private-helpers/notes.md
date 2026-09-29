# Lab 14 — Rule References and Private Helper Rules / Rule Referansları ve Private Helper Rule'lar

## English

### Goal

Learn how one YARA rule can reference another rule and how `private rule` can be used to build reusable helper logic without reporting those helper rules as normal matches.

This lab introduces a more modular way to write detection logic.

## 1. Rule references

A rule can use another rule's result in its own condition.

Conceptually:

```yara
rule A {
    condition:
        ...
}

rule B {
    condition:
        A and ...
}
```

If `A` is true for the scanned file, rule `B` can use that result as another condition.

## 2. Why split logic?

Instead of putting everything into one very large rule, you can separate ideas:

```text
header check
content check
file-structure check
final composed rule
```

This can make a rule easier to read, test, and maintain.

## 3. Private helper rules

Lab 14 uses:

```yara
private rule Lab14_Helper_Header
```

and:

```yara
private rule Lab14_Helper_Content
```

A private rule can participate in rule logic but is not reported as a normal matching result by YARA.

That makes it useful as an internal helper.

## 4. Header helper

The first helper checks:

```yara
$header at 0
```

So the file must begin with:

```text
LAB14
```

This reuses the offset concept from Lab 12.

## 5. Content helper

The second helper defines:

```yara
$a = "alpha"
$b = "beta"
$c = "gamma"
```

and requires:

```yara
2 of them
```

This reuses the threshold concept from Lab 13.

## 6. Final composed rule

The public rule is:

```yara
rule Lab14_Composed_Detection
{
    condition:
        Lab14_Helper_Header and Lab14_Helper_Content
}
```

The final rule therefore requires both helper conditions.

The logic becomes:

```text
correct header
      +
enough content indicators
      ↓
final rule matches
```

## 7. Test

Run:

```bash
yara test_rules.yar samples/match.txt
yara test_rules.yar samples/no-match-header.txt
yara test_rules.yar samples/no-match-content.txt
```

Expected behavior:

```text
match.txt            -> Lab14_Composed_Detection
no-match-header.txt  -> no match
no-match-content.txt -> no match
```

You can also use:

```bash
yara -s test_rules.yar samples/match.txt
```

Note that private helper rules are used internally rather than shown as ordinary final matches.

## 8. Modular detection thinking

This approach encourages you to think in independent questions:

```text
Does the file have expected structure?
Does it contain enough relevant indicators?
Do both conditions hold?
```

Then the final rule combines the answers.

## 9. Benefits

Helper rules can improve:

- readability,
- reuse,
- testing,
- maintenance,
- separation of concerns.

But unnecessary fragmentation can also make a simple rule harder to follow. Use modularity when it actually improves clarity.

## 10. Detection-engineering connection

Real detection logic often combines different categories of evidence.

For example:

```text
file type
   +
structural property
   +
content indicators
   +
final threshold
```

Breaking these ideas into well-named helpers can make complex logic easier to reason about.

A match is still not proof of malware. Validation against appropriate datasets remains essential.

## Exercises

1. Change `Lab14_Helper_Content` from `2 of them` to `all of them`.
2. Add `gamma` to `match.txt` and retest.
3. Remove `private` from one helper and observe the output.
4. Add a third private helper that checks `filesize < 1KB`.
5. Update the final rule to require all three helpers.
6. Explain when splitting one rule into helpers improves readability.

## Questions

1. What is a rule reference?
2. What does `private rule` change about output behavior?
3. Why are helper rules useful?
4. Can a private rule still affect another rule's condition?
5. Which earlier concepts are reused in this lab?
6. Why should modular rules still be tested with negative samples?

## Main takeaway

```text
small helper rules
       ↓
clear individual checks
       ↓
rule references
       ↓
combined final condition
       ↓
easier testing and maintenance
```

---

## Türkçe

### Amaç

Bir YARA rule'unun başka bir rule'un sonucunu nasıl kullanabildiğini ve `private rule` ile final output'ta görünmeyen reusable helper logic oluşturmayı öğrenmek.

Bu lab detection logic'i daha modüler yazmaya giriş yapar.

## 1. Rule reference

Bir rule başka bir rule'un sonucunu kendi condition'ında kullanabilir.

Kavramsal olarak:

```yara
rule A {
    condition:
        ...
}

rule B {
    condition:
        A and ...
}
```

`A` scanned file için true ise `B`, bu sonucu başka bir condition gibi kullanabilir.

## 2. Logic neden bölünür?

Her şeyi tek dev rule içine koymak yerine fikirleri ayırabiliriz:

```text
header check
content check
file-structure check
final composed rule
```

Bu yapı readability, test ve maintenance açısından daha rahat olabilir.

## 3. Private helper rule

Lab 14:

```yara
private rule Lab14_Helper_Header
```

ve:

```yara
private rule Lab14_Helper_Content
```

kullanıyor.

Private rule detection logic içinde kullanılabilir fakat normal final match gibi raporlanmaz.

Bu yüzden internal helper olarak kullanışlıdır.

## 4. Header helper

İlk helper:

```yara
$header at 0
```

kontrolünü yapar.

Yani dosyanın:

```text
LAB14
```

ile başlaması gerekir.

Bu Lab 12'deki offset mantığını tekrar kullanır.

## 5. Content helper

İkinci helper:

```yara
$a = "alpha"
$b = "beta"
$c = "gamma"
```

tanımlar ve:

```yara
2 of them
```

ister.

Bu da Lab 13'teki threshold mantığını tekrar eder.

## 6. Final composed rule

Public rule:

```yara
rule Lab14_Composed_Detection
{
    condition:
        Lab14_Helper_Header and Lab14_Helper_Content
}
```

Yani iki helper'ın da true olması gerekir.

```text
doğru header
      +
yeterli content indicator
      ↓
final rule match
```

## 7. Test

```bash
yara test_rules.yar samples/match.txt
yara test_rules.yar samples/no-match-header.txt
yara test_rules.yar samples/no-match-content.txt
```

Beklenen:

```text
match.txt            -> Lab14_Composed_Detection
no-match-header.txt  -> no match
no-match-content.txt -> no match
```

Ayrıca:

```bash
yara -s test_rules.yar samples/match.txt
```

kullanabilirsin.

Private helper rule'lar internal logic olarak çalışır; normal final match gibi listelenmez.

## 8. Modüler detection düşüncesi

Soruları ayrı ayrı düşün:

```text
Beklenen structure var mı?
Yeterli relevant indicator var mı?
İkisi de doğru mu?
```

Son rule bu cevapları birleştirir.

## 9. Avantajları

Helper rule'lar:

- readability,
- reuse,
- testing,
- maintenance,
- separation of concerns

konularında faydalı olabilir.

Ama gereksiz yere çok parçaya bölmek basit rule'u daha zor okunur hale de getirebilir.

## 10. Detection engineering bağlantısı

Gerçek detection logic genellikle birden fazla evidence kategorisini birleştirir:

```text
file type
   +
structural property
   +
content indicators
   +
final threshold
```

Bunları iyi isimlendirilmiş helper'lara ayırmak karmaşık rule'ları daha anlaşılır hale getirebilir.

Match yine tek başına malware kanıtı değildir. Validation dataset ile test hâlâ gereklidir.

## Alıştırmalar

1. `Lab14_Helper_Content` içinde `2 of them` yerine `all of them` kullan.
2. `match.txt` içine `gamma` ekleyip tekrar test et.
3. Helper'lardan birinden `private` keyword'ünü kaldır ve output'u gözlemle.
4. `filesize < 1KB` kontrol eden üçüncü private helper ekle.
5. Final rule'da üç helper'ı da zorunlu hale getir.
6. Helper'a bölmenin ne zaman readability sağladığını açıkla.

## Sorular

1. Rule reference nedir?
2. `private rule` output davranışını nasıl değiştirir?
3. Helper rule neden faydalıdır?
4. Private rule başka rule'un condition'ını etkileyebilir mi?
5. Bu lab önceki hangi kavramları tekrar kullanıyor?
6. Modüler rule'lar neden yine negative sample ile test edilmelidir?

## Ana çıkarım

```text
küçük helper rule'lar
       ↓
net ayrı kontroller
       ↓
rule reference
       ↓
birleşik final condition
       ↓
daha kolay test ve maintenance
```
