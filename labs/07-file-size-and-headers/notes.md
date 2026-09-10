# Lab 07 - File Size and Header Checks / Dosya Boyutu ve Header Kontrolleri

## English

### Goal

Learn how YARA can use simple structural information in addition to strings and regex patterns.

In this lab we use:

- `filesize`
- `uint16(0)`
- a simple header check
- multiple conditions joined with `and`

The goal is to understand that YARA can inspect specific byte positions and basic file properties, not only search for text.

### Rule used in this lab

```yara
rule File_Header_And_Size_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning filesize and header checks"
        lab = "07"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and filesize < 1KB
}
```

### `uint16(0)`

`uint16(0)` tells YARA to read a 16-bit unsigned integer starting at offset `0`, which is the very beginning of the file.

This lab checks:

```yara
uint16(0) == 0x5A4D
```

On a little-endian system, the bytes `4D 5A` correspond to the characters `MZ`.

This is commonly associated with DOS/PE-style executable headers, but the sample in this lab is only harmless text that starts with `MZ` for practice.

### `filesize`

YARA provides the special value `filesize` for checking the size of the scanned file.

This lab uses:

```yara
filesize < 1KB
```

So the rule requires both conditions to be true:

```text
first bytes look like MZ
AND
file is smaller than 1 KB
```

### Why combine conditions?

A single indicator can be too broad.

For example, a file may contain `MZ` somewhere by coincidence. By checking the beginning of the file and adding a size condition, the rule becomes more specific.

This does not make the rule production-ready. It only demonstrates how multiple structural checks can work together.

### Run the lab

Matching sample:

```console
yara labs/07-file-size-and-headers/structure_conditions.yar labs/07-file-size-and-headers/sample-match.txt
```

Expected output:

```text
File_Header_And_Size_Demo labs/07-file-size-and-headers/sample-match.txt
```

Non-matching sample:

```console
yara labs/07-file-size-and-headers/structure_conditions.yar labs/07-file-size-and-headers/sample-no-match.txt
```

No output is expected.

### Main takeaway

```text
strings/regex -> search for patterns
uint16(offset) -> read bytes from a specific location
filesize       -> check file size
condition      -> combine these checks into matching logic
```

This is the first step toward writing rules that care about file structure instead of only visible text.

---

## Türkçe

### Amaç

YARA'nın yalnızca string veya regex aramakla kalmayıp dosyanın basit yapısal özelliklerini de kontrol edebildiğini öğrenmek.

Bu lab'de şunları kullanıyoruz:

- `filesize`
- `uint16(0)`
- basit bir header kontrolü
- `and` ile birden fazla koşulu birleştirme

### Kullanılan rule

```yara
rule File_Header_And_Size_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning filesize and header checks"
        lab = "07"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and filesize < 1KB
}
```

### `uint16(0)` ne demek?

`uint16(0)`, YARA'ya dosyanın `0` offsetinden başlayarak 16-bit unsigned bir değer okumasını söyler.

Offset `0`, dosyanın en başıdır.

Bu lab şu kontrolü yapıyor:

```yara
uint16(0) == 0x5A4D
```

Little-endian gösterimde `4D 5A` byte'ları `MZ` karakterlerine karşılık gelir.

`MZ`, DOS/PE tarzı executable header'larıyla ilişkilidir. Fakat bu lab'deki örnek gerçek bir executable değildir; sadece güvenli alıştırma amacıyla `MZ` ile başlayan normal bir metin dosyasıdır.

### `filesize`

YARA, taranan dosyanın boyutunu kontrol etmek için `filesize` isimli özel bir değer sağlar.

Bu lab'de:

```yara
filesize < 1KB
```

kullanıyoruz.

Yani rule'un eşleşmesi için iki şart da doğru olmalı:

```text
dosyanın başlangıcı MZ gibi görünecek
VE
dosya 1 KB'den küçük olacak
```

### Neden birden fazla koşul?

Tek bir gösterge çoğu zaman fazla geniş olabilir.

Örneğin `MZ` tek başına her zaman anlamlı değildir. Header konumunu ve başka bir özelliği birlikte kontrol etmek rule'u biraz daha spesifik hale getirir.

Bu örnek production seviyesinde bir detection rule değildir. Ama YARA'da yapısal koşulların nasıl birleştirildiğini göstermek için iyi bir başlangıçtır.

### Lab'i çalıştırma

Eşleşen örnek:

```console
yara labs/07-file-size-and-headers/structure_conditions.yar labs/07-file-size-and-headers/sample-match.txt
```

Beklenen çıktı:

```text
File_Header_And_Size_Demo labs/07-file-size-and-headers/sample-match.txt
```

Eşleşmeyen örnek:

```console
yara labs/07-file-size-and-headers/structure_conditions.yar labs/07-file-size-and-headers/sample-no-match.txt
```

Burada çıktı beklenmez.

### Ana çıkarım

```text
strings/regex -> pattern arar
uint16(offset) -> belirli bir konumdan byte okur
filesize       -> dosya boyutunu kontrol eder
condition      -> tüm kontrolleri eşleşme mantığında birleştirir
```

Bu lab, sadece görünür metinleri aramaktan dosya yapısını incelemeye geçiş için ilk adımdır.
