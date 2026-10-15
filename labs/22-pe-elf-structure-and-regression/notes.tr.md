# Gün 22 — PE/ELF Yapısal Tespit ve Regression

[English](notes.md) · [Türkçe](notes.tr.md)

Bu gün tamamen izinli, zararsız ve yerel eğitim senaryolarına dayanır. Üretim sistemi veya gerçek delil yerine geçmez.

## Hedefler ve konular

### 1. Magic bytes versus valid formats

Bu kavramın güven sınırını, girdisini, beklenen çıktısını ve hangi yanlış çıkarımı önlediğini açıkla. Örnek üzerinde gözlem ile varsayımı ayır.

Çalışma sorusu: Kontrol kaldırılırsa hangi olumsuz test başarısız olur?

### 2. PE section conditions

Bu kavramın güven sınırını, girdisini, beklenen çıktısını ve hangi yanlış çıkarımı önlediğini açıkla. Örnek üzerinde gözlem ile varsayımı ayır.

Çalışma sorusu: Kontrol kaldırılırsa hangi olumsuz test başarısız olur?

### 3. ELF structure and module checks

Bu kavramın güven sınırını, girdisini, beklenen çıktısını ve hangi yanlış çıkarımı önlediğini açıkla. Örnek üzerinde gözlem ile varsayımı ayır.

Çalışma sorusu: Kontrol kaldırılırsa hangi olumsuz test başarısız olur?

### 4. String and structure composition

Bu kavramın güven sınırını, girdisini, beklenen çıktısını ve hangi yanlış çıkarımı önlediğini açıkla. Örnek üzerinde gözlem ile varsayımı ayır.

Çalışma sorusu: Kontrol kaldırılırsa hangi olumsuz test başarısız olur?

### 5. Negative samples and false positives

Bu kavramın güven sınırını, girdisini, beklenen çıktısını ve hangi yanlış çıkarımı önlediğini açıkla. Örnek üzerinde gözlem ile varsayımı ayır.

Çalışma sorusu: Kontrol kaldırılırsa hangi olumsuz test başarısız olur?

### 6. Rule regression and versioning

Bu kavramın güven sınırını, girdisini, beklenen çıktısını ve hangi yanlış çıkarımı önlediğini açıkla. Örnek üzerinde gözlem ile varsayımı ayır.

Çalışma sorusu: Kontrol kaldırılırsa hangi olumsuz test başarısız olur?

## Yerel uygulama

Dosya: `rules.yar`

```bash
yara rules.yar samples/control.txt
yara rules.yar samples/fake-header.txt
```

## Uygulama ve negatif test planı

1. Temel örneği çalıştır ve sonucu kaydet.
2. Doğru girdiyi tespit et.
3. Hatalı girdi senaryosu oluştur.
4. Sınır değeri dene.
5. Beklenen ve gerçek sonucu karşılaştır.
6. Sistem hangi bilgiyi kesin kanıtlamıyor, yaz.
7. İlgili kod satırını bul.
8. Tek bir kontrolü çalışma kopyasında değiştir.
9. Testleri yeniden çalıştır.
10. Araç sürümünü ve hash'leri kaydet.
11. False positive/negative olasılığını tartış.
12. Kısa analiz raporu hazırla.

## Mini görevler

1. Güvenlik kontrolüne yeni bir negatif test ekle.
2. Bir hata mesajının bilgi sızdırıp sızdırmadığını tartış.
3. Koddan bağımsız kısa tehdit modeli çiz.

## Tekrar soruları

1. Ana güven sınırı ne?
2. Hangi input güvenilmez?
3. Olumlu test neyi gösterir?
4. Negatif test neyi gösterir?
5. Bir sınır değeri ver.
6. Model veya araç çıktısına ne ölçüde güvenebiliriz?
7. Yanlış pozitif ne zaman oluşur?
8. Yanlış negatif ne zaman oluşur?
9. Gerçek üretim ortamında ne eksik?
10. Hash neden kaydedilir?
11. Kimlik doğrulama ve yetkilendirme farkı ne?
12. Sonuçta hangi belirsizlik kalır?
13. Logda ne tutulmalı?
14. Hangi hassas veri gereksiz?
15. Değişiklik sonrası ne tekrar test edilmeli?
16. Bu labın en önemli çıkarımı ne?

## Sınırlamalar

Sentetik örneklerin başarılı olması gerçek dünya saldırılarına karşı güvenliği kanıtlamaz. Varsayımlar, izinler ve çevre koşulları ayrıca değerlendirilmelidir.
