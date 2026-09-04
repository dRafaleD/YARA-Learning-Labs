# Lab 05 - Rule Metadata / Rule Metadata'sı

## English

### Goal

Learn what the `meta` section in a YARA rule is used for and understand that metadata describes a rule but does not decide whether the rule matches.

### What is metadata?

A YARA rule can contain a `meta` section with descriptive information such as:

- author
- description
- lab or version number
- purpose
- reference information

Example:

```yara
meta:
    author = "dRafaleD"
    description = "Harmless practice rule for learning YARA metadata"
    lab = "05"
    purpose = "education"
```

This information helps humans understand and organize rules.

### Important idea

The `meta` section does **not** make a rule match.

The matching decision is still controlled by the `condition` section.

In this lab:

```yara
strings:
    $marker = "YARA_METADATA_LAB"

condition:
    $marker
```

The rule matches only when the marker string is present in the scanned file.

### Rule used in this lab

```yara
rule Metadata_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning YARA metadata"
        lab = "05"
        purpose = "education"

    strings:
        $marker = "YARA_METADATA_LAB"

    condition:
        $marker
}
```

### Run the lab

Matching sample:

```console
yara labs/05-rule-metadata/metadata.yar labs/05-rule-metadata/sample-match.txt
```

Expected result:

```text
Metadata_Demo labs/05-rule-metadata/sample-match.txt
```

Non-matching sample:

```console
yara labs/05-rule-metadata/metadata.yar labs/05-rule-metadata/sample-no-match.txt
```

No match should be printed.

To display rule metadata as well, YARA CLI can be run with metadata output enabled:

```console
yara -m labs/05-rule-metadata/metadata.yar labs/05-rule-metadata/sample-match.txt
```

### Why metadata matters in real rule collections

When a rule repository grows, descriptive metadata becomes useful for maintenance. It can help answer questions such as:

- Who wrote this rule?
- What is the rule intended to detect?
- Is it a training rule or a production rule?
- Which version or case does it belong to?

Good metadata improves organization, but good metadata cannot compensate for a poor detection condition.

### Main takeaway

```text
meta      -> information about the rule
strings   -> patterns the rule can search for
condition -> logic that decides whether the rule matches
```

A YARA match still means only that the rule condition was satisfied. It is not automatically proof that a file is malicious.

---

## Türkçe

### Amaç

YARA rule'larında kullanılan `meta` bölümünün ne işe yaradığını öğrenmek ve metadata'nın bir rule'un eşleşip eşleşmeyeceğine karar vermediğini anlamak.

### Metadata nedir?

Bir YARA rule'u, rule hakkında açıklayıcı bilgiler tutan bir `meta` bölümü içerebilir.

Örneğin:

- yazar
- açıklama
- lab veya sürüm numarası
- kullanım amacı
- referans bilgileri

```yara
meta:
    author = "dRafaleD"
    description = "Harmless practice rule for learning YARA metadata"
    lab = "05"
    purpose = "education"
```

Bu bilgiler YARA'nın eşleşme mantığından çok, insanların rule'u anlamasına ve düzenlemesine yardımcı olur.

### En önemli nokta

`meta` bölümü tek başına bir eşleşme oluşturmaz.

Bir rule'un eşleşip eşleşmeyeceğini yine `condition` bölümü belirler.

Bu lab'de:

```yara
strings:
    $marker = "YARA_METADATA_LAB"

condition:
    $marker
```

şeklinde basit bir koşul kullanıyoruz.

Dosyanın içinde `YARA_METADATA_LAB` bulunursa rule eşleşir; metadata bilgileri bu sonucu değiştirmez.

### Kullanılan rule

```yara
rule Metadata_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning YARA metadata"
        lab = "05"
        purpose = "education"

    strings:
        $marker = "YARA_METADATA_LAB"

    condition:
        $marker
}
```

### Lab'i çalıştırma

Eşleşen örnek:

```console
yara labs/05-rule-metadata/metadata.yar labs/05-rule-metadata/sample-match.txt
```

Beklenen sonuç:

```text
Metadata_Demo labs/05-rule-metadata/sample-match.txt
```

Eşleşmeyen örnek:

```console
yara labs/05-rule-metadata/metadata.yar labs/05-rule-metadata/sample-no-match.txt
```

Burada çıktı olmaması beklenir.

Metadata'yı çıktı içinde görmek için:

```console
yara -m labs/05-rule-metadata/metadata.yar labs/05-rule-metadata/sample-match.txt
```

kullanılabilir.

### Metadata neden önemlidir?

Rule sayısı arttıkça metadata bakım ve düzen açısından daha değerli hale gelir.

Örneğin şu soruların cevabını kolaylaştırabilir:

- Bu rule'u kim yazdı?
- Rule'un amacı ne?
- Eğitim için mi yoksa gerçek kullanım için mi yazıldı?
- Hangi lab, sürüm veya analiz vakasına ait?

Ancak metadata sadece açıklayıcı bilgidir. Kötü yazılmış bir `condition` bölümünü iyi metadata güvenilir hale getirmez.

### Ana çıkarım

```text
meta      -> rule hakkında açıklayıcı bilgi
strings   -> aranabilecek pattern'lar
condition -> eşleşmeyi belirleyen mantık
```

Bir YARA eşleşmesinin yalnızca rule koşulunun sağlandığını gösterdiğini unutmamak gerekir; tek başına malware kanıtı değildir.
