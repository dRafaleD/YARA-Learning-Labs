# Gün 21 — Byte Konumları, Dosya Yapısı ve Sınır Değeri Testleri

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

Bu gün önceki labların üzerine inşa edilen, yalnızca yerel ve zararsız eğitim verisi kullanan uygulamalı bir çalışmadır. Kodun her varsayımını incele; çıktıları otomatik güvenlik kanıtı sayma.

## Öğrenme hedefleri

- Offset-sensitive detection
- Bounded region
- Size gates
- Boolean composition
- Positive and negatives
- Matching evidence
- Regression automation
- Portability

## Veri akışı ve tehdit modeli

```text
controlled training input
        ↓
parser / evaluator / analyst
        ↓
security or evidence check
        ↓
observable result
        ↓
review assumptions and limits
```

## 1. Offset-sensitive detection

Her yerde aramak yerine header at 0 kullan, kaydırılmış header örneğiyle karşılaştır.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 2. Bounded region

Bölüm işareti keyfi uzaklıkta değil tanımlı offset aralığında olmalı.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 3. Size gates

Minimum ve maksimum boyut sınırını test et; filesize format kanıtı değildir.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 4. Boolean composition

Header, bölüm ve sürüm göstergelerini birleştirip rastgele eşleşmeleri azalt.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 5. Positive and negatives

Geçerli, kaydırılmış, kesilmiş ve eksik bölüm örneklerine beklenen sonucu yaz.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 6. Matching evidence

yara -s ile offsetleri incele, eşleşmeyi zararlılık kanıtıyla karıştırma.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 7. Regression automation

Koşul değişince tüm vakaları koş; gerçek sonuç beklenenden farklıysa test başarısız olsun.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 8. Portability

YARA sürümü ve komutu kaydet; sentetik signature sadece eğitim içindir.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## Uygulama

Yalnızca repo içindeki dosyaları kullan. Bu örnek üretim ortamına kurulacak güvenlik servisi değildir.

```bash
python3 create_samples.py
yara -s test_rules.yar samples/positive.txt
yara test_rules.yar samples/late-header.txt
python3 verify_samples.py
```

## Test matrisi

| Senaryo | Beklenen | Neden |
|---|---|---|
| Valid training input | Kabul / eşleşme | Baseline |
| Wrong owner or header | Ret / eşleşmeme | Scope / structure |
| Truncated or missing field | Kontrollü hata | Input validation |
| Unrelated benign sample | Yanlış alarm yok | False-positive awareness |

## Alıştırmalar

1. Örneği çalıştır ve çıktıyı kaydet.
2. İlk varsayımını not et.
3. Olumlu senaryoyu doğrula.
4. Bir negatif senaryo ekle.
5. İkinci negatif senaryo ekle.
6. Bir sınır değeri dene.
7. İlgili kontrolü kaynak kodunda bul.
8. Gözlem ve çıkarımı ayrı yaz.
9. Tek bir kontrolü çalışma kopyasında değiştir.
10. Bütün senaryoları tekrar test et.
11. Sonuçların sınırlamalarını yaz.
12. Bir sayfalık kısa analiz raporu hazırla.

## Tekrar soruları

1. Bu labda hangi güven sınırı var?
2. Hangi veri kullanıcı tarafından kontrol ediliyor?
3. Olumlu testin amacı ne?
4. Negatif testin amacı ne?
5. Çıktı neyi gerçekten kanıtlıyor?
6. Çıktı neyi kanıtlamıyor?
7. En kritik input hangisi?
8. Bir sınır değeri örneği ver.
9. Fail-closed davranış nedir?
10. Bu labı prod ortamına doğrudan almak neden riskli?
11. Bir false positive senaryosu düşün.
12. Bir false negative senaryosu düşün.
13. Log hangi alanları taşımalı?
14. Hangi kişisel veri gereksiz?
15. Sürüm bilgisi niçin kaydedilir?
16. Kontrol değişince hangi testler tekrar koşulmalı?

## Mini projeler

1. Bir yeni negatif test ve beklenen çıktı ekle; çalıştırıp belgele.
2. Bir güvenlik varsayımını çalışma kopyasında boz; hangi testin yakaladığını açıkla.
3. Kaynak, hash, araç sürümü, komut, gözlem ve sınırlamalardan oluşan kısa rapor yaz.

## Özet

Kendi aracının gerçek davranışını ölç; sentetik örneği aşırı genelleme. Güvenlik kararı, izin ve adli çıkarım bağımsız doğrulama gerektirir.
