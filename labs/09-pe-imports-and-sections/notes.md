# Lab 09 - PE Imports and Sections / PE Import'ları ve Section'lar

## English

### Goal

Learn how YARA's `pe` module can inspect imported functions and basic PE section information instead of relying only on raw strings or byte signatures.

### Why this matters

Windows PE files contain structured information that can be useful during triage. Two important examples are:

- imported DLLs and API functions
- sections such as `.text`, `.data`, and `.rdata`

YARA can inspect this structure through the `pe` module.

### Rule used in this lab

```yara
import "pe"

rule PE_Imports_And_Sections_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning PE imports and sections"
        lab = "09"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        pe.imports("KERNEL32.dll", "GetLastError")
}
```

### `pe.imports()`

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

This checks whether the PE import table contains the specified DLL and API function.

An import tells us that a program references functionality from another library. It does **not** by itself tell us whether the file is malicious.

For example, common Windows programs may import functions from `KERNEL32.dll`.

### Section count

```yara
pe.number_of_sections > 0
```

A PE file is divided into sections. Common section names can include:

```text
.text   -> executable code
.data   -> writable initialized data
.rdata  -> read-only data
```

Exact section names and layouts can vary between binaries and compilers.

### Looking at section names

YARA can iterate over PE sections. A later rule could use a pattern such as:

```yara
for any section in pe.sections : (
    section.name == ".text"
)
```

The important idea for this lab is to recognize that sections are structured PE data, not ordinary text searched across the whole file.

### Relationship with reverse engineering

In Ghidra or another PE analysis tool, an analyst often inspects:

```text
PE file
  -> sections
  -> imports
  -> strings
  -> functions
```

YARA can use some of the same structural clues for fast filtering before deeper analysis.

### Important limitation

A common import is not a malware indicator by itself.

Good YARA rules usually combine multiple meaningful clues instead of saying:

```text
one API exists -> malware
```

The purpose of this lab is only to learn the PE module syntax and structure-aware matching.

### Try the lab

Use a known benign Windows PE file in your own lab environment:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar /path/to/sample.exe
```

Whether it matches depends on whether that PE imports `GetLastError` from `KERNEL32.dll`.

### Main takeaway

```text
raw bytes / strings -> content-based clues
pe.imports()        -> imported DLL/API information
pe.sections         -> section structure
condition           -> combine clues into one decision
```

---

## Türkçe

### Amaç

YARA'nın `pe` modülüyle yalnızca ham string veya byte imzalarına bakmak yerine PE dosyasının import ve section bilgilerini incelemeyi öğrenmek.

### Neden önemli?

Windows PE dosyalarında analiz sırasında işe yarayan yapısal bilgiler bulunur. Bunların önemli örnekleri:

- import edilen DLL ve API fonksiyonları
- `.text`, `.data`, `.rdata` gibi section'lar

YARA bu bilgileri `pe` modülü üzerinden okuyabilir.

### Bu lab'de kullanılan rule

```yara
import "pe"

rule PE_Imports_And_Sections_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning PE imports and sections"
        lab = "09"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        pe.imports("KERNEL32.dll", "GetLastError")
}
```

### `pe.imports()` ne yapıyor?

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

PE import table içinde belirtilen DLL ve API fonksiyonunun bulunup bulunmadığını kontrol eder.

Bir import, programın başka bir kütüphanedeki fonksiyonu kullandığını gösterir. **Tek başına zararlılık göstergesi değildir.**

### Section sayısı

```yara
pe.number_of_sections > 0
```

PE dosyaları section'lara ayrılır. Sık görülen örnekler:

```text
.text   -> çalıştırılabilir kod
.data   -> yazılabilir ve başlangıç değeri olan veri
.rdata  -> salt okunur veri
```

Section isimleri ve düzeni compiler'a ve binary'ye göre değişebilir.

### Section isimlerine bakmak

YARA PE section'ları üzerinde dolaşabilir. Örneğin daha sonraki bir rule şu yapıyı kullanabilir:

```yara
for any section in pe.sections : (
    section.name == ".text"
)
```

Buradaki ana fikir, section bilgisinin tüm dosyada aranan sıradan bir string değil, parse edilmiş PE yapısının parçası olduğudur.

### Reverse engineering bağlantısı

Ghidra veya başka bir PE analiz aracında genellikle şu akış görülür:

```text
PE dosyası
  -> section'lar
  -> import'lar
  -> string'ler
  -> fonksiyonlar
```

YARA da daha derin analize geçmeden önce bu yapısal ipuçlarının bir kısmını hızlı filtreleme için kullanabilir.

### Önemli sınırlama

Sıradan bir Windows API import'u tek başına malware göstergesi değildir.

İyi YARA rule'ları genellikle tek bir yaygın API yerine birden fazla anlamlı özelliği birlikte değerlendirir.

Bu lab'ın amacı detection üretmek değil, PE modülü söz dizimini ve structure-aware matching mantığını öğrenmektir.

### Lab'i deneme

Kendi güvenli lab ortamında bilinen zararsız bir Windows PE dosyasıyla çalıştırabilirsin:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar /path/to/sample.exe
```

Dosyanın `KERNEL32.dll` üzerinden `GetLastError` import edip etmemesine göre sonuç değişir.

### Ana çıkarım

```text
ham byte / string -> içerik tabanlı ipuçları
pe.imports()      -> DLL/API import bilgisi
pe.sections       -> section yapısı
condition         -> ipuçlarını tek kararda birleştirir
```
