# Lab 12 — Match Counts, Offsets and Positions / Eşleşme Sayıları, Offset ve Konumlar

## English

### Goal
Move from asking only **whether** a string matched to asking **how many times** it matched and **where** it matched.

YARA provides useful operators for this:

```text
#identifier   -> number of matches
@identifier  -> offset of a match
@identifier[n] -> offset of the nth match
```

### Why position matters
Two files can contain the same text but place it in different locations. Position can therefore be useful when a file format or known structure gives the offset meaning.

Position alone is not proof of malicious behavior. It is another condition that can make a rule more precise.

### Rule 1
`test_rules.yar` contains:

```yara
rule Lab12_Offset_And_Occurrence
{
    strings:
        $marker = "YARA12"
        $tag = "training"

    condition:
        $marker at 0 and #tag >= 2
}
```

This requires:
1. `YARA12` to begin at offset 0.
2. `training` to appear at least twice.

The condition combines **position** and **occurrence count**.

### Rule 2
The second rule uses:

```yara
@word[1] < 64
```

This asks whether the first match of `$word` appears before offset 64.

### Test
Run:

```bash
yara -s test_rules.yar samples/match-count-and-offset.txt
yara -s test_rules.yar samples/no-match-position.txt
yara -s test_rules.yar samples/match-position.txt
```

Or scan all samples:

```bash
yara -r -s test_rules.yar samples/
```

The `-s` output is useful because it shows matching strings and their offsets.

### Things to observe
Compare the positive and negative samples.

Ask:
- Does `YARA12` start at offset 0?
- How many times does `training` occur?
- Where does the first `position` match occur?
- Which part of the condition caused the negative sample not to match?

### Security connection
Offsets and counts can reduce overly broad rules. For example, a structural marker at an expected location can be more meaningful than the same bytes appearing anywhere in a file.

However, overly strict offsets can also make rules fragile. Good detection logic balances precision with expected variation.

### Exercises
1. Change `#tag >= 2` to `#tag == 2` and retest.
2. Move `YARA12` away from offset 0 and observe the result.
3. Change the positional limit from 64 to 8.
4. Add another harmless `training` string and inspect `-s` output.
5. Explain when an exact `at` condition might be too restrictive.

### Questions
1. What does `#tag` represent?
2. What does `@word[1]` represent?
3. What does `$marker at 0` require?
4. Why can match count improve a rule?
5. Why can an exact offset make a rule brittle?

### Main takeaway
```text
string exists
     ↓
how many matches?
     ↓
where are the matches?
     ↓
combine evidence in condition
```

---

## Türkçe

### Amaç
Bir string'in sadece eşleşip eşleşmediğine değil, **kaç kere** ve **hangi konumda** eşleştiğine bakmayı öğrenmek.

YARA'da:

```text
#identifier     -> eşleşme sayısı
@identifier     -> eşleşme offset'i
@identifier[n]  -> n'inci eşleşmenin offset'i
```

### Konum neden önemli?
İki dosya aynı text'i içerebilir ama farklı konumlarda tutabilir. Dosya formatı veya bilinen yapı offset'e anlam kazandırıyorsa konum faydalı bir sinyal olabilir.

Konum tek başına malware kanıtı değildir; rule'u daha precise hale getirebilen ek bir koşuldur.

### Rule 1
```yara
$marker at 0 and #tag >= 2
```

şunları ister:
1. `YARA12` offset 0'da başlamalı.
2. `training` en az iki kez geçmeli.

Yani **position + occurrence count** birleştirilir.

### Rule 2
```yara
@word[1] < 64
```

`$word` için ilk eşleşmenin offset 64'ten önce olmasını ister.

### Test
```bash
yara -s test_rules.yar samples/match-count-and-offset.txt
yara -s test_rules.yar samples/no-match-position.txt
yara -s test_rules.yar samples/match-position.txt
```

Tüm klasör:
```bash
yara -r -s test_rules.yar samples/
```

`-s`, eşleşen string'leri ve offset'lerini görmeyi kolaylaştırır.

### Gözlem
Şunları kontrol et:
- `YARA12` gerçekten offset 0'da mı?
- `training` kaç kere geçiyor?
- İlk `position` hangi offset'te?
- Negative sample'da condition'ın hangi kısmı false oluyor?

### Güvenlik bağlantısı
Offset ve count kullanmak aşırı geniş rule'ları daraltabilir. Beklenen yapısal konumdaki marker, dosyanın herhangi bir yerindeki aynı byte'lardan daha anlamlı olabilir.

Ama aşırı katı offset koşulları rule'u kırılgan da yapabilir. İyi detection logic precision ile beklenen değişkenliği dengeler.

### Alıştırmalar
1. `#tag >= 2` yerine `#tag == 2` yazıp tekrar test et.
2. `YARA12` marker'ını offset 0'dan uzaklaştır.
3. 64 sınırını 8 yap.
4. Bir `training` daha ekleyip `-s` çıktısını incele.
5. Exact `at` koşulunun ne zaman fazla kısıtlayıcı olacağını açıkla.

### Sorular
1. `#tag` neyi temsil eder?
2. `@word[1]` neyi temsil eder?
3. `$marker at 0` ne ister?
4. Match count rule'u neden geliştirebilir?
5. Exact offset neden rule'u kırılgan hale getirebilir?

### Ana çıkarım
```text
string var mı?
     ↓
kaç eşleşme var?
     ↓
eşleşmeler nerede?
     ↓
condition içinde kanıtları birleştir
```
