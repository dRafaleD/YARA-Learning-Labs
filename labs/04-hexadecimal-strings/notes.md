# Lab 04 - Hexadecimal Strings / Hexadecimal String'ler

## English

### Goal

Learn how YARA can match raw byte sequences with hexadecimal strings and understand the difference between searching for readable text and searching for bytes.

### Why hexadecimal patterns matter

Not every useful indicator inside a file is readable text. Executables and other binary files contain machine code, headers, constants, and structured byte sequences.

YARA can describe these byte patterns inside braces:

```yara
$pattern = { 48 45 58 5F 4C 41 42 }
```

Each pair represents one byte written in hexadecimal.

For example:

```text
48 45 58
 H  E  X
```

The bytes can represent text, but hexadecimal strings are especially useful when the pattern we care about is naturally described as bytes.

### Rule used in this lab

```yara
rule Hex_Exact_Demo
{
    strings:
        $hex_marker = { 48 45 58 5F 4C 41 42 }

    condition:
        $hex_marker
}

rule Hex_Wildcard_Demo
{
    strings:
        $pattern = { 41 42 ?? 44 45 }

    condition:
        $pattern
}
```

### Exact hexadecimal bytes

The first rule searches for this exact sequence:

```text
48 45 58 5F 4C 41 42
```

which corresponds to:

```text
HEX_LAB
```

The rule is intentionally simple so the relationship between bytes and the matching result is easy to inspect.

Scan the matching sample:

```console
yara labs/04-hexadecimal-strings/hex_strings.yar labs/04-hexadecimal-strings/sample-match.bin
```

Expected matches include:

```text
Hex_Exact_Demo labs/04-hexadecimal-strings/sample-match.bin
```

### Wildcard byte: `??`

YARA hexadecimal strings can contain wildcards.

```yara
$pattern = { 41 42 ?? 44 45 }
```

Here `??` means:

> Any byte is accepted at this position.

Therefore all of these satisfy the pattern:

```text
41 42 43 44 45
41 42 FF 44 45
41 42 00 44 45
```

Only the third byte is allowed to vary.

This is useful when most of a byte sequence is stable but one position can change.

### Why not use `??` everywhere?

A very broad pattern such as:

```yara
{ ?? ?? ?? ?? }
```

matches an enormous number of files and has almost no identifying value.

A useful YARA rule tries to balance:

```text
flexibility
    +
specificity
```

Wildcards should describe bytes that genuinely vary, not simply make a rule easier to match.

### Negative test

`sample-no-match.bin` does not contain the practice patterns.

Run:

```console
yara labs/04-hexadecimal-strings/hex_strings.yar labs/04-hexadecimal-strings/sample-no-match.bin
```

Expected result: no output.

### Text string vs hexadecimal string

These two ideas can sometimes describe the same bytes:

```yara
$text = "HEX_LAB"
```

and:

```yara
$hex = { 48 45 58 5F 4C 41 42 }
```

But they communicate different intent.

A text string says:

> Find this readable text.

A hexadecimal string says:

> Find this sequence of bytes.

When analyzing binary structures or machine-code patterns, the byte-oriented form is often more natural.

### Mini exercise

Before changing the rule, predict the result.

1. Replace `??` with `43`. Does the wildcard sample still match?
2. Replace it with `FF`. What changes?
3. Add another wildcard. Does the rule become more or less specific?
4. Convert `HEX_LAB` to hexadecimal manually and compare it with the rule.

### What I learned

- YARA can search for raw byte sequences with hexadecimal strings.
- Hexadecimal strings are written inside `{ }`.
- Each two-digit hexadecimal value normally represents one byte.
- `??` accepts any byte at that position.
- Wildcards make patterns more flexible but also less specific.
- A YARA match is still only evidence that the rule condition matched; it is not proof that a file is malicious.

---

## Türkçe

### Amaç

YARA'nın hexadecimal string'ler kullanarak ham byte dizilerini nasıl eşleştirdiğini öğrenmek ve okunabilir metin aramakla doğrudan byte aramak arasındaki farkı anlamak.

### Hexadecimal pattern'lar neden önemli?

Bir dosyadaki her yararlı gösterge okunabilir metin değildir. Executable dosyalar; machine code, header'lar, sabit değerler ve çeşitli yapısal byte dizileri içerir.

YARA bu byte pattern'larını süslü parantez içinde tanımlayabilir:

```yara
$pattern = { 48 45 58 5F 4C 41 42 }
```

Her ikili hexadecimal sayı bir byte'ı temsil eder.

Örneğin:

```text
48 45 58
 H  E  X
```

Byte'lar bazen metni temsil edebilir; fakat hexadecimal string'lerin asıl gücü, aradığımız yapının byte olarak ifade edilmesinin daha doğal olduğu durumlarda ortaya çıkar.

### Bu lab'de kullanılan rule

```yara
rule Hex_Exact_Demo
{
    strings:
        $hex_marker = { 48 45 58 5F 4C 41 42 }

    condition:
        $hex_marker
}

rule Hex_Wildcard_Demo
{
    strings:
        $pattern = { 41 42 ?? 44 45 }

    condition:
        $pattern
}
```

### Tam hexadecimal byte eşleşmesi

İlk rule şu byte dizisini birebir arar:

```text
48 45 58 5F 4C 41 42
```

ASCII olarak bu:

```text
HEX_LAB
```

metnine karşılık gelir.

Burada özellikle basit bir örnek kullanıyoruz; amaç byte ile eşleşme arasındaki ilişkiyi net görmek.

Matching sample'ı tarayın:

```console
yara labs/04-hexadecimal-strings/hex_strings.yar labs/04-hexadecimal-strings/sample-match.bin
```

Beklenen eşleşmeler arasında:

```text
Hex_Exact_Demo labs/04-hexadecimal-strings/sample-match.bin
```

bulunur.

### Wildcard byte: `??`

YARA hexadecimal string'lerinde wildcard kullanılabilir:

```yara
$pattern = { 41 42 ?? 44 45 }
```

Buradaki `??`:

> Bu konumda herhangi bir byte olabilir.

anlamına gelir.

Bu nedenle:

```text
41 42 43 44 45
41 42 FF 44 45
41 42 00 44 45
```

dizilerinin tamamı pattern'ı karşılar.

Yalnızca üçüncü byte değişkendir.

Bu özellik, byte dizisinin büyük bölümü sabitken belirli bir kısmı değişebiliyorsa kullanışlıdır.

### Neden her yere `??` koymuyoruz?

Şöyle bir pattern:

```yara
{ ?? ?? ?? ?? }
```

çok fazla dosyayla eşleşebilir ve neredeyse hiçbir ayırt edici değer taşımaz.

İyi bir YARA rule'u şu ikisi arasında denge kurmaya çalışır:

```text
esneklik
   +
özgüllük
```

Wildcard'lar gerçekten değişebilen byte'ları temsil etmek için kullanılmalıdır.

### Negatif test

`sample-no-match.bin`, alıştırmadaki pattern'ları içermez.

```console
yara labs/04-hexadecimal-strings/hex_strings.yar labs/04-hexadecimal-strings/sample-no-match.bin
```

Beklenen sonuç: çıktı olmaması.

### Text string ile hexadecimal string farkı

Bazen aynı byte'ları iki farklı şekilde ifade edebiliriz:

```yara
$text = "HEX_LAB"
```

ve:

```yara
$hex = { 48 45 58 5F 4C 41 42 }
```

Ancak anlattıkları niyet farklıdır.

Text string:

> Bu okunabilir metni bul.

Hexadecimal string:

> Bu byte dizisini bul.

Binary yapıları veya machine-code pattern'ları incelerken byte odaklı gösterim çoğu zaman daha doğaldır.

### Mini alıştırma

Rule'u değiştirmeden önce sonucu tahmin etmeye çalış:

1. `??` yerine `43` koyarsan wildcard sample hâlâ eşleşir mi?
2. Yerine `FF` koyarsan ne değişir?
3. Bir wildcard daha eklersen rule daha mı spesifik olur, daha mı genel?
4. `HEX_LAB` metnini kendin hexadecimal'e çevirip rule ile karşılaştır.

### Ne öğrendim?

- YARA hexadecimal string'lerle ham byte dizilerini arayabilir.
- Hexadecimal string'ler `{ }` içinde yazılır.
- İki basamaklı her hexadecimal değer normalde bir byte'ı temsil eder.
- `??`, bulunduğu konumda herhangi bir byte'ın kabul edilmesini sağlar.
- Wildcard kullanımı pattern'ı esnekleştirirken özgüllüğünü azaltabilir.
- Bir YARA eşleşmesi yalnızca rule koşulunun sağlandığını gösterir; tek başına dosyanın zararlı olduğunu kanıtlamaz.
