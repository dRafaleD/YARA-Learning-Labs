# Lab 09 - PE Imports and Sections / PE Import'ları ve Section'lar

## English

### Goal

Learn how YARA's `pe` module can inspect imported functions and basic PE section information instead of relying only on raw strings or byte signatures.

After this lab you should be able to:

- explain `pe.imports("KERNEL32.dll", "GetLastError")` word by word
- tell the difference between searching for an API name as text and asking the PE import table
- treat sections as parsed PE data, not as ordinary strings
- combine this lab with the header and PE checks from Labs 07 and 08
- remember that a common Windows API is not a malware indicator by itself

### Why this matters

Labs 01 to 06 searched file content. Lab 07 read bytes at a known offset. Lab 08 asked the `pe` module whether a file looks like a Windows PE.

Lab 09 takes the next step: it asks what the PE is linked against, and how the file is divided into sections.

Windows PE files contain structured information that can be useful during triage. Two important examples are:

- imported DLLs and API functions
- sections such as `.text`, `.data`, and `.rdata`

YARA can inspect this structure through the `pe` module.

A useful mental model from reverse-engineering tools is:

```text
PE file
  -> sections
  -> imports
  -> strings
  -> functions
```

YARA can use some of the same structural clues for fast filtering before deeper analysis.

### String search is not an import check

This contrast is the main idea of the lab.

A content rule from Labs 01 to 03 can match any file that contains the text `GetLastError`, including source code, notes, and this lab's text sample:

```yara
rule String_Search_GetLastError
{
    strings:
        $api = "GetLastError"

    condition:
        $api
}
```

`pe.imports()` asks a different question: does the parsed import table list that API from that DLL?

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

| | String search | `pe.imports()` |
| --- | --- | --- |
| Where it looks | Raw file content | Parsed PE import table |
| Matches a `.txt` file | Yes, if the text is present | No, because the file is not a PE |
| What it proves | The bytes/text appeared | The program references that API |
| Malware verdict | No | No |

An import means the program **references** a library function. It does not prove that the function was called at runtime, and it does not prove that the file is malicious.

`pe.imports()` also does not see APIs resolved later by name. That is a limitation of import-table matching, not a bug in the lab.

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

Read the condition as three `and`-combined checks:

- `uint16(0) == 0x5A4D` — Lab 07 raw `MZ` header check
- `pe.number_of_sections > 0` — Lab 08 parsed PE property
- `pe.imports("KERNEL32.dll", "GetLastError")` — today's new check

`meta` still describes the rule and does not decide the match. Enable it on the command line with `yara -m` if you want to display those fields.

### `pe.imports()`

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

This checks whether the PE import table contains the specified DLL and API function.

For this lab, three forms are enough. The DLL name is case-insensitive.

**1. Named function, boolean result** — the form used by the lab rule:

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

`kernel32.dll` and `KERNEL32.dll` are treated the same. The function name should be written as it appears in the import table; do not change it to `getlasterror`.

**2. Import count from a DLL** — useful when you only need to know that `kernel32.dll` is present:

```yara
pe.imports("kernel32.dll") >= 1
```

From YARA 4.0 onward this form returns a number. Any value greater than `0` also counts as true.

**3. Regular expressions** — a bridge to Lab 06, shown here only as a board example:

```yara
pe.imports(/kernel32\.dll/i, /^GetLastError$/) >= 1
```

In this regex form the names are case-sensitive unless you add `/i`.

This lab stays with **standard imports**. Delayed imports and import-by-ordinal can wait for a later exercise.

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

Exact section names and layouts can vary between binaries and compilers. That is why this lab's main rule checks that at least one section exists instead of requiring one exact name.

### Looking at section names

A section is parsed PE metadata. It is not the same as searching the whole file for the text `.text`.

This content search is the wrong model:

```yara
$s = ".text"
```

YARA can iterate over PE sections. A structure-aware check looks like this:

```yara
for any section in pe.sections : (
    section.name == ".text"
)
```

or, if you index the first section only:

```yara
pe.sections[0].name == ".text"
```

The first form asks whether **any** section is named `.text`. The second form asks whether **section 0** has that name. The first section is not always `.text`, so `for any` is the safer teaching example.

Section characteristics such as execute or write flags are left for a later lab.

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

GetLastError, CloseHandle, and many other KERNEL32 functions appear in ordinary Windows programs. Combining them with `and` still does not create a detection rule unless the clues themselves are specific.

The purpose of this lab is only to learn the PE module syntax and structure-aware matching.

### Try the lab

Use a known benign Windows PE file in your own lab environment. The smallest path is to compile the harmless C sample in this folder:

```c
#include <stdio.h>
#include <windows.h>

int main(void)
{
    DWORD err = GetLastError();
    printf("GetLastError=%lu\n", (unsigned long)err);
    return 0;
}
```

Compile it locally, then scan the resulting executable from the repository root:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar hello.exe
```

Expected match when that PE imports `GetLastError` from `KERNEL32.dll`:

```text
PE_Imports_And_Sections_Demo hello.exe
```

Whether a random benign PE matches depends on its import table. This lab does not include malware samples.

### Contrast test: text is not a PE

`sample-not-pe.txt` contains the words `GetLastError` and `KERNEL32.dll`, but it is only a text file.

Content search:

```console
yara labs/09-pe-imports-and-sections/string_search.yar labs/09-pe-imports-and-sections/sample-not-pe.txt
```

Expected match:

```text
String_Search_GetLastError labs/09-pe-imports-and-sections/sample-not-pe.txt
```

PE import check:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar labs/09-pe-imports-and-sections/sample-not-pe.txt
```

No output is expected. The file starts with ordinary English, not a PE import table.

The Lab 07 `MZ` practice text is another useful negative sample:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar labs/07-file-size-and-headers/sample-match.txt
```

Lab 07 can match that file. Lab 09 should not, because a short `MZ` text file is not a PE with an import table.

### Mini exercise

Before changing a rule, predict the result.

1. In `pe_imports_sections.yar`, replace `"KERNEL32.dll"` with `"kernel32.dll"`. Does the compiled `hello.exe` still match?
2. Replace `"GetLastError"` with `"GetLastErrorA"`. What happens?
3. Remove `uint16(0) == 0x5A4D` from the condition. Why does the lab keep that check even when `pe.imports()` already implies a PE?
4. Scan `sample-not-pe.txt` with both `string_search.yar` and `pe_imports_sections.yar`. Why do the results differ?
5. Add this extra check to the lab rule, then scan your `hello.exe`:

```yara
for any section in pe.sections : (
    section.name == ".text"
)
```

If it does not match, inspect the actual section names. Compilers do not all use the same layout.

### Main takeaway

```text
raw bytes / strings -> content-based clues
pe.imports()        -> imported DLL/API information
pe.sections         -> section structure
condition           -> combine clues into one decision
```

A YARA match still means only that the rule condition was satisfied. It is not automatically proof that a file is malicious.

Later labs can add entry points, section characteristics, and false-positive reduction. Those topics are left out of this lab on purpose.

---

## Türkçe

### Amaç

YARA'nın `pe` modülüyle yalnızca ham string veya byte imzalarına bakmak yerine PE dosyasının import ve section bilgilerini incelemeyi öğrenmek.

Bu lab'den sonra şunları yapabilmelisin:

- `pe.imports("KERNEL32.dll", "GetLastError")` satırını kelime kelime açıklamak
- Bir API adını metin olarak aramakla PE import table'a sormak arasındaki farkı söylemek
- Section'ı tüm dosyada aranan sıradan bir string değil, parse edilmiş PE verisi olarak görmek
- Bu lab'i Lab 07 ve Lab 08'deki header / PE kontrolleriyle birleştirmek
- Yaygın bir Windows API'sinin tek başına malware göstergesi olmadığını hatırlamak

### Neden önemli?

Lab 01-06 dosya içeriğini arıyordu. Lab 07 bilinen bir offset'ten byte okuyordu. Lab 08, `pe` modülüne dosyanın Windows PE gibi görünüp görünmediğini soruyordu.

Lab 09 bir adım ileri gider: PE'nin hangi kütüphanelere bağlı olduğunu ve dosyanın section'lara nasıl ayrıldığını sorar.

Windows PE dosyalarında analiz sırasında işe yarayan yapısal bilgiler bulunur. Bunların önemli örnekleri:

- import edilen DLL ve API fonksiyonları
- `.text`, `.data`, `.rdata` gibi section'lar

YARA bu bilgileri `pe` modülü üzerinden okuyabilir.

Reverse engineering araçlarından gelen zihinsel model:

```text
PE dosyası
  -> section'lar
  -> import'lar
  -> string'ler
  -> fonksiyonlar
```

YARA da daha derin analize geçmeden önce bu yapısal ipuçlarının bir kısmını hızlı filtreleme için kullanabilir.

### String aramak, import kontrolü değildir

Bu lab'in ana fikri bu karşıtlıktır.

Lab 01-03'teki bir içerik kuralı, `GetLastError` metnini geçen her dosyayla eşleşebilir: kaynak kod, notlar ve bu lab'deki metin örneği dahil.

```yara
rule String_Search_GetLastError
{
    strings:
        $api = "GetLastError"

    condition:
        $api
}
```

`pe.imports()` başka bir soru sorar: parse edilmiş import table'da bu DLL'den bu API var mı?

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

| | String arama | `pe.imports()` |
| --- | --- | --- |
| Nereye bakar | Ham dosya içeriği | Parse edilmiş PE import table |
| `.txt` dosyasıyla eşleşir mi | Metin varsa evet | Hayır; dosya PE değildir |
| Ne kanıtlar | Metin/byte'ların geçtiğini | Programın o API'yi referansladığını |
| Malware hükmü | Hayır | Hayır |

Bir import, programın bir kütüphane fonksiyonunu **referansladığını** gösterir. Fonksiyonun çalışma anında çağrıldığını veya dosyanın zararlı olduğunu kanıtlamaz.

`pe.imports()`, sonradan isimle çözülen API'leri de görmez. Bu, import-table eşlemesinin bir sınırıdır; lab'in hatası değildir.

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

Condition'ı `and` ile bağlı üç kontrol olarak oku:

- `uint16(0) == 0x5A4D` — Lab 07 ham `MZ` header kontrolü
- `pe.number_of_sections > 0` — Lab 08 parse edilmiş PE özelliği
- `pe.imports("KERNEL32.dll", "GetLastError")` — bugünün yeni kontrolü

`meta` hâlâ rule'u açıklar ve eşleşmeye karar vermez. Bu alanları görmek için komut satırında `yara -m` kullanılabilir.

### `pe.imports()` ne yapıyor?

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

PE import table içinde belirtilen DLL ve API fonksiyonunun bulunup bulunmadığını kontrol eder.

Bu lab için üç biçim yeter. DLL adı büyük/küçük harfe duyarsızdır.

**1. İsimli fonksiyon, boolean sonuç** — lab kuralının kullandığı biçim:

```yara
pe.imports("KERNEL32.dll", "GetLastError")
```

`kernel32.dll` ve `KERNEL32.dll` aynı kabul edilir. Fonksiyon adı import table'da göründüğü gibi yazılmalıdır; `getlasterror` yapmayın.

**2. Bir DLL'den kaç fonksiyon import edilmiş** — yalnızca `kernel32.dll` var mı diye bakmak için:

```yara
pe.imports("kernel32.dll") >= 1
```

YARA 4.0'dan itibaren bu biçim sayı döner. `0`'dan büyük her değer aynı zamanda true sayılır.

**3. Regular expression** — Lab 06 köprüsü; yalnızca tahta örneği:

```yara
pe.imports(/kernel32\.dll/i, /^GetLastError$/) >= 1
```

Bu regex biçiminde adlar, `/i` eklenmedikçe büyük/küçük harfe duyarlıdır.

Bu lab **standart import'larda** kalır. Delayed import ve ordinal ile import sonraki alıştırmaya bırakılabilir.

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

Section isimleri ve düzeni compiler'a ve binary'ye göre değişebilir. Bu yüzden lab'in ana kuralı belirli bir isim zorlamak yerine en az bir section olup olmadığına bakar.

### Section isimlerine bakmak

Section, parse edilmiş PE metadata'sıdır. Tüm dosyada `.text` metnini aramakla aynı şey değildir.

Yanlış model, içerik aramasıdır:

```yara
$s = ".text"
```

YARA PE section'ları üzerinde dolaşabilir. Yapıya bakan kontrol şöyle görünür:

```yara
for any section in pe.sections : (
    section.name == ".text"
)
```

veya yalnızca ilk section'ı indekslemek:

```yara
pe.sections[0].name == ".text"
```

Birinci biçim **herhangi bir** section'ın adının `.text` olup olmadığını sorar. İkinci biçim **0. section**'ın o ada sahip olup olmadığını sorar. İlk section her zaman `.text` olmak zorunda değildir; öğretim örneği olarak `for any` daha güvenlidir.

Execute / write gibi section characteristics sonraki lab'e bırakılmıştır.

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

GetLastError, CloseHandle ve daha birçok KERNEL32 fonksiyonu olağan Windows programlarında da görünür. Bunları `and` ile birleştirmek, ipuçları spesifik olmadıkça detection rule üretmez.

Bu lab'ın amacı detection üretmek değil, PE modülü söz dizimini ve structure-aware matching mantığını öğrenmektir.

### Lab'i deneme

Kendi güvenli lab ortamında bilinen zararsız bir Windows PE dosyasıyla çalıştır. En küçük yol, bu klasördeki zararsız C örneğini derlemektir:

```c
#include <stdio.h>
#include <windows.h>

int main(void)
{
    DWORD err = GetLastError();
    printf("GetLastError=%lu\n", (unsigned long)err);
    return 0;
}
```

Yerelde derledikten sonra oluşan executable'ı repo kökünden tara:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar hello.exe
```

PE, `KERNEL32.dll` üzerinden `GetLastError` import ediyorsa beklenen eşleşme:

```text
PE_Imports_And_Sections_Demo hello.exe
```

Rastgele zararsız bir PE'nin eşleşmesi onun import table'ına bağlıdır. Bu lab malware örneği içermez.

### Karşıt test: metin PE değildir

`sample-not-pe.txt` içinde `GetLastError` ve `KERNEL32.dll` sözcükleri vardır, fakat dosya yalnızca bir metindir.

İçerik araması:

```console
yara labs/09-pe-imports-and-sections/string_search.yar labs/09-pe-imports-and-sections/sample-not-pe.txt
```

Beklenen eşleşme:

```text
String_Search_GetLastError labs/09-pe-imports-and-sections/sample-not-pe.txt
```

PE import kontrolü:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar labs/09-pe-imports-and-sections/sample-not-pe.txt
```

Çıktı beklenmez. Dosya PE import table ile değil, sıradan İngilizce metinle başlar.

Lab 07'deki `MZ` alıştırma metni de yararlı bir negatif örnektir:

```console
yara labs/09-pe-imports-and-sections/pe_imports_sections.yar labs/07-file-size-and-headers/sample-match.txt
```

Lab 07 bu dosyayla eşleşebilir. Lab 09 eşleşmemelidir; çünkü kısa bir `MZ` metin dosyası import table'ı olan bir PE değildir.

### Mini alıştırma

Rule'u değiştirmeden önce sonucu tahmin et.

1. `pe_imports_sections.yar` içinde `"KERNEL32.dll"` yerine `"kernel32.dll"` yaz. Derlenmiş `hello.exe` hâlâ eşleşir mi?
2. `"GetLastError"` yerine `"GetLastErrorA"` yaz. Ne olur?
3. Condition'dan `uint16(0) == 0x5A4D` satırını kaldır. `pe.imports()` zaten bir PE ima ederken lab bu kontrolü neden tutuyor?
4. `sample-not-pe.txt` dosyasını hem `string_search.yar` hem `pe_imports_sections.yar` ile tara. Sonuçlar neden farklı?
5. Lab kuralına şu ekstra kontrolü ekleyip `hello.exe` dosyanı tara:

```yara
for any section in pe.sections : (
    section.name == ".text"
)
```

Eşleşmezse gerçek section adlarına bak. Compiler'lar aynı düzeni kullanmak zorunda değildir.

### Ana çıkarım

```text
ham byte / string -> içerik tabanlı ipuçları
pe.imports()      -> DLL/API import bilgisi
pe.sections       -> section yapısı
condition         -> ipuçlarını tek kararda birleştirir
```

Bir YARA eşleşmesinin yalnızca rule koşulunun sağlandığını gösterdiğini unutmamak gerekir; tek başına malware kanıtı değildir.

Entry point, section characteristics ve false-positive azaltma sonraki lab'lere bırakılmıştır. Bu lab'e bilinçli olarak alınmamıştır.
