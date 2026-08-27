# Lab 01 - What is YARA? / YARA Nedir?

## English

### Goal

Understand the smallest useful parts of a YARA rule and run a safe rule against a harmless text file.

### What is YARA?

YARA searches files or memory using rules. A rule can describe text strings, byte patterns, and logical or structural conditions. When its condition evaluates to true for a target, YARA reports the rule as a match.

The result says that the rule matched; it does not decide by itself whether the target is malware.

### How a rule works

A rule starts with the `rule` keyword and a rule name. The optional `strings` section assigns identifiers to patterns that YARA can search for. The required `condition` section is a Boolean expression that decides whether the rule matches.

In this lab, the rule defines one text string and uses that string directly as its condition.

### My first rule

```yara
rule Hello_YARA
{
    strings:
        $text = "HELLO_YARA"

    condition:
        $text
}
```

- `Hello_YARA` is the rule name shown when a match is reported.
- The `strings` section lists the patterns this rule can use.
- `$text` is a local string identifier; it refers to the text `HELLO_YARA`.
- The `condition` section controls the final result.
- Because the condition is `$text`, the rule matches when the target contains the exact, case-sensitive text `HELLO_YARA`.

### Test

Install YARA and, from the repository root, run:

```console
yara labs/01-what-is-yara/hello.yar labs/01-what-is-yara/sample.txt
```

The first path is the rule file. The second path is the harmless file being scanned.

### Expected result

The output should begin with the matching rule name and then show the target path:

```text
Hello_YARA labs/01-what-is-yara/sample.txt
```

Path separators may look different on Windows, but `Hello_YARA` should still appear.

### What I learned

I learned how a rule name, the `strings` section, a string identifier, and the `condition` section work together. I also confirmed a rule by testing it on a known, harmless file.

### What to remember

- A YARA match means the condition evaluated to true; it is not a malware verdict.
- Text strings are case-sensitive by default.
- A common string can match many benign files, so useful detection rules usually need stronger context and careful testing.
- Positive and negative test files both matter when checking a rule.

## Türkçe

### Amaç

Kullanışlı en küçük YARA rule'unun bölümlerini anlamak ve güvenli bir rule'u zararsız bir metin dosyası üzerinde çalıştırmak.

### YARA nedir?

YARA, rule'lar kullanarak dosya veya bellek içinde arama yapar. Bir rule; metin string'lerini, byte pattern'ları ve mantıksal ya da yapısal koşulları tanımlayabilir. Koşul hedef için doğru sonucunu verdiğinde YARA, rule'u eşleşme olarak bildirir.

Bu sonuç yalnızca rule'un eşleştiğini söyler; hedefin malware olup olmadığına tek başına karar vermez.

### Bir kural nasıl çalışır?

Bir rule, `rule` anahtar sözcüğü ve rule adıyla başlar. İsteğe bağlı `strings` bölümü, YARA'nın arayabileceği pattern'lara tanımlayıcı atar. Zorunlu `condition` bölümü ise rule'un eşleşip eşleşmeyeceğine karar veren bir Boolean ifadedir.

Bu lab'de rule tek bir metin string'i tanımlar ve doğrudan bu string'i koşul olarak kullanır.

### İlk kuralım

```yara
rule Hello_YARA
{
    strings:
        $text = "HELLO_YARA"

    condition:
        $text
}
```

- `Hello_YARA`, eşleşme bildirildiğinde gösterilen rule adıdır.
- `strings` bölümü, rule'un kullanabileceği pattern'ları listeler.
- `$text`, yerel bir string tanımlayıcısıdır ve `HELLO_YARA` metnini temsil eder.
- `condition` bölümü nihai sonucu belirler.
- Koşul `$text` olduğu için hedef, büyük-küçük harfe duyarlı olarak tam `HELLO_YARA` metnini içerdiğinde rule eşleşir.

### Test

YARA'yı kurduktan sonra repo kök dizininde şu komutu çalıştırın:

```console
yara labs/01-what-is-yara/hello.yar labs/01-what-is-yara/sample.txt
```

İlk yol rule dosyasını, ikinci yol ise taranan zararsız dosyayı gösterir.

### Beklenen sonuç

Çıktı, eşleşen rule adıyla başlamalı ve ardından hedef dosyanın yolunu göstermelidir:

```text
Hello_YARA labs/01-what-is-yara/sample.txt
```

Windows'ta yol ayraçları farklı görünebilir; ancak `Hello_YARA` yine görünmelidir.

### Ne öğrendim?

Rule adı, `strings` bölümü, string tanımlayıcısı ve `condition` bölümünün birlikte nasıl çalıştığını öğrendim. Ayrıca rule'u, içeriği bilinen zararsız bir dosya üzerinde test ederek doğruladım.

### Akılda tutulması gerekenler

- YARA eşleşmesi, koşulun doğru sonucunu verdiği anlamına gelir; bir malware hükmü değildir.
- Metin string'leri varsayılan olarak büyük-küçük harfe duyarlıdır.
- Yaygın bir string çok sayıda zararsız dosyayla eşleşebilir; bu nedenle kullanışlı detection rule'ları genellikle daha güçlü bağlam ve dikkatli test gerektirir.
- Bir rule'u kontrol ederken hem eşleşmesi gereken hem de eşleşmemesi gereken test dosyaları önemlidir.
