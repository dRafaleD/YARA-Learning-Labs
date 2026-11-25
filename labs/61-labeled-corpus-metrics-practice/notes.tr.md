# Lab 61 — Uygulama Günü: Etiketli Veri Kümesi ve Tespit Metrikleri

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules_v1.yar](rules_v1.yar) · [rules_v2.yar](rules_v2.yar)

12 zararsız etiketli metni iki YARA kural sürümüyle tara. Pozitif etiket yalnızca hayalî eğitim görevindeki ilgili örneği ifade eder, malware anlamına gelmez.

| Metrik | V1 | V2 |
|---|---:|---:|
| TP | 3 | 5 |
| FP | 1 | 2 |
| TN | 5 | 4 |
| FN | 3 | 1 |
| Precision | %75,0 | %71,4 |
| Recall | %50,0 | %83,3 |
| F1 | %60,0 | %76,9 |
| Yanlış pozitif oranı | %16,7 | %33,3 |

Precision = TP/(TP+FP), recall = TP/(TP+FN), FPR = FP/(FP+TN). F1 precision ve recall'un harmonik ortalamasıdır. Tanımsız oranlar None ile gösterilir.

**Alıştırmalar:** İki karışıklık matrisini elle çiz. 24 tarama sonucunu tahmin et. F1 hesabını yap. İki zararsız negatif örnek ekleyip sayıları tekrar hesapla. Recall artarken yanlış pozitiflerin nasıl değiştiğini yorumla. Değerlendirme verisiyle kural ayarladıktan sonra bağımsız doğrulama iddiasında bulunma.

Beklenen son satır: 24 sample evaluations + 7 metric checks passed. YARA CLI gerekir; gerçek malware veya ağ erişimi yoktur.

## Çalıştır
```bash
python3 labs/61-labeled-corpus-metrics-practice/evaluate.py
```
