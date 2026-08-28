# Lab 02 - Multiple Strings and Conditions / Birden Fazla String ve Koşullar

## English

### Goal

Learn how multiple YARA strings can be combined with Boolean and counting conditions, then test the rule against harmless positive and negative samples.

### Why use more than one string?

A rule based on one common string can match many benign files. Combining several independent indicators can make a rule more specific and reduce false positives.

That does **not** mean that `2 of them` or `all of them` automatically creates a good rule. The quality and specificity of the strings still matter.

### Rule used in this lab

```yara
rule Suspicious_Download_Pattern
{
    strings:
        $download = "DOWNLOAD_FILE"
        $execute  = "EXECUTE_FILE"
        $network  = "REMOTE_SERVER"

    condition:
        2 of them
}
```

The rule defines three harmless practice markers. The condition requires at least two of them to appear in the scanned file.

### Understanding the condition

Useful condition forms include:

```yara
1 of them
2 of them
any of them
all of them
```

- `1 of them` means at least one defined string must match.
- `2 of them` means at least two must match.
- `any of them` means any one of the strings is enough.
- `all of them` means every defined string must match.

You can also combine named strings directly:

```yara
condition:
    $download and $execute
```

or:

```yara
condition:
    $download or $network
```

### Positive test

`sample-match.txt` contains:

```text
DOWNLOAD_FILE
REMOTE_SERVER
```

Two strings match, so the rule should match.

Run from the repository root:

```console
yara labs/02-multiple-strings-and-conditions/multiple_strings.yar labs/02-multiple-strings-and-conditions/sample-match.txt
```

Expected output:

```text
Suspicious_Download_Pattern labs/02-multiple-strings-and-conditions/sample-match.txt
```

### Negative test

`sample-no-match.txt` contains only one marker:

```text
DOWNLOAD_FILE
```

Because the rule requires two matches, YARA should produce no output.

```console
yara labs/02-multiple-strings-and-conditions/multiple_strings.yar labs/02-multiple-strings-and-conditions/sample-no-match.txt
```

### What I learned

- A YARA rule can define multiple strings.
- Conditions decide how those strings are combined.
- `and`, `or`, `any of them`, `all of them`, and counted conditions provide different levels of strictness.
- Combining indicators can reduce false positives, but only when the indicators themselves are meaningful.
- Positive and negative samples should both be tested.

---

## Türkçe

### Amaç

Birden fazla YARA string'inin Boolean ve sayısal koşullarla nasıl birleştirildiğini öğrenmek ve rule'u zararsız pozitif/negatif örnekler üzerinde test etmek.

### Neden birden fazla string kullanılır?

Tek ve yaygın bir string'e dayanan rule çok sayıda zararsız dosyayla eşleşebilir. Birbirinden bağımsız birkaç göstergenin birlikte aranması rule'u daha spesifik hâle getirebilir ve false positive ihtimalini azaltabilir.

Ancak `2 of them` veya `all of them` kullanmak tek başına kaliteli bir rule oluşturmaz. String'lerin ne kadar anlamlı ve spesifik olduğu hâlâ önemlidir.

### Bu lab'de kullanılan rule

```yara
rule Suspicious_Download_Pattern
{
    strings:
        $download = "DOWNLOAD_FILE"
        $execute  = "EXECUTE_FILE"
        $network  = "REMOTE_SERVER"

    condition:
        2 of them
}
```

Rule üç zararsız alıştırma marker'ı tanımlar. Koşul, taranan dosyada bunlardan en az ikisinin bulunmasını ister.

### Koşulu anlamak

Sık kullanılan bazı koşullar:

```yara
1 of them
2 of them
any of them
all of them
```

- `1 of them`: tanımlanan string'lerden en az biri eşleşmelidir.
- `2 of them`: en az iki string eşleşmelidir.
- `any of them`: string'lerden herhangi biri yeterlidir.
- `all of them`: tanımlanan bütün string'ler eşleşmelidir.

String'leri isimleriyle de birleştirebiliriz:

```yara
condition:
    $download and $execute
```

veya:

```yara
condition:
    $download or $network
```

### Pozitif test

`sample-match.txt` içinde şu iki marker bulunur:

```text
DOWNLOAD_FILE
REMOTE_SERVER
```

İki string eşleştiği için rule eşleşmelidir.

Repo kök dizininden:

```console
yara labs/02-multiple-strings-and-conditions/multiple_strings.yar labs/02-multiple-strings-and-conditions/sample-match.txt
```

Beklenen çıktı:

```text
Suspicious_Download_Pattern labs/02-multiple-strings-and-conditions/sample-match.txt
```

### Negatif test

`sample-no-match.txt` yalnızca tek marker içerir:

```text
DOWNLOAD_FILE
```

Rule iki eşleşme istediği için YARA çıktı vermemelidir.

```console
yara labs/02-multiple-strings-and-conditions/multiple_strings.yar labs/02-multiple-strings-and-conditions/sample-no-match.txt
```

### Ne öğrendim?

- Bir YARA rule'u birden fazla string tanımlayabilir.
- `condition` bölümü bu string'lerin nasıl birleştirileceğini belirler.
- `and`, `or`, `any of them`, `all of them` ve sayısal koşullar farklı katılık seviyeleri sağlar.
- Birden fazla göstergeyi birleştirmek false positive oranını azaltabilir, ancak göstergelerin kendisi anlamlı olmalıdır.
- Rule test edilirken hem eşleşmesi gereken hem de eşleşmemesi gereken örnekler kullanılmalıdır.
