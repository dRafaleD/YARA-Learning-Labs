# Lab 03 - String Modifiers / String Modifier'ları

## English

### Goal

Learn how the `nocase`, `ascii`, and `wide` modifiers change the way YARA searches for text, then verify the behavior with harmless samples.

### Why modifiers matter

The same text can appear in different forms inside a file. A program may store a string with different letter casing, as ordinary single-byte text, or in a two-byte representation commonly seen in Windows binaries.

YARA string modifiers let a rule describe these variations without creating a separate string for every representation.

### Rules used in this lab

```yara
rule NoCase_Demo
{
    strings:
        $marker = "HELLO_YARA" nocase

    condition:
        $marker
}

rule ASCII_Wide_Demo
{
    strings:
        $marker = "WIDE_MARKER" ascii wide

    condition:
        $marker
}
```

### `nocase`

By default, a YARA text string is case-sensitive.

```yara
$marker = "HELLO_YARA"
```

would not match `hello_yara`.

Adding `nocase` makes the comparison case-insensitive:

```yara
$marker = "HELLO_YARA" nocase
```

`sample-case.txt` deliberately contains the lowercase form:

```text
hello_yara
```

Run:

```console
yara labs/03-string-modifiers/string_modifiers.yar labs/03-string-modifiers/sample-case.txt
```

Expected match:

```text
NoCase_Demo labs/03-string-modifiers/sample-case.txt
```

### `ascii` and `wide`

`ascii` searches for the ordinary single-byte representation of the text. For normal YARA text strings this is already the default behavior, but writing it explicitly is useful when it is combined with `wide`.

```yara
$marker = "WIDE_MARKER" ascii wide
```

This tells YARA to search for both the ASCII form and the wide form.

The committed `sample-wide.txt` is a harmless UTF-16LE practice file containing `WIDE_MARKER`. Its bytes therefore resemble:

```text
57 00 49 00 44 00 45 00 ...
 W     I     D     E
```

Run:

```console
yara labs/03-string-modifiers/string_modifiers.yar labs/03-string-modifiers/sample-wide.txt
```

Expected match:

```text
ASCII_Wide_Demo labs/03-string-modifiers/sample-wide.txt
```

> `wide` should not be understood as a complete Unicode text engine. For a basic YARA text string, it searches the two-byte form produced by inserting a zero byte after each character. This is especially useful for many UTF-16LE-like strings found in Windows files.

### Negative test

`sample-no-match.txt` contains neither practice marker.

```console
yara labs/03-string-modifiers/string_modifiers.yar labs/03-string-modifiers/sample-no-match.txt
```

Expected result: no output.

### What I learned

- YARA text strings are case-sensitive by default.
- `nocase` allows a string to match regardless of letter case.
- `ascii` searches the single-byte representation.
- `wide` searches the two-byte zero-padded representation commonly useful for Windows strings.
- `ascii wide` lets the same rule look for both representations.
- Modifiers make a rule more flexible, but broader matching can also increase false positives, so the surrounding indicators and condition still matter.

---

## Türkçe

### Amaç

`nocase`, `ascii` ve `wide` modifier'larının YARA'nın metin arama şeklini nasıl değiştirdiğini öğrenmek ve davranışı zararsız örnek dosyalarla doğrulamak.

### Modifier'lar neden önemlidir?

Aynı metin bir dosyanın içinde farklı biçimlerde bulunabilir. Bir program string'i farklı büyük-küçük harflerle, normal tek baytlık metin olarak veya özellikle Windows binary'lerinde sık görülen iki baytlık bir gösterimde saklayabilir.

YARA string modifier'ları, her temsil için ayrı string yazmak yerine bu farklılıkları rule içinde tanımlamamızı sağlar.

### Bu lab'de kullanılan rule'lar

```yara
rule NoCase_Demo
{
    strings:
        $marker = "HELLO_YARA" nocase

    condition:
        $marker
}

rule ASCII_Wide_Demo
{
    strings:
        $marker = "WIDE_MARKER" ascii wide

    condition:
        $marker
}
```

### `nocase`

YARA text string'leri varsayılan olarak büyük-küçük harfe duyarlıdır.

```yara
$marker = "HELLO_YARA"
```

normalde `hello_yara` ile eşleşmez.

`nocase` eklediğimizde büyük-küçük harf farkı önemini kaybeder:

```yara
$marker = "HELLO_YARA" nocase
```

`sample-case.txt` bilerek küçük harfli biçimi içerir:

```text
hello_yara
```

Çalıştırın:

```console
yara labs/03-string-modifiers/string_modifiers.yar labs/03-string-modifiers/sample-case.txt
```

Beklenen eşleşme:

```text
NoCase_Demo labs/03-string-modifiers/sample-case.txt
```

### `ascii` ve `wide`

`ascii`, metnin normal tek baytlık temsilini arar. Normal YARA text string'lerinde bu zaten varsayılan davranıştır; fakat `wide` ile beraber kullanıldığında açıkça yazmak faydalıdır.

```yara
$marker = "WIDE_MARKER" ascii wide
```

Bu kullanım YARA'ya hem ASCII hem de wide gösterimi aramasını söyler.

Repodaki `sample-wide.txt`, `WIDE_MARKER` içeren tamamen zararsız bir UTF-16LE alıştırma dosyasıdır. Bu nedenle byte'ları yaklaşık olarak şöyle görünür:

```text
57 00 49 00 44 00 45 00 ...
 W     I     D     E
```

Çalıştırın:

```console
yara labs/03-string-modifiers/string_modifiers.yar labs/03-string-modifiers/sample-wide.txt
```

Beklenen eşleşme:

```text
ASCII_Wide_Demo labs/03-string-modifiers/sample-wide.txt
```

> `wide`, tam kapsamlı bir Unicode metin motoru olarak düşünülmemelidir. Temel YARA text string'lerinde karakterlerin arasına sıfır baytı eklenmiş iki baytlık gösterimi arar. Bu özellikle Windows dosyalarında görülen birçok UTF-16LE benzeri string için kullanışlıdır.

### Negatif test

`sample-no-match.txt` iki alıştırma marker'ını da içermez.

```console
yara labs/03-string-modifiers/string_modifiers.yar labs/03-string-modifiers/sample-no-match.txt
```

Beklenen sonuç: çıktı olmaması.

### Ne öğrendim?

- YARA text string'leri varsayılan olarak büyük-küçük harfe duyarlıdır.
- `nocase`, harf büyüklüğünü önemsemeden eşleşme sağlar.
- `ascii`, tek baytlık metin gösterimini arar.
- `wide`, özellikle Windows string'lerinde yararlı olan sıfır baytlı iki baytlık gösterimi arar.
- `ascii wide`, aynı string'in iki temsilini de aramamızı sağlar.
- Modifier'lar rule'u daha esnek hâle getirir; ancak eşleşmeyi genişletmek false positive ihtimalini de artırabilir. Bu nedenle condition ve diğer göstergeler hâlâ önemlidir.
