# Lab 58 — YARA Kural Sürümü ve Alarm Sayısı Karşılaştırması

[English](notes.md) · [Türkçe](notes.tr.md) · [V1 kuralları](rules_v1.yar) · [V2 kuralları](rules_v2.yar) · [Değerlendirme](evaluate.py)

## 57. lab'den devam
Önceki gün gecikmiş olaylar nedeniyle alarm özetinin sürümünü artırdık. Peki alarm sayısı **loglar değil de YARA kuralları değiştiği için** artarsa?

**Ruleset version:** kullanılan kural paketinin sürümü. **Pinned evaluation:** aynı veri kümesini belirlenmiş kural sürümüyle taramak. **Batch fingerprint:** taranan veri grubunun SHA-256 özeti.

Dört zararsız metni iki kuralla tarıyoruz. V1 yalnızca `BLUE-TOKEN`, V2 ise `BLUE-TOKEN` **veya** `GREEN-TOKEN` bulur. Aynı olaylar için V1'de **2**, V2'de **3** alarm oluşur; fark yalnızca `e2` olayıdır.

Bu artış **daha fazla zararlı yazılım bulunduğu** anlamına gelmez; kural tanımı değişmiştir.

## Çalıştır
YARA komut satırı aracı gereklidir:
```bash
python3 labs/58-rule-version-pinning-and-alert-comparison/evaluate.py
```

## Sorular
Kurallar değişirken veri neden aynı tutulmalı? Daha fazla alarm neden daha iyi doğruluk demek değildir? Bir SIEM raporunda kural sürümü niçin kaydedilmeli?

## Sınırlar
Gerçek malware örneği içermez; yalnızca sentetik metin ve örnek YARA kurallarıdır.
