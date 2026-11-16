# Lab 52 — İçerik Hash'iyle Alarm Tekilleştirme

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## Lab 51'den devam
Önceki gün bir dosyanın birden çok YARA kuralıyla eşleşebileceğini öğrendik. Bu kez **aynı içeriğin birden fazla dosyada bulunması** durumunu inceliyoruz.

**Raw alerts:** tüm kural eşleşmelerinin sayısı. **Flagged files:** en az bir kuralla eşleşen dosyalar. **Distinct contents:** SHA-256 değerine göre farklı bayt içeriğine sahip örnekler.

Altı zararsız metin dosyası, iki YARA kuralıyla test ediliyor. İki dosya tamamen aynı. Sonuç:
- Toplam **7 kural eşleşmesi**.
- **5 işaretlenen dosya**.
- **4 farklı işaretlenen içerik**.
- Tüm veri kümesinde **5 farklı içerik**.

Dosya bazında TP=3, FP=2, TN=1, FN=0. Aynı içerikleri birleştirince TP=2, FP=2, TN=1, FN=0. **Saydığın birim değişince ölçüm de değişir.**

## Çalıştırma
YARA CLI kurulu olmalı:
~~~bash
python3 labs/52-content-hash-deduplication-and-alert-counts/evaluate.py
~~~

## Sorular
Aynı hash neden aynı saldırı olayı demek değil? Dosya, olay veya içerik bazında tekilleştirme ne zaman tercih edilir? TP ve FP sayılarını raporda neden açıkça tanımlamalıyız?

## Sınırlar
Yalnızca zararsız sentetik metinler ve eğitim kuralları kullanılır; gerçek malware tespit başarısı iddia edilmez.
