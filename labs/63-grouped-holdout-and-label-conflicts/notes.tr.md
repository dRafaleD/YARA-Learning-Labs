# Lab 63 — Gruplu Holdout ve Veri Etiketi Çelişkileri

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

62. lab'de tekrarların metriklere etkisini inceledik. Bugün taramadan önce geliştirme ve holdout kümelerinde aynı içeriğin bulunmasını SHA-256 ile kontrol ediyoruz. Aynı baytlar iki kümeye yayılırsa SPLIT_OVERLAP, aynı içeriğin etiketleri çelişirse LABEL_CONFLICT sonucu verilir. Temiz örnekte beş satır vardır; sadece üç holdout satırı zararsız BLUE-TOKEN kuralıyla taranır. Beklenen: TP=1, FP=0, TN=1, FN=1. Dört bütünlük senaryosunu tahmin et ve aynı küme içinde tekrar ekle. Tam hash eşitliği yakın kopyaları bulmaz veya bağımsız holdout garantilemez. Tarama için YARA CLI gerekir; gerçek malware yoktur.

## Çalıştır
```bash
python3 labs/63-grouped-holdout-and-label-conflicts/evaluate.py
```
