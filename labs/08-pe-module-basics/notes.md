# Lab 08 - PE Module Basics / PE Module Temelleri

## English

### Goal

Learn how YARA can use the `pe` module to reason about Windows Portable Executable files instead of relying only on raw strings or byte patterns.

### What is the PE module?

YARA modules expose structured information about some file formats. The `pe` module parses Portable Executable files and gives rules access to fields such as machine type, section count, entry point information, imports, and other PE metadata.

To use it, the rule starts with:

```yara
import "pe"
```

### Rule used in this lab

```yara
import "pe"

rule PE_Module_Basics
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning basic PE-aware YARA conditions"
        lab = "08"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        (pe.machine == pe.MACHINE_I386 or pe.machine == pe.MACHINE_AMD64)
}
```

### Breaking down the condition

```yara
uint16(0) == 0x5A4D
```

Checks the first two bytes for the classic `MZ` signature used by PE files.

```yara
pe.number_of_sections > 0
```

Asks the PE parser whether the file has at least one PE section.

```yara
pe.machine == pe.MACHINE_I386
```

Checks whether the PE targets 32-bit x86.

```yara
pe.machine == pe.MACHINE_AMD64
```

Checks whether the PE targets 64-bit x86-64.

The rule accepts either architecture.

### Why this is better than only checking `MZ`

A file beginning with `MZ` is not automatically a valid Windows executable. A stronger rule combines the raw header check with parsed PE properties.

That gives us this progression:

```text
raw bytes -> file structure -> parsed metadata -> stronger condition
```

### How to test safely

Use a harmless executable that you compiled yourself, then scan it with:

```console
yara labs/08-pe-module-basics/pe_basics.yar /path/to/hello.exe
```

This lab does not include malware samples.

### Reverse engineering connection

This is the first lab where YARA begins to overlap more directly with reverse engineering concepts. PE sections, architecture, imports, and entry points are also things you inspect in tools such as Ghidra, PE-bear, or other static-analysis tools.

A useful mental model is:

```text
YARA asks structured questions about the binary
Reverse engineering explains what those structures mean in context
```

### Main takeaway

```text
import "pe"        -> enable PE-aware fields
uint16(0)          -> raw header check
pe.number_of_sections -> structural property
pe.machine         -> target architecture
condition          -> combines all checks
```

A YARA match still means only that the rule condition matched. It does not prove that the file is malicious.

---

## Türkçe

### Amaç

YARA'nın yalnızca string veya ham byte pattern'larına bakmak yerine `pe` modülünü kullanarak Windows Portable Executable dosyalarının yapısal bilgilerini nasıl değerlendirebildiğini öğrenmek.

### PE modülü nedir?

YARA modülleri bazı dosya formatları hakkında yapılandırılmış bilgiler sunar. `pe` modülü Portable Executable dosyalarını parse eder ve rule içinde mimari, section sayısı, entry point, import'lar ve diğer PE bilgilerine erişmeyi sağlar.

Kullanmak için rule'un başına:

```yara
import "pe"
```

eklenir.

### Bu lab'de kullanılan rule

```yara
import "pe"

rule PE_Module_Basics
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning basic PE-aware YARA conditions"
        lab = "08"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        (pe.machine == pe.MACHINE_I386 or pe.machine == pe.MACHINE_AMD64)
}
```

### Condition bölümünü parçalayalım

```yara
uint16(0) == 0x5A4D
```

Dosyanın ilk iki byte'ını kontrol eder. `0x5A4D`, PE dosyalarında gördüğümüz klasik `MZ` imzasıdır.

```yara
pe.number_of_sections > 0
```

PE parser'a dosyanın en az bir section içerip içermediğini sorar.

```yara
pe.machine == pe.MACHINE_I386
```

Dosyanın 32-bit x86 hedefleyip hedeflemediğini kontrol eder.

```yara
pe.machine == pe.MACHINE_AMD64
```

Dosyanın 64-bit x86-64 hedefleyip hedeflemediğini kontrol eder.

Rule iki mimariden birini kabul eder.

### Neden sadece `MZ` kontrolünden daha iyi?

Bir dosyanın `MZ` ile başlaması onun tek başına geçerli bir Windows executable olduğu anlamına gelmez. Daha güçlü bir rule, ham header kontrolünü PE'den parse edilen yapısal bilgilerle birleştirir.

Yani ilerleme şu şekildedir:

```text
ham byte -> dosya yapısı -> parse edilmiş metadata -> daha güçlü condition
```

### Güvenli test

Kendi derlediğin zararsız bir `.exe` dosyasını kullanıp şöyle tarayabilirsin:

```console
yara labs/08-pe-module-basics/pe_basics.yar /path/to/hello.exe
```

Bu lab malware örneği içermez.

### Reverse engineering bağlantısı

Bu lab, YARA ile reverse engineering'in daha net kesişmeye başladığı ilk adımlardan biridir. PE section'ları, mimari, import'lar ve entry point gibi bilgiler Ghidra ve benzeri statik analiz araçlarında da sürekli karşımıza çıkar.

Şöyle düşünebilirsin:

```text
YARA binary hakkında yapısal sorular sorar
Reverse engineering ise bu yapıların bağlam içinde ne anlama geldiğini açıklar
```

### Ana çıkarım

```text
import "pe"           -> PE alanlarını açar
uint16(0)             -> ham header kontrolü
pe.number_of_sections -> yapısal özellik
pe.machine            -> hedef mimari
condition             -> bütün kontrolleri birleştirir
```

Bir YARA eşleşmesinin yalnızca condition'ın sağlandığını gösterdiğini unutma; tek başına malware kanıtı değildir.
