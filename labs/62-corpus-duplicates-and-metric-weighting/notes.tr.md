# Lab 62 — Veri Kümesi Tekrarları ve Metrik Ağırlıkları

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

61. lab'de precision, recall ve F1 ölçtük. Bugün tekrarlanan gözlemler ile benzersiz içerikleri ayırıyoruz. Yedi zararsız gözlem dört farklı SHA-256 özetine karşılık gelir. Aynı pozitif örneğin tekrarlanması benzersiz içerik kapsamasını artırmadan metrikleri yükseltebilir.

| Sayım | Gözlem | Benzersiz içerik |
|---|---:|---:|
| TP | 3 | 1 |
| FP | 1 | 1 |
| TN | 2 | 1 |
| FN | 1 | 1 |

Gözlem bazında precision ve recall %75, benzersiz içerikte ikisi de %50 olur. Analiz birimini raporda belirtmek gerekir. Aynı içeriğe farklı etiket verilirse çelişki bildirilir.

**Alıştırma:** negatif bir gözlemi tekrar ekle ve iki tabloyu yeniden hesapla. Çelişkili etiket ekleyip reddi doğrula. Yedi tarama ve altı kontrol vardır. YARA CLI gereklidir; gerçek malware kullanılmaz.

## Çalıştır
```bash
python3 labs/62-corpus-duplicates-and-metric-weighting/evaluate.py
```
