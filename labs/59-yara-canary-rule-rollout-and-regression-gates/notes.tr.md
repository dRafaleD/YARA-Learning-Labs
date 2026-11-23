# Lab 59 — YARA Canary Testi ve Kural Yayın Kontrolü

[English](notes.md) · [Türkçe](notes.tr.md) · [V1](rules_v1.yar) · [V2](rules_v2.yar) · [V3](rules_v3.yar) · [Değerlendirme](evaluate.py)

## 58. lab'den devam
Önceki gün V1 ve V2 kurallarının aynı veri kümesinde farklı alarm sayıları üretebildiğini gördük. Şimdi yeni kuralı yayınlamadan önce **beklenmedik değişiklikleri kontrol ediyoruz**.

**Canary test:** küçük ve bilinen örnek kümesiyle önce deneme yapmak. **Regression:** yeni sürümde eskiden olmayan olumsuz davranışın ortaya çıkması. **Promotion gate:** yeni kuralın kabul edilme koşulu.

Dört zararsız olayımız var. V1 `e1,e3`, V2 `e1,e2,e3` buluyor; bu beklenen genişleme. V3 yanlışlıkla sıradan `e4` metnini de işaretliyor. Kontrol sistemi V2 için `PROMOTE_CANDIDATE`, V3 için `QUARANTINE` dönüyor.

## Çalıştır
YARA komut satırı aracı gereklidir:
```bash
python3 labs/59-yara-canary-rule-rollout-and-regression-gates/evaluate.py
```

## Sorular
Sadece toplam alarm sayısına bakmak neden yetmez? Canary örneği çok küçükse hangi sonuçları genelleyemeyiz? Rule SHA-256 neden kaydedilmeli?

## Sınırlar
Gerçek malware, gerçek SIEM veya üretim kuralı kullanılmaz.
