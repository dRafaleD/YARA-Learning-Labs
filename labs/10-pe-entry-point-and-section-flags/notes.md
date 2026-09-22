# Lab 10 - PE Entry Point and Section Flags / PE Entry Point ve Section Bayrakları

## English

### Goal

Learn how YARA can locate a PE file's entry point and inspect the characteristics of the section that contains it.

After this lab you should be able to:

- explain `pe.entry_point` and why its meaning changes when YARA scans a file versus process memory
- use `pe.section_index(pe.entry_point)` instead of comparing the entry point to section virtual addresses by hand
- test one section flag with a bitwise AND, especially `pe.SECTION_MEM_EXECUTE`
- tell file-header `pe.characteristics` apart from `section.characteristics`
- treat an unusual section flag as a triage clue, not as a malware verdict

### Why this matters

Lab 08 asked whether a file looks like a PE. Lab 09 asked which libraries it imports and how it is split into sections.

Lab 10 asks a more specific structural question:

```text
Where does execution start, and what is that section allowed to do?
```

In reverse-engineering tools this is the same first glance: find the entry point, see which section owns it, then read that section's permissions.

YARA can ask those questions without opening Ghidra. The result is still only a match against a condition.

### Entry point

```yara
pe.entry_point
```

This value comes from the PE optional header, but YARA converts it for the current scan target:

- when scanning a **file**, `pe.entry_point` is a file offset
- when scanning **process memory**, it is a virtual address

That conversion is why this lab does not compare `pe.entry_point` with `section.virtual_address` by hand. Those two numbers are not the same kind of address during a file scan.

`pe.entry_point_raw` is the unconverted `AddressOfEntryPoint` value from the optional header. This lab uses the converted `pe.entry_point` together with `pe.section_index()`.

### Finding the section that owns the entry point

```yara
pe.section_index(pe.entry_point)
```

`pe.section_index()` returns the index of a section. It accepts either a section name or an address.

```yara
pe.section_index(".text")
pe.section_index(pe.entry_point)
```

The name form is case-sensitive. If no section matches, the function does not give a usable index, so the lab rules also require:

```yara
pe.section_index(pe.entry_point) >= 0
```

Once you have the index, the section object is:

```yara
pe.sections[pe.section_index(pe.entry_point)]
```

That object has the same fields introduced in Lab 09: `name`, `virtual_address`, `virtual_size`, `raw_data_size`, and `characteristics`.

### Section characteristics

Section flags are a bitmap. Test one flag with bitwise AND:

```yara
pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_EXECUTE
```

Useful constants for this lab:

```text
pe.SECTION_MEM_EXECUTE -> the section may contain code
pe.SECTION_MEM_READ    -> the section may be read
pe.SECTION_MEM_WRITE   -> the section may be written
```

A typical compiler-generated `.text` section is readable and executable. It is often **not** writable.

Do not confuse these flags with the PE **file** characteristics:

```yara
pe.characteristics & pe.DLL
```

`pe.characteristics` describes the image as a whole, for example whether it is a DLL. `section.characteristics` describes one section.

### Rules used in this lab

```yara
import "pe"

rule PE_Entry_Point_Executable_Section
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning PE entry points and executable section flags"
        lab = "10"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        pe.section_index(pe.entry_point) >= 0 and
        pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_EXECUTE
}

rule PE_Entry_Point_In_Text_Section
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning pe.section_index with a section name"
        lab = "10"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.section_index(pe.entry_point) >= 0 and
        pe.section_index(".text") >= 0 and
        pe.section_index(pe.entry_point) == pe.section_index(".text")
}
```

The first rule is the main lesson: the entry point sits in a section that has the execute flag.

The second rule is stricter and name-based. Many MSVC and MinGW programs use `.text`, but compilers are allowed to choose other names. If the second rule misses a self-compiled `hello.exe`, inspect the real section names before changing the condition.

### Why this is more specific than a string search

A Lab 01-style rule can match any file that contains the text `.text` or `entry point`.

```yara
$s = ".text"
```

The Lab 10 rules do not search for those words. They ask the PE parser:

```text
Does this file have an MZ header?
Does it have at least one section?
Can YARA map the entry point to a section?
Does that section have the execute flag?
```

That is the same false-positive idea as Labs 02, 07, and 09: combine independent structural checks instead of relying on one common string.

An execute flag on the entry-point section is still **not** a malware indicator. Ordinary programs start in a code section.

### A writable entry-point section is only a clue

This board example is intentionally **not** the lab's main rule:

```yara
pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_EXECUTE and
pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_WRITE
```

A section that is both executable and writable can be interesting during triage. Packers, some loaders, and a few legitimate programs can look that way. A simple `hello.c` compiled with a common toolchain usually will **not**.

Do not turn that observation into:

```text
writable entry-point section -> malware
```

The lab's job is to read the flags correctly and keep the claim as small as the evidence.

### Try the lab

Compile the harmless C sample in this folder with a Windows PE toolchain such as MSVC or MinGW:

```c
#include <stdio.h>

int main(void)
{
    puts("YARA_LAB_10");
    return 0;
}
```

Scan the resulting executable from the repository root:

```console
yara labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar hello.exe
```

A typical self-compiled console program should match `PE_Entry_Point_Executable_Section`. `PE_Entry_Point_In_Text_Section` matches only when the entry point section is actually named `.text`.

This lab does not include malware samples.

### Negative test

`sample-not-pe.txt` mentions entry points and section flags as ordinary English.

```console
yara labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar labs/10-pe-entry-point-and-section-flags/sample-not-pe.txt
```

No output is expected.

The Lab 07 `MZ` practice text is another useful negative sample:

```console
yara labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar labs/07-file-size-and-headers/sample-match.txt
```

Lab 07 can match that file. Lab 10 should not.

If you still have the Lab 09 `hello.exe`, you can scan it with this lab's rules as well. A PE that imports `GetLastError` will often also have an executable entry-point section.

### Mini exercise

Before changing a rule, predict the result.

1. Scan `sample-not-pe.txt` with the lab rules. Why is there no match even though the file contains the words `.text` and `entry point`?
2. On your `hello.exe`, keep `PE_Entry_Point_Executable_Section` and drop `PE_Entry_Point_In_Text_Section` if the names differ. Which check is more portable across compilers?
3. Add `pe.SECTION_MEM_WRITE` to the first rule with `and`. Does a normal `hello.exe` still match?
4. Replace `pe.section_index(pe.entry_point)` with a hand-written comparison against `section.virtual_address`. Why is that unsafe during a file scan?
5. Print metadata while scanning:

```console
yara -m labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar hello.exe
```

Confirm that `meta` still does not decide the match.

### Main takeaway

```text
pe.entry_point     -> where execution is recorded to start
pe.section_index() -> map that address or a name to a section
section flags      -> what that section is allowed to do
condition          -> combine those facts; do not turn one flag into a verdict
```

A YARA match still means only that the rule condition was satisfied. It is not automatically proof that a file is malicious.

Later labs can add dedicated rule-testing workflow. This lab already uses that habit: one positive PE you compiled, plus text files that must not match.

---

## Türkçe

### Amaç

YARA'nın bir PE dosyasının entry point'ini nasıl bulduğunu ve bu adresi barındıran section'ın characteristics bayraklarını nasıl okuduğunu öğrenmek.

Bu lab'den sonra şunları yapabilmelisin:

- `pe.entry_point` değerini açıklamak ve dosya taraması ile process memory taramasında neden farklı anlama geldiğini söylemek
- Entry point'i section sanal adresleriyle elle karşılaştırmak yerine `pe.section_index(pe.entry_point)` kullanmak
- Özellikle `pe.SECTION_MEM_EXECUTE` olmak üzere bir section bayrağını bitwise AND ile test etmek
- Dosya başlığındaki `pe.characteristics` ile `section.characteristics` farkını ayırmak
- Sıradışı bir section bayrağını triage ipucu olarak görmek, malware hükmü olarak görmemek

### Neden önemli?

Lab 08 dosyanın PE gibi görünüp görünmediğini sordu. Lab 09 hangi kütüphaneleri import ettiğini ve section'lara nasıl ayrıldığını sordu.

Lab 10 daha spesifik bir yapısal soru sorar:

```text
Çalışma nereden başlıyor ve o section'ın ne yapmasına izin var?
```

Reverse engineering araçlarında da ilk bakış budur: entry point'i bul, hangi section'a ait olduğunu gör, izinlerini oku.

YARA bu soruları Ghidra açmadan sorabilir. Sonuç yine yalnızca bir condition eşleşmesidir.

### Entry point

```yara
pe.entry_point
```

Bu değer PE optional header'dan gelir, fakat YARA onu taradığı hedefe göre dönüştürür:

- **dosya** taranırken `pe.entry_point` bir dosya offset'idir
- **process memory** taranırken bir sanal adrestir

Bu yüzden lab, `pe.entry_point` değerini `section.virtual_address` ile elle karşılaştırmez. Dosya taramasında bu iki sayı aynı tür adres değildir.

`pe.entry_point_raw`, optional header'daki dönüştürülmemiş `AddressOfEntryPoint` değeridir. Bu lab, dönüştürülmüş `pe.entry_point` ile `pe.section_index()` kombinasyonunu kullanır.

### Entry point'i barındıran section'ı bulmak

```yara
pe.section_index(pe.entry_point)
```

`pe.section_index()` bir section'ın indeksini döndürür. Section adı veya adres kabul eder.

```yara
pe.section_index(".text")
pe.section_index(pe.entry_point)
```

İsim biçimi büyük/küçük harfe duyarlıdır. Eşleşen section yoksa kullanılabilir bir indeks gelmez; bu yüzden lab kuralları şunu da ister:

```yara
pe.section_index(pe.entry_point) >= 0
```

İndeks elindeyken section nesnesi:

```yara
pe.sections[pe.section_index(pe.entry_point)]
```

Bu nesne Lab 09'daki alanlara sahiptir: `name`, `virtual_address`, `virtual_size`, `raw_data_size` ve `characteristics`.

### Section characteristics

Section bayrakları bir bitmap'tir. Tek bir bayrak bitwise AND ile test edilir:

```yara
pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_EXECUTE
```

Bu lab için yararlı sabitler:

```text
pe.SECTION_MEM_EXECUTE -> section kod içerebilir
pe.SECTION_MEM_READ    -> section okunabilir
pe.SECTION_MEM_WRITE   -> section yazılabilir
```

Compiler'ın ürettiği tipik bir `.text` section'ı okunur ve çalıştırılabilir. Çoğu zaman **yazılabilir değildir**.

Bu bayrakları PE **dosya** characteristics'i ile karıştırma:

```yara
pe.characteristics & pe.DLL
```

`pe.characteristics` görüntünün tamamını anlatır; örneğin dosyanın DLL olup olmadığı. `section.characteristics` tek bir section'ı anlatır.

### Bu lab'de kullanılan rule'lar

```yara
import "pe"

rule PE_Entry_Point_Executable_Section
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning PE entry points and executable section flags"
        lab = "10"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.number_of_sections > 0 and
        pe.section_index(pe.entry_point) >= 0 and
        pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_EXECUTE
}

rule PE_Entry_Point_In_Text_Section
{
    meta:
        author = "dRafaleD"
        description = "Harmless training rule for learning pe.section_index with a section name"
        lab = "10"
        purpose = "education"

    condition:
        uint16(0) == 0x5A4D and
        pe.section_index(pe.entry_point) >= 0 and
        pe.section_index(".text") >= 0 and
        pe.section_index(pe.entry_point) == pe.section_index(".text")
}
```

Birinci kural ana derstir: entry point, execute bayrağı olan bir section'dadır.

İkinci kural daha katı ve isme bağlıdır. Birçok MSVC ve MinGW programı `.text` kullanır, fakat compiler başka ad da seçebilir. İkinci kural kendi derlediğin `hello.exe` ile kaçırırsa condition'ı değiştirmeden önce gerçek section adlarına bak.

### Neden string aramaktan daha spesifik?

Lab 01 tarzı bir kural, içinde `.text` veya `entry point` yazan her dosyayla eşleşebilir.

```yara
$s = ".text"
```

Lab 10 kuralları bu sözcükleri aramaz. PE parser'a şunu sorar:

```text
Dosyanın MZ header'ı var mı?
En az bir section var mı?
YARA entry point'i bir section'a eşleyebiliyor mu?
O section'da execute bayrağı var mı?
```

Bu, Lab 02, 07 ve 09'daki false-positive fikrinin devamıdır: tek yaygın string yerine birbirinden bağımsız yapısal kontrolleri birleştir.

Entry point section'ındaki execute bayrağı hâlâ **malware göstergesi değildir**. Sıradan programlar da kod section'ından başlar.

### Yazılabilir entry-point section yalnızca bir ipucudur

Şu tahta örneği bilinçli olarak lab'in ana kuralı değildir:

```yara
pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_EXECUTE and
pe.sections[pe.section_index(pe.entry_point)].characteristics & pe.SECTION_MEM_WRITE
```

Hem çalıştırılabilir hem yazılabilir bir section triage sırasında ilginç olabilir. Packer'lar, bazı loader'lar ve az sayıda meşru program böyle görünebilir. Yaygın bir araç zinciriyle derlenen basit `hello.c` genellikle **böyle olmaz**.

Bu gözlemi şu cümleye çevirme:

```text
yazılabilir entry-point section -> malware
```

Lab'in işi bayrakları doğru okumak ve iddiayı kanıt kadar küçük tutmaktır.

### Lab'i deneme

Bu klasördeki zararsız C örneğini MSVC veya MinGW gibi bir Windows PE araç zinciriyle derle:

```c
#include <stdio.h>

int main(void)
{
    puts("YARA_LAB_10");
    return 0;
}
```

Oluşan executable'ı repo kökünden tara:

```console
yara labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar hello.exe
```

Tipik bir kendin derlediğin konsol programı `PE_Entry_Point_Executable_Section` ile eşleşmelidir. `PE_Entry_Point_In_Text_Section` yalnızca entry point section'ının adı gerçekten `.text` ise eşleşir.

Bu lab malware örneği içermez.

### Negatif test

`sample-not-pe.txt` entry point ve section bayraklarından sıradan İngilizce olarak söz eder.

```console
yara labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar labs/10-pe-entry-point-and-section-flags/sample-not-pe.txt
```

Çıktı beklenmez.

Lab 07'deki `MZ` alıştırma metni de yararlı bir negatif örnektir:

```console
yara labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar labs/07-file-size-and-headers/sample-match.txt
```

Lab 07 bu dosyayla eşleşebilir. Lab 10 eşleşmemelidir.

Lab 09'daki `hello.exe` hâlâ elindeyse bu lab'in kurallarıyla da tarayabilirsin. `GetLastError` import eden bir PE'nin çoğu zaman çalıştırılabilir bir entry-point section'ı da vardır.

### Mini alıştırma

Rule'u değiştirmeden önce sonucu tahmin et.

1. `sample-not-pe.txt` dosyasını lab kurallarıyla tara. Dosyada `.text` ve `entry point` sözcükleri varken neden eşleşme olmaz?
2. `hello.exe` üzerinde `PE_Entry_Point_Executable_Section` kalsın, isimler farklıysa `PE_Entry_Point_In_Text_Section` düşsün. Compiler'lar arasında hangisi daha taşınabilir?
3. İlk kurala `and` ile `pe.SECTION_MEM_WRITE` ekle. Normal bir `hello.exe` hâlâ eşleşir mi?
4. `pe.section_index(pe.entry_point)` yerine `section.virtual_address` ile elle karşılaştırma yaz. Dosya taramasında bu neden güvensiz?
5. Tararken metadata'yı da yazdır:

```console
yara -m labs/10-pe-entry-point-and-section-flags/entry_point_sections.yar hello.exe
```

`meta` bölümünün hâlâ eşleşmeye karar vermediğini doğrula.

### Ana çıkarım

```text
pe.entry_point     -> çalışmanın nereden başladığı kaydı
pe.section_index() -> bu adresi veya bir adı section'a eşler
section bayrakları -> o section'ın ne yapmasına izin var
condition          -> bu gerçekleri birleştir; tek bayrağı hükme çevirme
```

Bir YARA eşleşmesinin yalnızca rule koşulunun sağlandığını gösterdiğini unutmamak gerekir; tek başına malware kanıtı değildir.

İleride ayrı bir rule-test iş akışı lab'i eklenebilir. Bu lab o alışkanlığı şimdiden kullanır: kendi derlediğin bir pozitif PE ve eşleşmemesi gereken metin dosyaları.
