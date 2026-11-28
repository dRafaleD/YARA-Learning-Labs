# Lab 65 — Grup Bazında Makro ve Mikro Tespit Ortalamaları

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](evaluate.py) · [rules.yar](rules.yar)

64. lab'de grup başına tespit metriklerini karşılaştırdık. Bugün altı hayalî metin eşit olmayan iki gruba ayrılıyor. A recall 1/1, B recall 1/3. Makro recall grup ortalamasıdır: 2/3. Mikro recall pozitif örnekleri birleştirir: 2/4 = 1/2. Pozitifi olmayan grubun tanımsız recall değeri sıfır sayılmaz. Tarama öncesinde altı aritmetik kontrol vardır. İki ortalamayı elle hesapla, pozitifsiz grup ekle ve B grubuna kaçırılmış pozitif ekle. Sonuçları yorumla. Gerçek malware yoktur; tarama için YARA CLI gerekir.

## Çalıştır
```bash
python3 labs/65-per-group-macro-and-micro-averages/evaluate.py
```
