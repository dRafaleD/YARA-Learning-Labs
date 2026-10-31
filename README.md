# YARA-Learning-Labs

Learn YARA one small, safe lab at a time. / Küçük ve güvenli lab çalışmalarıyla adım adım YARA öğrenin.

[English](#english) · [Türkçe](#türkçe)

# English

## About this repository

YARA-Learning-Labs is a learning journal for studying YARA from the fundamentals onward. It is intended both as a personal refresher and as a beginner-friendly guide for anyone following the same path.

Each lab introduces one concept, provides harmless examples, and records the main lessons without pretending to be a complete course.

## What is YARA?

YARA is a rule-based pattern-matching tool used to search files or memory for predefined indicators such as strings, byte patterns, and structural conditions. A rule describes what YARA should look for and the condition that must be true before YARA reports a match.

A YARA match means that a rule's condition was satisfied. It is **not automatically proof that a file is malware**. A match must be interpreted together with the rule's quality, the file's context, and other analysis results.

## Labs

| Lab | Topic | Main idea |
| --- | --- | --- |
| [01 - What is YARA?](labs/01-what-is-yara/notes.md) | Rule fundamentals | `rule`, `strings`, identifiers, and `condition` |
| [02 - Multiple Strings and Conditions](labs/02-multiple-strings-and-conditions/notes.md) | Combining indicators | `and`, `or`, `any of them`, `all of them`, and counted matches |
| [03 - String Modifiers](labs/03-string-modifiers/notes.md) | Matching text variations | `nocase`, `ascii`, and `wide` |
| [04 - Hexadecimal Strings](labs/04-hexadecimal-strings/notes.md) | Matching raw bytes | Exact byte sequences and `??` wildcards |
| [05 - Rule Metadata](labs/05-rule-metadata/notes.md) | Describing and organizing rules | `meta` fields and the difference between description and detection logic |
| [06 - Regular Expressions](labs/06-regular-expressions/notes.md) | Matching variable text patterns | Regex basics, repetition ranges, and combining regex with conditions |
| [07 - File Size and Header Checks](labs/07-file-size-and-headers/notes.md) | Structural conditions | `filesize`, `uint16(0)`, offsets, and simple header checks |
| [08 - PE Module Basics](labs/08-pe-module-basics/notes.md) | PE-aware conditions | `import "pe"`, section count, architecture, and combining parsed PE data with raw header checks |
| [09 - PE Imports and Sections](labs/09-pe-imports-and-sections/notes.md) | PE structure inspection | `pe.imports()`, section metadata, and structure-aware filtering |
| [10 - PE Entry Point and Section Flags](labs/10-pe-entry-point-and-section-flags/notes.md) | Entry point and permissions | `pe.entry_point`, `pe.section_index()`, and `SECTION_MEM_EXECUTE` |
| [11 - Rule Testing Workflow](labs/11-rule-testing-workflow/notes.md) | Testing and validation | Positive/negative samples, recursive scans, and inspecting matching strings |
| [12 - Match Counts and Offsets](labs/12-match-counts-and-offsets/notes.md) | Match position and frequency | `#identifier`, `@identifier[n]`, and positional conditions |
| [13 - String Sets and Threshold Conditions](labs/13-string-sets-and-thresholds/notes.md) | Grouping indicators | Prefix groups, `n of (...)`, and threshold-based conditions |
| [14 - Rule References and Private Helper Rules](labs/14-rule-references-and-private-helpers/notes.md) | Modular rule logic | Rule references, `private rule`, and reusable helper conditions |
| [15 - ELF Module Basics](labs/15-elf-module-basics/notes.md) | ELF-aware detection | `import "elf"`, ELF type, architecture, entry point, and structure-aware conditions |
| [16 - External Variables, Tags and Rule Organization](labs/16-external-variables-tags-and-organization/notes.md) | Rule-set organization | External variables, tags, scan configuration, and reproducible workflows |
| [17 - Include Files, Modular Rule Sets and Dependencies](labs/17-includes-modular-rules-and-dependencies/notes.md) | Multi-file rule organization | `include`, shared helpers, dependencies, runbooks, and packaging |
| [18 - Rule Quality, False Positives and Performance](labs/18-rule-quality-performance-and-test-corpus/notes.md) | Detection quality | False positives/negatives, selectivity, thresholds, benign corpora, regression tests, and local timing |
| [19 - Math Module: Entropy, Byte Windows and Detection Confidence](labs/19-math-entropy-and-windowed-analysis/notes.md) | Byte statistics and rule testing | `math.entropy`, bounded windows, synthetic samples, FP/FN analysis |
| [20 - Detection Metrics, Corpus Labels and Regression Testing](labs/20-detection-testing-metrics-and-regression/notes.md) | Testing and metrics | Confusion matrix, precision/recall, labeled corpus and automated YARA regression |
| [21 - Byte Positions, File Structure and Boundary-Case Testing](labs/21-byte-positions-file-structure-and-boundary-tests/notes.md) | Positional rules | `at`, `in`, size gates, negative samples and regression |
| [22 - PE/ELF Format Detection, Structural Indicators and Regression](labs/22-pe-elf-structure-and-regression/notes.md) | Multi-format training | PE/ELF parser modules, benign controls and regression |

| [23 - ASCII and Wide String Detection with Regression Fixtures](labs/23-23-ascii-wide-encoding-and-regression/notes.md) | Encoding and testing | ASCII, wide, corpus fixtures and negative testing |

| [24 - Rule Namespaces and Multi-Ruleset Regression Testing](labs/24-rule-namespaces-and-multi-ruleset-testing/notes.md) | Multi-rule testing | Rule organization and reproducible test fixtures |

| [25 - Corpus Quality, Near-Miss Rules and Regression Gates](labs/25-corpus-quality-and-regression/notes.md) | Rule validation | Near misses, quality and corpus regression |

| [26 - YARA Match Explanation, Metadata and Validation](labs/26-yara-metadata-and-explainable-matches/notes.md) | Rule validation | Metadata and matching evidence |

| [27 - Hex Patterns, Bounded Jumps and Negative Testing](labs/27-hex-jumps-and-bounded-patterns/notes.md) | Hex patterns | Bounded jumps and negative tests |

| [28 - File Signatures, Offset Constraints and False Positive Control](labs/28-file-signatures-offsets-and-false-positives/notes.md) | File signature checks | Offsets and contextual indicators |

Future labs will continue gradually with more advanced rule composition, modules, validation, and detection-engineering exercises.

## Repository structure

```text
YARA-Learning-Labs/
├── README.md
├── labs/
│   ├── 01-what-is-yara/
│   ├── 02-multiple-strings-and-conditions/
│   ├── 03-string-modifiers/
│   ├── 04-hexadecimal-strings/
│   ├── 05-rule-metadata/
│   ├── 06-regular-expressions/
│   ├── 07-file-size-and-headers/
│   ├── 08-pe-module-basics/
│   ├── 09-pe-imports-and-sections/
│   ├── 10-pe-entry-point-and-section-flags/
│   ├── 11-rule-testing-workflow/
│   ├── 12-match-counts-and-offsets/
│   ├── 13-string-sets-and-thresholds/
│   ├── 14-rule-references-and-private-helpers/
│   ├── 15-elf-module-basics/
│   ├── 16-external-variables-tags-and-organization/
│   ├── 17-includes-modular-rules-and-dependencies/
│   ├── 18-rule-quality-performance-and-test-corpus/
│   ├── 19-math-entropy-and-windowed-analysis/
│   ├── 20-detection-testing-metrics-and-regression/
│   └── 21-byte-positions-file-structure-and-boundary-tests/
├── resources.md
└── LICENSE
```

Start with Lab 01 and continue in order. Each lab adds one small concept and keeps the samples harmless and easy to inspect.

## Safety note

The current labs use only harmless practice text and locally generated test data. They contain no malware sample, offensive payload, or rule for an active malicious campaign. Do not treat unknown files as safe merely because a YARA scan returns no match, and analyze suspicious material only in an appropriately isolated environment.

## References / Credits

- [Official YARA documentation](https://yara.readthedocs.io/en/latest/) is the primary reference for YARA concepts and syntax.
- [ZAYOTEM Malware Analysis Feed](https://github.com/ZAYOTEM/malware-analysis-feed) was consulted as one learning reference for seeing how YARA rules can be organized around analysis cases. That project is MIT-licensed: Copyright (c) 2022 ZAYOTEM.

The explanations, lab structure, practice rules, and samples in this repository were written specifically for YARA-Learning-Labs. No ZAYOTEM malware samples, scripts, or rules are redistributed here. See [resources.md](resources.md) for more detail.

# Türkçe

## Bu repo hakkında

YARA-Learning-Labs, YARA'yı temelden başlayarak öğrenmek için tutulan bir öğrenme günlüğüdür. Hem kişisel olarak bilgileri tazelemek hem de aynı yolu izleyen yeni başlayanlara anlaşılır bir rehber sunmak amacıyla hazırlanmıştır.

Her lab tek bir kavramı tanıtır, zararsız örnekler sunar ve eksiksiz bir kurs olduğu iddiasına girmeden temel çıkarımları kaydeder.

## YARA nedir?

YARA, dosya veya bellek içinde önceden tanımlanmış string, byte pattern ve yapısal koşullar gibi göstergeleri aramak için kullanılan kural tabanlı bir pattern-matching aracıdır. Bir rule, YARA'nın neyi arayacağını ve eşleşme bildirmesi için hangi koşulun doğru olması gerektiğini tanımlar.

Bir YARA eşleşmesi, rule içindeki koşulun sağlandığını gösterir. Bir dosyanın malware olduğunun **tek başına kanıtı değildir**. Eşleşme; rule'un kalitesi, dosyanın bağlamı ve diğer analiz sonuçlarıyla birlikte değerlendirilmelidir.

## Lab'ler

| Lab | Konu | Ana fikir |
| --- | --- | --- |
| [01 - YARA Nedir?](labs/01-what-is-yara/notes.md) | Rule temelleri | `rule`, `strings`, tanımlayıcılar ve `condition` |
| [02 - Birden Fazla String ve Koşullar](labs/02-multiple-strings-and-conditions/notes.md) | Göstergeleri birleştirmek | `and`, `or`, `any of them`, `all of them` ve sayısal eşleşmeler |
| [03 - String Modifier'ları](labs/03-string-modifiers/notes.md) | Metin gösterimlerini eşleştirmek | `nocase`, `ascii` ve `wide` |
| [04 - Hexadecimal String'ler](labs/04-hexadecimal-strings/notes.md) | Ham byte eşleştirmek | Tam byte dizileri ve `??` wildcard'ları |
| [05 - Rule Metadata](labs/05-rule-metadata/notes.md) | Rule'ları açıklamak ve düzenlemek | `meta` alanları ile açıklama ve detection mantığı arasındaki fark |
| [06 - Regular Expression'lar](labs/06-regular-expressions/notes.md) | Değişken metin pattern'larını eşleştirmek | Regex temelleri, tekrar aralıkları ve regex'i condition ile birleştirmek |
| [07 - Dosya Boyutu ve Header Kontrolleri](labs/07-file-size-and-headers/notes.md) | Yapısal koşullar | `filesize`, `uint16(0)`, offset ve basit header kontrolleri |
| [08 - PE Module Temelleri](labs/08-pe-module-basics/notes.md) | PE-aware koşullar | `import "pe"`, section sayısı, mimari ve parse edilmiş PE verisini ham header kontrolleriyle birleştirmek |
| [09 - PE Import'ları ve Section'lar](labs/09-pe-imports-and-sections/notes.md) | PE yapısını incelemek | `pe.imports()`, section metadata'sı ve structure-aware filtreleme |
| [10 - PE Entry Point ve Section Bayrakları](labs/10-pe-entry-point-and-section-flags/notes.md) | Entry point ve izinler | `pe.entry_point`, `pe.section_index()` ve `SECTION_MEM_EXECUTE` |
| [11 - Rule Test İş Akışı](labs/11-rule-testing-workflow/notes.md) | Test ve doğrulama | Pozitif/negatif örnekler, recursive tarama ve eşleşen stringleri inceleme |
| [12 - Eşleşme Sayıları ve Offsetler](labs/12-match-counts-and-offsets/notes.md) | Eşleşme konumu ve sıklığı | `#identifier`, `@identifier[n]` ve positional condition'lar |
| [13 - String Grupları ve Threshold Koşulları](labs/13-string-sets-and-thresholds/notes.md) | Indicator gruplama | Prefix grupları, `n of (...)` ve threshold tabanlı condition'lar |
| [14 - Rule Referansları ve Private Helper Rule'lar](labs/14-rule-references-and-private-helpers/notes.md) | Modüler rule mantığı | Rule reference, `private rule` ve reusable helper condition'lar |
| [15 - ELF Module Temelleri](labs/15-elf-module-basics/notes.md) | ELF-aware detection | `import "elf"`, ELF type, architecture, entry point ve structure-aware condition'lar |
| [16 - External Variable, Tag ve Rule Organizasyonu](labs/16-external-variables-tags-and-organization/notes.md) | Rule-set organizasyonu | External variable, tag, scan configuration ve reproducible workflow |
| [17 - Include Dosyaları ve Modüler Rule Setleri](labs/17-includes-modular-rules-and-dependencies/notes.md) | Multi-file rule organizasyonu | `include`, shared helper, dependency, runbook ve packaging |
| [18 - Rule Kalitesi, False Positive ve Performance](labs/18-rule-quality-performance-and-test-corpus/notes.md) | Detection quality | False positive/negative, selectivity, threshold, benign corpus, regression ve local timing |
| [19 - Math Modülü: Entropy, Byte Window ve Tespit Güvenilirliği](labs/19-math-entropy-and-windowed-analysis/notes.tr.md) | Byte istatistiği ve rule testi | `math.entropy`, pencere ölçümü, sentetik test ve FP/FN yorumu |
| [20 - Tespit Metrikleri, Corpus Etiketleri ve Regression Test](labs/20-detection-testing-metrics-and-regression/notes.tr.md) | Test ve metrikler | Confusion matrix, precision/recall, etiketli corpus ve YARA regression otomasyonu |
| [21 - Byte Konumları, Dosya Yapısı ve Sınır Değeri Testleri](labs/21-byte-positions-file-structure-and-boundary-tests/notes.tr.md) | Konum tabanlı tespit | `at`, `in`, sınır kontrolleri ve regression |
| [22 - PE/ELF Yapısal Tespit ve Regression](labs/22-pe-elf-structure-and-regression/notes.tr.md) | Yapısal doğrulama | PE/ELF modülleri ve testler |

| [23 - ASCII ve Wide String Tespiti ve Regresyon Örnekleri](labs/23-23-ascii-wide-encoding-and-regression/notes.tr.md) | Kodlama ve test | ASCII, wide, corpus ve negatif test |

| [24 - Kural İsim Alanları ve Çoklu Kural Kümesi Regresyon Testleri](labs/24-rule-namespaces-and-multi-ruleset-testing/notes.tr.md) | Çoklu kural testi | Kural düzeni ve tekrar üretilebilir test örnekleri |

| [25 - Veri Kümesi Kalitesi, Yakın Eşleşmeler ve Regresyon Kontrolleri](labs/25-corpus-quality-and-regression/notes.tr.md) | Kural doğrulama | Yakın eşleşme, kalite ve regresyon |

| [26 - YARA Eşleşme Açıklamaları, Metadata ve Doğrulama](labs/26-yara-metadata-and-explainable-matches/notes.tr.md) | Kural doğrulama | Metadata ve eşleşme kanıtları |

| [27 - Hex Patternleri, Sınırlı Atlama ve Negatif Test](labs/27-hex-jumps-and-bounded-patterns/notes.tr.md) | Hex örüntüler | Sınırlı atlama ve negatif test |

| [28 - Dosya İmzaları, Offset Sınırları ve Yanlış Pozitif Kontrolü](labs/28-file-signatures-offsets-and-false-positives/notes.tr.md) | Dosya imzaları | Offset ve bağlamsal göstergeler |

İlerleyen lab'lerde daha gelişmiş rule composition, module kullanımı, validation ve detection-engineering çalışmaları adım adım eklenecektir.

## Repo yapısı

```text
YARA-Learning-Labs/
├── README.md
├── labs/
│   ├── 01-what-is-yara/
│   ├── 02-multiple-strings-and-conditions/
│   ├── 03-string-modifiers/
│   ├── 04-hexadecimal-strings/
│   ├── 05-rule-metadata/
│   ├── 06-regular-expressions/
│   ├── 07-file-size-and-headers/
│   ├── 08-pe-module-basics/
│   ├── 09-pe-imports-and-sections/
│   ├── 10-pe-entry-point-and-section-flags/
│   ├── 11-rule-testing-workflow/
│   ├── 12-match-counts-and-offsets/
│   ├── 13-string-sets-and-thresholds/
│   ├── 14-rule-references-and-private-helpers/
│   ├── 15-elf-module-basics/
│   ├── 16-external-variables-tags-and-organization/
│   ├── 17-includes-modular-rules-and-dependencies/
│   ├── 18-rule-quality-performance-and-test-corpus/
│   ├── 19-math-entropy-and-windowed-analysis/
│   ├── 20-detection-testing-metrics-and-regression/
│   └── 21-byte-positions-file-structure-and-boundary-tests/
├── resources.md
└── LICENSE
```

Lab 01'den başlayıp sırayla ilerleyin. Her lab tek bir yeni kavram ekler ve örnekleri zararsız, kolay incelenebilir halde tutar.

## Güvenlik notu

Mevcut lab'ler yalnızca zararsız alıştırma metinleri ve yerel olarak oluşturulan test verileri kullanır. Malware örneği, saldırı amaçlı payload veya etkin bir zararlı kampanyaya yönelik rule içermez. Bir YARA taramasının eşleşme bulmaması, bilinmeyen bir dosyanın güvenli olduğu anlamına gelmez. Şüpheli materyalleri yalnızca uygun şekilde izole edilmiş bir ortamda inceleyin.

## Kaynaklar / Teşekkür

- YARA kavramları ve söz dizimi için birincil kaynak [resmî YARA dokümantasyonudur](https://yara.readthedocs.io/en/latest/).
- YARA rule'larının analiz vakaları etrafında nasıl düzenlenebildiğini görmek için öğrenme kaynaklarından biri olarak [ZAYOTEM Malware Analysis Feed](https://github.com/ZAYOTEM/malware-analysis-feed) incelenmiştir. Bu proje MIT lisanslıdır: Copyright (c) 2022 ZAYOTEM.

Bu repodaki açıklamalar, lab yapısı, alıştırma rule'ları ve örnek dosyalar YARA-Learning-Labs için özel olarak yazılmıştır. ZAYOTEM'e ait malware örnekleri, script'ler veya rule'lar burada yeniden dağıtılmamaktadır. Ayrıntılar için [resources.md](resources.md) dosyasına bakın.


## Latest lab

- **Lab 40 — Global Rules for Scoped Scanning**
- [English notes](labs/40-global-rules-for-scoped-scanning/notes.md) · [Türkçe notlar](labs/40-global-rules-for-scoped-scanning/notes.tr.md) · [Practical exercise](labs/40-global-rules-for-scoped-scanning/rules.yar)
