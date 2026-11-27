# Lab 64 — Grup Bazlı Tespit Metrikleri ve Toplam Yanlılığı

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

63. lab'de veri kümesi bütünlüğünü denetledik. Bugün grup bazlı recall ve yanlış pozitif oranlarını toplam metriklerle karşılaştırıyoruz. Zararsız BLUE-TOKEN kuralı A grubunu doğru sınıflandırır, B grubundaki iki örneği de yanlış sınıflandırır. Toplam recall 2/3, FPR 1/3; B grubunda recall sıfır, FPR birdir. Payda sıfırsa None döner. İki karışıklık matrisini elle hesapla ve A grubuna zararsız negatif örnek ekle. Toplam başarının zayıf alt grubu nasıl gizleyebildiğini açıkla. Altı hayalî örnek gerçek tespit başarısını göstermez. YARA CLI gerekir; gerçek malware yoktur.

## Çalıştır
```bash
python3 labs/64-per-group-detection-metrics/evaluate.py
```
