# Lab 50 — YARA Kurallarında Gruplara Ayrılmış Performans Ölçümü

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## 49. günden devam
Önceki gün temel oranın sonuçlara etkisini gördük. Şimdi **stratification (katmanlara ayırma)** kavramını öğreniyoruz: bir kuralın başarısını tüm örneklerde tek sayı olarak vermek yerine alt gruplarda ayrı ölçmek.

İki hayalî grup var: alpha ve beta. Kurallar yalnızca `BLUE-TOKEN` ve `GREEN-TOKEN` gibi zararsız yazıları arar. **Any** kuralında alpha için TP=2, FP=1; beta için TP=2, FP=3. Yani aynı kural beta grubunda daha fazla yanlış alarm üretir. **Both** kuralı iki grupta da birer gerçek pozitifi kaçırır.

## Çalıştır
YARA komut satırı aracı kurulu olmalı:
```bash
python3 labs/50-stratified-rule-evaluation-and-hidden-false-positives/evaluate.py
```

## Sorular
Toplu başarı oranı neden bir gruptaki hataları saklayabilir? Precision, recall ve false-positive ölçülerini gruplara göre neden ayrı hesaplamalıyız? Holdout kümeleri nasıl ayrılmalı?

## Güvenlik
Gerçek zararlı yazılım veya gerçek tespit kuralı yoktur; sadece geçici sentetik metinler kullanılır.
