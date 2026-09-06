# Lab 06 - Regular Expressions / Regular Expression'lar

## English

### Goal

Learn how YARA can match text patterns with regular expressions when an exact string would be too rigid.

### Why regular expressions?

An exact string is useful when the text is always identical:

```yara
$marker = "LAB-2048"
```

But sometimes part of the text changes while the structure stays the same.

For example:

```text
LAB-1024
LAB-2048
LAB-9001
```

Instead of writing a separate string for every value, YARA can use a regular expression:

```yara
$ticket = /LAB-[0-9]{4}/
```

This means:

```text
LAB-        -> exact text
[0-9]       -> one digit
{4}         -> exactly four times
```

So the pattern matches strings such as `LAB-2048`, but not `LAB-20A8`.

### Rule used in this lab

```yara
rule Regex_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning YARA regular expressions"
        lab = "06"
        purpose = "education"

    strings:
        $ticket = /LAB-[0-9]{4}/
        $user = /user_[a-z]{3,8}/ nocase

    condition:
        $ticket and $user
}
```

### Second expression

```yara
$user = /user_[a-z]{3,8}/ nocase
```

This searches for:

- the exact prefix `user_`
- followed by 3 to 8 letters
- without caring about upper/lower case because of `nocase`

Examples that can match:

```text
user_rafale
USER_TEST
user_admin
```

### Condition

The rule uses:

```yara
condition:
    $ticket and $user
```

Both patterns must be present in the scanned file.

This is important because a regular expression is only a way to describe a pattern. The `condition` section still decides whether the rule reports a match.

### Run the lab

Matching sample:

```console
yara labs/06-regular-expressions/regex.yar labs/06-regular-expressions/sample-match.txt
```

Expected output:

```text
Regex_Demo labs/06-regular-expressions/sample-match.txt
```

Non-matching sample:

```console
yara labs/06-regular-expressions/regex.yar labs/06-regular-expressions/sample-no-match.txt
```

No match should be printed.

### Main takeaway

```text
exact string -> best when the value is fixed
regex        -> useful when the structure is fixed but part of the value changes
condition    -> still controls the final match
```

Regular expressions are powerful, but very broad patterns can create false positives. Keep them as specific as possible and test both matching and non-matching samples.

---

## Türkçe

### Amaç

Sabit bir string'in fazla katı kaldığı durumlarda YARA ile regular expression kullanarak metin pattern'larını eşleştirmeyi öğrenmek.

### Regular expression neden kullanılır?

Metin her zaman aynıysa normal string yeterlidir:

```yara
$marker = "LAB-2048"
```

Fakat bazen değerin bir kısmı değişirken yapı aynı kalır:

```text
LAB-1024
LAB-2048
LAB-9001
```

Her değer için ayrı string yazmak yerine şöyle bir regex kullanılabilir:

```yara
$ticket = /LAB-[0-9]{4}/
```

Bunun basit anlamı:

```text
LAB-        -> birebir aranacak metin
[0-9]       -> tek bir rakam
{4}         -> bu rakam desenini tam 4 kez bekle
```

Bu nedenle `LAB-2048` eşleşebilirken `LAB-20A8` eşleşmez.

### Bu lab'de kullanılan rule

```yara
rule Regex_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning YARA regular expressions"
        lab = "06"
        purpose = "education"

    strings:
        $ticket = /LAB-[0-9]{4}/
        $user = /user_[a-z]{3,8}/ nocase

    condition:
        $ticket and $user
}
```

### İkinci regex

```yara
$user = /user_[a-z]{3,8}/ nocase
```

Şunu arar:

- önce `user_` metni
- ardından 3 ile 8 arasında harf
- `nocase` nedeniyle büyük/küçük harf fark etmez

Örnek eşleşmeler:

```text
user_rafale
USER_TEST
user_admin
```

### Condition bölümü

```yara
condition:
    $ticket and $user
```

kullanıldığı için dosyada iki pattern'ın da bulunması gerekir.

Regex sadece aranacak pattern'ı tarif eder. Rule'un eşleşip eşleşmeyeceğine son olarak yine `condition` karar verir.

### Lab'i çalıştırma

Eşleşen örnek:

```console
yara labs/06-regular-expressions/regex.yar labs/06-regular-expressions/sample-match.txt
```

Beklenen çıktı:

```text
Regex_Demo labs/06-regular-expressions/sample-match.txt
```

Eşleşmeyen örnek:

```console
yara labs/06-regular-expressions/regex.yar labs/06-regular-expressions/sample-no-match.txt
```

Burada çıktı olmaması beklenir.

### Ana çıkarım

```text
exact string -> değer tamamen sabitse iyi seçim
regex        -> yapı sabit ama değerin bir bölümü değişiyorsa kullanışlı
condition    -> son eşleşme kararını yine verir
```

Regex güçlüdür fakat fazla geniş yazılırsa false positive üretebilir. Bu yüzden mümkün olduğunca spesifik tutulmalı ve hem eşleşen hem eşleşmeyen örneklerle test edilmelidir.
