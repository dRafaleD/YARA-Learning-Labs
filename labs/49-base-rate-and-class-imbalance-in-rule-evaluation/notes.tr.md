# Lab 49 — YARA Ölçümünde Sınıf Dengesizliği ve Temel Oran

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## Önceki günden devam
48. lab'de katı ve esnek kural eşiklerini karşılaştırdık. Şimdi önemli bir ayrıntı: **gerçek pozitifler çok azsa aynı kuralın uyarıları daha az güvenilir olabilir.**

**Prevalence / base rate (temel oran):** veri kümesinde gerçek pozitiflerin oranı.
**Precision (kesinlik):** TP / (TP + FP). Uyarıların kaçı gerçekten pozitif?
**Recall (duyarlılık):** TP / (TP + FN). Gerçek pozitiflerin kaçı yakalandı?
**False-positive rate:** FP / (FP + TN). Gerçek negatiflerin kaçı yanlış alarm oldu?
**Class imbalance:** bir sınıfın diğerinden çok daha yaygın olması.

## Tamamen zararsız test
YARA kuralları yalnızca `BLUE-TOKEN` ve `GREEN-TOKEN` metinlerini arar:
- **Any:** birini görse eşleşir.
- **Both:** ikisini de görmeli.

İki pozitif örnek; biri iki işareti, biri yalnızca BLUE'yu içeriyor. On sekiz negatif örnekten üçü BLUE içeriyor, kalanları düz metin. Dengeli deneyde 2 pozitif + 2 negatif, düşük oranlı deneyde 2 pozitif + 18 negatif var.

| Veri kümesi | Kural | TP | FP | TN | FN | Precision | Recall |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Dengeli | Any | 2 | 2 | 0 | 0 | 0.50 | 1.00 |
| Dengeli | Both | 1 | 0 | 2 | 1 | 1.00 | 0.50 |
| Pozitif nadir | Any | 2 | 3 | 15 | 0 | 0.40 | 1.00 |
| Pozitif nadir | Both | 1 | 0 | 18 | 1 | 1.00 | 0.50 |

**Dikkat:** bunlar özellikle tasarlanmış hayalî veriler. Gerçek malware tespit başarısını göstermez. Karar vermek için bağımsız, doğru etiketlenmiş bir test kümesi gerekir.

## Çalıştırma
YARA CLI kurulu olmalı:
~~~bash
python3 labs/49-base-rate-and-class-imbalance-in-rule-evaluation/evaluate.py
~~~
Betik zararsız metin dosyalarını geçici dizinde üretir, gerçek YARA CLI ile kuralları çalıştırır ve TP/FP/TN/FN sayar.

## Sorular
1. Precision ile recall farkı nedir?
2. Pozitifler az olduğunda yanlış pozitif neden daha önemli olur?
3. Eşiği sıkılaştırmak her zaman iyi midir?
4. Holdout kümesi neden bağımsız olmalı?
5. YARA eşleşmesi neden zararlı yazılım kanıtı değildir?

## Güvenlik
Gerçek zararlı örnek yoktur. Yalnızca yerel, yapay metin kullanılır.
