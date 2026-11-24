# Lab 60 — Canary Holdout ve Etiketli Regresyon Kümesi

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules_v1.yar](rules_v1.yar) · [rules_v2.yar](rules_v2.yar)

59. lab'de canary testini yaptık. Bugün ayrı bir **holdout (geliştirmeden ayrı değerlendirme kümesi)** kullanıyoruz. Daha geniş kural geliştirme kümesindeki kaçırılan örneği buluyor ama holdout içindeki zararsız renk açıklamasını da işaretliyor. TP, FP, TN, FN değerleri iki küme için ayrı hesaplanıyor; kural SHA-256 değeri kaydediliyor.

**Sorular:** Holdout neden kural geliştirme sırasında kullanılmamalı? Geliştirme kümesinde recall artması neden tek başına yeterli değil? Yanlış pozitif görünce ne yapılmalı?

Altı hayalî metin gerçek malware değildir. Bu küçük örnek gerçek dünyadaki yanlış pozitif oranını ölçemez. YARA CLI gereklidir.

## Çalıştır
```bash
python3 labs/60-canary-holdout-and-labeled-regression-corpus/evaluate.py
```
