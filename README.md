# YARA-Learning-Labs

Learn YARA one small, safe lab at a time. / Küçük ve güvenli lab çalışmalarıyla adım adım YARA öğrenin.

[English](#english) · [Türkçe](#türkçe)

# English

## About this repository

YARA-Learning-Labs is a learning journal for studying YARA from the fundamentals onward. It is intended both as a personal refresher and as a beginner-friendly guide for anyone following the same path.

The first version is intentionally small. Each lab should introduce one idea, provide a harmless example, and record the main lessons without pretending to be a complete course.

## What is YARA?

YARA is a rule-based pattern-matching tool used to search files or memory for predefined indicators such as strings, byte patterns, and structural conditions. A rule describes what YARA should look for and the condition that must be true before YARA reports a match.

A YARA match is a signal that a rule's condition was satisfied. It is **not automatically proof that a file is malware**. A match must be interpreted together with the rule's quality, the file's context, and other analysis results.

## What will I learn?

The first lab covers the basic parts of a YARA rule and tests a harmless text marker. Later notes may explore string modifiers, hexadecimal byte patterns, Boolean conditions, metadata, rule testing, and false-positive reduction. Those topics will be added gradually as real labs rather than as empty folders.

## Repository structure

```text
YARA-Learning-Labs/
├── README.md
├── labs/
│   └── 01-what-is-yara/
│       ├── notes.md
│       ├── hello.yar
│       └── sample.txt
├── resources.md
└── LICENSE
```

Start with [Lab 01 notes](labs/01-what-is-yara/notes.md), then inspect the rule and its harmless sample side by side.

## Safety note

This first lab uses only plain text created for practice. It contains no malware sample, offensive payload, or rule for an active malicious campaign. Do not treat unknown files as safe merely because a YARA scan returns no match, and analyze suspicious material only in an appropriately isolated environment.

## References / Credits

- [Official YARA documentation](https://yara.readthedocs.io/en/latest/) is the primary reference for YARA concepts and syntax.
- [ZAYOTEM Malware Analysis Feed](https://github.com/ZAYOTEM/malware-analysis-feed) was consulted as one learning reference for seeing how YARA rules can be organized around analysis cases. That project is MIT-licensed: Copyright (c) 2022 ZAYOTEM.

The explanations, lab structure, practice rule, and sample in this initial version were written specifically for YARA-Learning-Labs. No ZAYOTEM malware samples, scripts, or rules are redistributed here. See [resources.md](resources.md) for more detail.

# Türkçe

## Bu repo hakkında

YARA-Learning-Labs, YARA'yı temelden başlayarak öğrenmek için tutulan bir öğrenme günlüğüdür. Hem kişisel olarak bilgileri tazelemek hem de aynı yolu izleyen yeni başlayanlara anlaşılır bir rehber sunmak amacıyla hazırlanmıştır.

İlk sürüm bilinçli olarak küçük tutulmuştur. Her lab tek bir fikri tanıtmalı, zararsız bir örnek sunmalı ve eksiksiz bir kurs olduğu iddiasına girmeden temel çıkarımları kaydetmelidir.

## YARA nedir?

YARA, dosya veya bellek içinde önceden tanımlanmış string, byte pattern ve yapısal koşullar gibi göstergeleri aramak için kullanılan kural tabanlı bir pattern-matching aracıdır. Bir rule, YARA'nın neyi arayacağını ve eşleşme bildirmesi için hangi koşulun doğru olması gerektiğini tanımlar.

Bir YARA eşleşmesi, rule içindeki koşulun sağlandığını gösteren bir sinyaldir. Bir dosyanın malware olduğunun **tek başına kanıtı değildir**. Eşleşme; rule'un kalitesi, dosyanın bağlamı ve diğer analiz sonuçlarıyla birlikte değerlendirilmelidir.

## Neler öğreneceğim?

İlk lab, bir YARA rule'unun temel bölümlerini ele alır ve zararsız bir metin işaretini test eder. İleride string modifier'ları, hexadecimal byte pattern'ları, Boolean koşullar, metadata, rule testleri ve false positive azaltma konuları incelenebilir. Bu konular, boş klasörler hâlinde değil, gerçek lab çalışmaları hazır oldukça aşamalı biçimde eklenecektir.

## Repo yapısı

```text
YARA-Learning-Labs/
├── README.md
├── labs/
│   └── 01-what-is-yara/
│       ├── notes.md
│       ├── hello.yar
│       └── sample.txt
├── resources.md
└── LICENSE
```

[Lab 01 notları](labs/01-what-is-yara/notes.md) ile başlayın; ardından rule ile zararsız örnek dosyayı yan yana inceleyin.

## Güvenlik notu

Bu ilk lab yalnızca alıştırma için oluşturulmuş düz metin kullanır. Malware örneği, saldırı amaçlı payload veya etkin bir zararlı kampanyaya yönelik rule içermez. Bir YARA taramasının eşleşme bulmaması, bilinmeyen bir dosyanın güvenli olduğu anlamına gelmez. Şüpheli materyalleri yalnızca uygun şekilde izole edilmiş bir ortamda inceleyin.

## Kaynaklar / Teşekkür

- YARA kavramları ve söz dizimi için birincil kaynak [resmî YARA dokümantasyonudur](https://yara.readthedocs.io/en/latest/).
- YARA rule'larının analiz vakaları etrafında nasıl düzenlenebildiğini görmek için öğrenme kaynaklarından biri olarak [ZAYOTEM Malware Analysis Feed](https://github.com/ZAYOTEM/malware-analysis-feed) incelenmiştir. Bu proje MIT lisanslıdır: Copyright (c) 2022 ZAYOTEM.

Bu ilk sürümdeki açıklamalar, lab yapısı, alıştırma rule'u ve örnek dosya YARA-Learning-Labs için özel olarak yazılmıştır. ZAYOTEM'e ait malware örnekleri, script'ler veya rule'lar burada yeniden dağıtılmamaktadır. Ayrıntılar için [resources.md](resources.md) dosyasına bakın.
