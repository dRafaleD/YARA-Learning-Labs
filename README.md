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

Future labs may cover PE-aware conditions, testing, regular expressions, and false-positive reduction. They will be added gradually as real exercises rather than empty folders.

## Repository structure

```text
YARA-Learning-Labs/
├── README.md
├── labs/
│   ├── 01-what-is-yara/
│   ├── 02-multiple-strings-and-conditions/
│   ├── 03-string-modifiers/
│   ├── 04-hexadecimal-strings/
│   └── 05-rule-metadata/
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

İleride PE tabanlı koşullar, rule testleri, regular expression'lar ve false-positive azaltma konuları incelenebilir. Bu konular boş klasörler olarak değil, gerçek lab çalışmaları hazır oldukça eklenecektir.

## Repo yapısı

```text
YARA-Learning-Labs/
├── README.md
├── labs/
│   ├── 01-what-is-yara/
│   ├── 02-multiple-strings-and-conditions/
│   ├── 03-string-modifiers/
│   ├── 04-hexadecimal-strings/
│   └── 05-rule-metadata/
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
