# Lab 15 — ELF Module Basics / ELF Module Temelleri

## English

### Goal

Learn how YARA can use parsed ELF metadata instead of relying only on raw strings and byte patterns.

Earlier labs introduced the PE module for Windows executables. This lab adds the Linux side by using YARA's `elf` module with a harmless executable that you compile yourself.

Topics:

- `import "elf"`
- ELF type
- machine architecture
- entry point
- section count
- combining structure with a string indicator
- positive and negative testing
- understanding why structure-aware rules can reduce weak matches

A YARA match is still not proof that a file is malicious.

## 1. Why an ELF module?

Day 7 showed that raw bytes can identify simple file structure.

For example, an ELF file normally begins with the ELF magic:

```text
7F 45 4C 46
```

A raw rule could check those bytes.

But YARA can also parse the format for us:

```yara
import "elf"
```

This gives a rule access to ELF-aware information such as:

- file type,
- architecture,
- entry point,
- sections.

The mental shift is:

```text
raw bytes
   ↓
"does this look like ELF?"

versus

parsed ELF metadata
   ↓
"what kind of ELF is this?"
```

## 2. Connection to Reverse Engineering Day 20

The Reverse-Engineering-Labs repository recently introduced:

- ELF sections,
- symbols,
- stripped binaries,
- `.text`,
- `.rodata`,
- `.data`,
- `.bss`.

YARA Lab 15 looks at the same binary format from a detection-engineering perspective.

Reverse engineering asks:

> How is this binary organized and what does it do?

YARA asks:

> Which stable properties can a rule test?

These skills complement each other.

## 3. Build the harmless sample

The lab includes:

```text
source/elf_sample.c
```

Compile it on x86-64 Linux:

```bash
gcc -O0 -no-pie source/elf_sample.c -o samples/lab15_elf
```

If the `samples` directory does not exist locally:

```bash
mkdir -p samples
gcc -O0 -no-pie source/elf_sample.c -o samples/lab15_elf
```

Why `-no-pie`?

Modern Linux toolchains often build PIE executables by default. PIE binaries are commonly represented as `ET_DYN` in ELF metadata.

For this beginner lab, `-no-pie` makes the training target a traditional `ET_EXEC` executable so the rule and the concept line up clearly.

This is a lab choice—not a statement that PIE is suspicious.

## 4. Verify the file yourself

Before YARA, inspect it:

```bash
file samples/lab15_elf
readelf -h samples/lab15_elf
```

Look for:

- ELF
- 64-bit
- x86-64 / AMD64
- executable type
- entry point

You can also list sections:

```bash
readelf -S samples/lab15_elf
```

This is important: do not let YARA become a black box. Verify what the rule is testing with another tool.

## 5. Import the module

The rules begin with:

```yara
import "elf"
```

Without the import, ELF-specific fields are not available.

This is similar to the PE labs:

```text
import "pe"  -> parsed PE information
import "elf" -> parsed ELF information
```

## 6. ELF type

The first rule checks:

```yara
elf.type == elf.ET_EXEC
```

`ET_EXEC` represents an executable ELF object type.

Other ELF types exist. For example, shared objects and many PIE executables use different type metadata.

Do not create the false assumption:

```text
ELF + ET_EXEC = malware
```

It only describes file structure/type.

## 7. Machine architecture

The rule also checks:

```yara
elf.machine == elf.EM_X86_64
```

This asks whether the ELF metadata identifies the x86-64 architecture.

Why is this useful?

A rule may intentionally target only a particular platform.

But architecture is context, not maliciousness.

```text
x86-64 executable
      !=
malicious executable
```

## 8. Number of sections

The rule uses:

```yara
elf.number_of_sections > 0
```

This introduces a parsed structural property.

For the sample, inspect the actual count with:

```bash
readelf -h samples/lab15_elf
```

and compare it with the section table:

```bash
readelf -S samples/lab15_elf
```

The rule does not require an exact count because compiler/linker output can vary across systems.

## 9. Entry point

The second training rule checks:

```yara
elf.entry_point > 0
```

The entry point is the virtual address where execution begins according to the ELF header.

Important distinction:

```text
ELF entry point != C main()
```

Runtime startup code normally executes before `main()`.

This is an excellent connection between YARA, ELF knowledge and reverse engineering.

## 10. Combine structure and content

The first rule also contains:

```yara
$marker = "YARA_ELF_LAB_15" ascii
```

and requires:

```yara
$marker
```

The final logic is approximately:

```text
ET_EXEC
   +
x86-64
   +
has sections
   +
training marker
   ↓
match
```

This is stronger than matching the marker alone because the rule also requires the expected file structure.

It still does not make the rule a malware detector. It is a harmless training example.

## 11. Run the rules

After compiling:

```bash
yara test_rules.yar samples/lab15_elf
```

Expected matches:

```text
Lab15_ELF_Executable_With_Training_Marker
Lab15_ELF_Entry_Point_Present
```

Order may vary.

Show matching strings:

```bash
yara -s test_rules.yar samples/lab15_elf
```

The structural rule has no string to print; the marker-based rule does.

## 12. Negative test: source file

Run the same rules against the C source:

```bash
yara test_rules.yar source/elf_sample.c
```

The source contains the text:

```text
YARA_ELF_LAB_15
```

but it is not an ELF executable.

Therefore the first rule should not match.

This demonstrates an important detection-engineering idea:

```text
string present
      +
wrong file structure
      ↓
no match
```

Structure can provide useful context.

## 13. Negative test: PIE build

Compile a normal PIE build on a toolchain where PIE is the default:

```bash
gcc -O0 source/elf_sample.c -o samples/lab15_pie
readelf -h samples/lab15_pie
```

If the result is `ET_DYN`, the rules requiring `ET_EXEC` should not match.

This is not a failure.

It demonstrates that a rule can become too narrow if its structural assumptions do not match the files you want to detect.

## 14. Rule precision vs coverage

Imagine a rule requires:

```text
ET_EXEC + x86-64 + marker
```

It may avoid unrelated text files, but it will also miss a PIE version of the same training program.

This introduces a fundamental trade-off:

```text
more restrictive conditions
        ↓
potentially fewer false positives
        +
potentially more false negatives
```

Good rule design requires testing against the intended dataset.

## 15. Do not overfit build artifacts

Compiler, linker and platform choices can change:

- section count,
- ELF type,
- symbols,
- addresses,
- layout.

Therefore a rule based on one exact local build can become fragile.

Prefer properties that make sense for the detection goal rather than copying every observable field into the condition.

## 16. Structural checks are context

Useful structural properties may answer:

- Is this file actually ELF?
- Which architecture is it for?
- What object type is it?
- Does it have an entry point?
- How many sections are parsed?

These properties can strengthen other indicators.

But common structural properties are usually not unique enough to identify malicious behavior by themselves.

## 17. Detection-engineering workflow

A good workflow for this lab:

```text
understand file format
       ↓
inspect sample manually
       ↓
choose meaningful properties
       ↓
write rule
       ↓
positive test
       ↓
negative test
       ↓
change build conditions
       ↓
observe missed matches
       ↓
refine intentionally
```

## 18. Exercises

1. Compile the `-no-pie` sample.
2. Confirm `ET_EXEC` with `readelf -h`.
3. Run both YARA rules.
4. Use `yara -s` and find the training marker.
5. Scan `source/elf_sample.c` and explain why it does not match.
6. Build a PIE version and inspect its ELF type.
7. Explain why the `ET_EXEC` requirement may reduce coverage.
8. Remove the architecture condition temporarily and retest.
9. Change the marker in the source, rebuild and observe the result.
10. Compare YARA's structural checks with the information shown by `readelf`.

## 19. Questions

1. What does `import "elf"` provide?
2. What is `ET_EXEC`?
3. What does `EM_X86_64` describe?
4. Is the ELF entry point the same as C `main()`?
5. Why does the C source contain the marker but still fail the composed rule?
6. Why can PIE affect this lab's rule?
7. Why should section count usually not be hardcoded without a reason?
8. Can ELF structure alone prove maliciousness?
9. What is overfitting in a YARA-rule context?
10. Why are both positive and negative samples important?

## Main takeaway

```text
raw indicator
     +
parsed ELF structure
     ↓
more contextual rule
     ↓
test across variations
     ↓
understand precision / coverage trade-offs
```

---

## Türkçe

### Amaç

YARA'nın sadece raw string ve byte pattern aramak yerine parse edilmiş ELF metadata'sını nasıl kullanabildiğini öğrenmek.

Önceki lab'lerde Windows executable'ları için PE module gördük. Bu lab, kendi compile ettiğin zararsız bir executable üzerinden YARA'nın `elf` module'ünü kullanarak Linux tarafını ekliyor.

Konular:

- `import "elf"`
- ELF type
- machine architecture
- entry point
- section count
- structure + string indicator birleştirme
- positive/negative test
- structure-aware rule'un zayıf match'leri nasıl azaltabileceğini anlamak

YARA match yine tek başına malware kanıtı değildir.

## 1. Neden ELF module?

Day 7'de raw byte ile basit file structure kontrolü görmüştük.

ELF normalde şu magic ile başlar:

```text
7F 45 4C 46
```

Raw rule bunu kontrol edebilir.

Ama YARA formatı bizim için parse edebilir:

```yara
import "elf"
```

Böylece:

- file type,
- architecture,
- entry point,
- section

gibi ELF-aware bilgiye erişebiliriz.

Zihinsel fark:

```text
raw bytes
   ↓
"bu ELF'e benziyor mu?"

versus

parsed ELF metadata
   ↓
"bu nasıl bir ELF?"
```

## 2. Reverse Engineering Day 20 bağlantısı

Reverse-Engineering-Labs içinde yakın zamanda:

- ELF section,
- symbol,
- stripped binary,
- `.text`,
- `.rodata`,
- `.data`,
- `.bss`

işlendi.

YARA Lab 15 aynı binary formatına detection-engineering açısından bakıyor.

Reverse engineering:

> Binary nasıl organize edilmiş ve ne yapıyor?

YARA:

> Hangi stabil özellikleri rule ile test edebilirim?

İki beceri birbirini tamamlar.

## 3. Zararsız sample'ı build et

Lab:

```text
source/elf_sample.c
```

içeriyor.

x86-64 Linux'ta:

```bash
mkdir -p samples
gcc -O0 -no-pie source/elf_sample.c -o samples/lab15_elf
```

Neden `-no-pie`?

Modern Linux toolchain'leri default olarak PIE üretebilir. PIE binary'ler ELF metadata'da çoğunlukla `ET_DYN` olarak görünür.

Başlangıç labında training target'ın klasik `ET_EXEC` olması rule ile concept'in daha net uyuşmasını sağlıyor.

Bu, PIE'ın şüpheli olduğu anlamına gelmez.

## 4. Dosyayı kendin doğrula

YARA'dan önce:

```bash
file samples/lab15_elf
readelf -h samples/lab15_elf
readelf -S samples/lab15_elf
```

Şunları bul:

- ELF
- 64-bit
- x86-64 / AMD64
- executable type
- entry point
- section table

YARA'yı black box haline getirme. Rule'un test ettiği şeyi başka tool ile doğrula.

## 5. Module import

```yara
import "elf"
```

ELF-specific field'lara erişim sağlar.

```text
import "pe"  -> parsed PE information
import "elf" -> parsed ELF information
```

## 6. ELF type

```yara
elf.type == elf.ET_EXEC
```

`ET_EXEC`, executable ELF object type'ı temsil eder.

Başka ELF type'ları da vardır. Shared object ve birçok PIE executable farklı type metadata kullanabilir.

Şu çıkarımı yapma:

```text
ELF + ET_EXEC = malware
```

Bu yalnızca file structure/type bilgisidir.

## 7. Machine architecture

```yara
elf.machine == elf.EM_X86_64
```

ELF metadata'nın x86-64 architecture belirttiğini kontrol eder.

Belirli platformu hedefleyen rule için faydalı olabilir.

Ama:

```text
x86-64 executable != malicious executable
```

## 8. Section sayısı

```yara
elf.number_of_sections > 0
```

parse edilmiş structural property kullanır.

Gerçek değeri:

```bash
readelf -h samples/lab15_elf
readelf -S samples/lab15_elf
```

ile karşılaştır.

Exact count zorunlu tutmuyoruz çünkü compiler/linker output sistemler arasında değişebilir.

## 9. Entry point

İkinci training rule:

```yara
elf.entry_point > 0
```

kullanıyor.

Entry point, ELF header'a göre execution'ın başladığı virtual address'tir.

Önemli:

```text
ELF entry point != C main()
```

Runtime startup code normalde `main()`'den önce çalışır.

Bu YARA + ELF + reverse engineering arasında güzel bağlantıdır.

## 10. Structure ve content birleştirme

İlk rule:

```yara
$marker = "YARA_ELF_LAB_15" ascii
```

içeriyor.

Final logic:

```text
ET_EXEC
   +
x86-64
   +
section var
   +
training marker
   ↓
match
```

Marker'ı tek başına aramaktan daha context-aware'dır.

Yine de bu malware detector değildir; zararsız training example'dır.

## 11. Rule'ları çalıştır

```bash
yara test_rules.yar samples/lab15_elf
```

Beklenen:

```text
Lab15_ELF_Executable_With_Training_Marker
Lab15_ELF_Entry_Point_Present
```

Order değişebilir.

Matching string:

```bash
yara -s test_rules.yar samples/lab15_elf
```

Structural rule'da gösterilecek string yoktur; marker rule'unda vardır.

## 12. Negative test: source file

```bash
yara test_rules.yar source/elf_sample.c
```

Source file:

```text
YARA_ELF_LAB_15
```

text'ini içerir fakat ELF executable değildir.

Dolayısıyla composed rule match olmamalıdır.

```text
string var
   +
yanlış file structure
   ↓
no match
```

Structure context sağlar.

## 13. Negative test: PIE build

Toolchain default PIE üretiyorsa:

```bash
gcc -O0 source/elf_sample.c -o samples/lab15_pie
readelf -h samples/lab15_pie
```

Sonuç `ET_DYN` ise `ET_EXEC` isteyen rule match olmamalıdır.

Bu hata değildir. Structural assumption detection hedefinle uyuşmuyorsa rule'un fazla dar olabileceğini gösterir.

## 14. Precision ve coverage

Rule:

```text
ET_EXEC + x86-64 + marker
```

isterse unrelated text file'ları elemekte yardımcı olur fakat aynı training programın PIE build'ini de kaçırır.

```text
daha restrictive condition
        ↓
potansiyel daha az false positive
        +
potansiyel daha fazla false negative
```

Rule design intended dataset üzerinde test edilmelidir.

## 15. Build artifact'a overfit etme

Compiler, linker ve platform şunları değiştirebilir:

- section count
- ELF type
- symbol
- address
- layout

Tek local build'deki her özelliği condition'a koymak fragile rule oluşturabilir.

Detection goal için anlamlı property seç.

## 16. Structural check context sağlar

Structural property şu sorulara yardım eder:

- Gerçekten ELF mi?
- Hangi architecture?
- Hangi object type?
- Entry point var mı?
- Kaç section parse edildi?

Bunlar diğer indicator'ları güçlendirebilir.

Ama yaygın structural property tek başına malicious behavior için genellikle yeterince unique değildir.

## 17. Detection-engineering workflow

```text
file formatı anla
       ↓
sample'ı manual inspect et
       ↓
meaningful property seç
       ↓
rule yaz
       ↓
positive test
       ↓
negative test
       ↓
build condition değiştir
       ↓
missed match gözlemle
       ↓
bilinçli refine et
```

## 18. Alıştırmalar

1. `-no-pie` sample compile et.
2. `readelf -h` ile `ET_EXEC` doğrula.
3. İki YARA rule'unu çalıştır.
4. `yara -s` ile training marker'ı bul.
5. `source/elf_sample.c` scan et ve neden match olmadığını açıkla.
6. PIE version build edip ELF type'ı incele.
7. `ET_EXEC` şartının coverage'ı neden azaltabileceğini açıkla.
8. Architecture condition'ı geçici kaldırıp tekrar test et.
9. Source marker'ını değiştirip rebuild et ve sonucu gözlemle.
10. YARA structural check ile `readelf` output'unu karşılaştır.

## 19. Sorular

1. `import "elf"` ne sağlar?
2. `ET_EXEC` nedir?
3. `EM_X86_64` neyi açıklar?
4. ELF entry point ile C `main()` aynı mı?
5. C source marker içerdiği halde composed rule neden match olmaz?
6. PIE bu labdaki rule'u neden etkileyebilir?
7. Section count neden sebepsiz exact hardcode edilmemelidir?
8. ELF structure tek başına maliciousness kanıtlar mı?
9. YARA rule context'inde overfitting nedir?
10. Positive ve negative sample neden birlikte gerekir?

## Ana çıkarım

```text
raw indicator
     +
parsed ELF structure
     ↓
daha contextual rule
     ↓
variation'lar üzerinde test
     ↓
precision / coverage trade-off'unu anla
```
