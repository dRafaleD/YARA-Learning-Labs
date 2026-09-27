# Lab 13 — String Sets, Prefixes and Threshold Conditions / String Grupları, Prefix ve Threshold Koşulları

## English

### Goal
Learn how to organize related indicators into string sets and require a threshold instead of writing long chains of `and` and `or`.

### 1. Prefix-based groups
YARA identifiers can share a prefix:

```yara
$net_1 = "network-alpha"
$net_2 = "network-beta"
$net_3 = "network-gamma"
```

Then a condition can refer to the group:

```yara
2 of ($net_*)
```

This means at least two strings whose identifiers begin with `$net_` must match.

### 2. Combining groups
Lab 13 combines two families:

```yara
2 of ($net_*) and any of ($file_*)
```

The file needs evidence from both categories:
- at least two network markers,
- at least one file marker.

This is easier to maintain than repeating every possible combination manually.

### 3. Threshold conditions
A second rule uses:

```yara
3 of ($indicator_*)
```

This is useful when several weak indicators become more meaningful when enough of them appear together.

### 4. Why grouping helps
A rule such as:

```text
one weak string -> broad/noisy
multiple related indicators -> stronger context
```

Thresholds can improve precision, but choosing a threshold without testing can also create false negatives.

### 5. Test
Run:

```bash
yara -s test_rules.yar samples/match-groups.txt
yara -s test_rules.yar samples/no-match-groups.txt
yara -s test_rules.yar samples/match-threshold.txt
```

Or:

```bash
yara -r -s test_rules.yar samples/
```

### 6. Compare the samples
`match-groups.txt` contains two `$net_*` indicators and one `$file_*` indicator.

`no-match-groups.txt` contains only one network indicator, so the first rule should not satisfy its threshold.

`match-threshold.txt` contains three of the four `$indicator_*` strings.

### 7. Detection-engineering connection
Grouping indicators by meaning can make a rule easier to understand:

```text
network-related evidence
        +
file-related evidence
        +
threshold
        ↓
more contextual condition
```

A YARA match is still not proof that a file is malicious. The quality of the indicators and validation dataset matters.

### Exercises
1. Change `2 of ($net_*)` to `all of ($net_*)`.
2. Change the threshold rule from 3 to 2 and compare matches.
3. Add `$file_3` and verify that the prefix group includes it automatically.
4. Remove one indicator from the positive sample and predict the result before scanning.
5. Rewrite the first condition manually using `and`/`or`, then compare readability.

### Questions
1. What does `2 of ($net_*)` mean?
2. Why are identifier prefixes useful?
3. What is the advantage of a threshold over one weak indicator?
4. What risk appears if the threshold is too high?
5. Why should positive and negative samples both be tested?

### Main takeaway
```text
organize indicators
       ↓
group by prefix
       ↓
choose threshold
       ↓
combine evidence
       ↓
test positive + negative samples
```

---

## Türkçe

### Amaç
İlişkili indicator'ları string gruplarında düzenlemeyi ve uzun `and`/`or` zincirleri yerine threshold kullanmayı öğrenmek.

### 1. Prefix ile gruplama
Identifier'lar ortak prefix kullanabilir:

```yara
$net_1 = "network-alpha"
$net_2 = "network-beta"
$net_3 = "network-gamma"
```

Condition:

```yara
2 of ($net_*)
```

Bu, identifier'ı `$net_` ile başlayan string'lerden en az ikisinin eşleşmesi gerektiği anlamına gelir.

### 2. Grupları birleştirme
```yara
2 of ($net_*) and any of ($file_*)
```

Dosyada iki kategoriden de evidence ister:
- en az iki network marker,
- en az bir file marker.

Her kombinasyonu tek tek yazmaktan daha okunabilir ve maintainable'dır.

### 3. Threshold koşulları
İkinci rule:

```yara
3 of ($indicator_*)
```

Birden fazla zayıf indicator yeterli sayıda birlikte bulunduğunda daha anlamlı hale gelebilir.

### 4. Gruplama neden faydalı?
```text
tek zayıf string -> broad/noisy
birden fazla ilişkili indicator -> daha güçlü context
```

Threshold precision'ı artırabilir fakat test edilmeden fazla yüksek seçilirse false negative üretebilir.

### 5. Test
```bash
yara -s test_rules.yar samples/match-groups.txt
yara -s test_rules.yar samples/no-match-groups.txt
yara -s test_rules.yar samples/match-threshold.txt
```

veya:

```bash
yara -r -s test_rules.yar samples/
```

### 6. Sample'ları karşılaştır
`match-groups.txt`: iki `$net_*` ve bir `$file_*` indicator içerir.

`no-match-groups.txt`: yalnızca bir network indicator içerdiği için threshold'u geçemez.

`match-threshold.txt`: dört `$indicator_*` string'inden üçünü içerir.

### 7. Detection engineering bağlantısı
```text
network evidence
       +
file evidence
       +
threshold
       ↓
daha contextual condition
```

YARA match yine tek başına malware kanıtı değildir. Indicator kalitesi ve validation dataset önemlidir.

### Alıştırmalar
1. `2 of ($net_*)` yerine `all of ($net_*)` kullan.
2. Threshold'u 3'ten 2'ye indir ve sonuçları karşılaştır.
3. `$file_3` ekle; prefix grubuna otomatik dahil olduğunu doğrula.
4. Positive sample'dan bir indicator sil ve taramadan önce sonucu tahmin et.
5. İlk condition'ı manuel `and`/`or` ile yazıp okunabilirliği karşılaştır.

### Sorular
1. `2 of ($net_*)` ne anlama gelir?
2. Identifier prefix'leri neden faydalıdır?
3. Threshold'un tek zayıf indicator'a göre avantajı nedir?
4. Threshold fazla yüksek olursa hangi risk oluşur?
5. Neden hem positive hem negative sample test edilmelidir?

### Ana çıkarım
```text
indicator'ları düzenle
       ↓
prefix ile grupla
       ↓
threshold seç
       ↓
evidence birleştir
       ↓
positive + negative test et
```
