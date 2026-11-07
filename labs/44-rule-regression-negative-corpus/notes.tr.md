# Gün 44 — Negatif Veri Kümesi ve Yakın Eşleşmelerle YARA Regresyonu

[English](notes.md) · [Türkçe](notes.tr.md) · [Pratik](rules.yar)

## Hedef

Bu çalışma yalnızca izinli ve zararsız yerel örnekler üzerinden **Negatif Veri Kümesi ve Yakın Eşleşmelerle YARA Regresyonu** konusunu ele alır. Çıktıların doğrudan gözlem mi, yorum mu olduğunu ayırmayı hedefler.

## Temel bilgiler

1. Kural testlerinde pozitif ve negatif örnek birlikte gerekir; negatif örnek olmadan yanlış pozitif davranışı görülemez.

2. Yakın eşleşme örneği olumluya benzer ancak kuralı karşılamamalıdır.

3. Kesinlik ve duyarlılık etiketli örneklemle sınırlıdır; sentetik sonuçlar gerçek malware tespit gücünü kanıtlamaz.

## Uygulama

Önce dosyayı oku, sonucu tahmin et, ardından çalıştır:

```bash
python fixtures.py && yara rules.yar samples/positive.txt && yara rules.yar samples/near_miss.txt
```

Generate synthetic corpus with `fixtures.py`. Positive must match; near_miss and negative must not.

## Görevler

1. Beklenen ve gözlenen sonuçları karşılaştır.
2. Bir pozitif ve bir negatif örneği belgele.
3. Tek bir göstergeyle kesin sonuç çıkarmanın riskini açıkla.
4. Kodu zararsız bir sınır değerle değiştir ve testi tekrarla.

## Bilgi kontrolü

- Girdi hangi güven sınırını geçiyor?
- Hangi veri eksik veya yanlış yorumlanabilir?
- Gerçek sistemde hangi bağımsız doğrulama gerekir?

## Güvenlik ve sınırlar

Gerçek zararlı dosyalar, saldırı hedefleri veya üretim sistemleri kullanılmaz. Bu küçük eğitim örneği saha performansı garantilemez.
