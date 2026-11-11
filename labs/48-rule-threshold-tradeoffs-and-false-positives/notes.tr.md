# Lab 48 — YARA Eşik Değerleri, Duyarlılık ve Yanlış Pozitifler

[English](notes.md) · [Türkçe](notes.tr.md) · [Kurallar](rules.yar) · [Çevrimdışı ölçüm](evaluate.py)

## 47. lab'den devam
47. lab'de eğitim ve test kümelerinde birbirine çok benzeyen dosyaların bulunmasının sonuçları yanıltabileceğini görmüştük. Şimdi düzgün ayrılmış bir testte başka bir soruyu inceleyelim: **Bir YARA kuralı kaç gösterge aramalı?**

Az koşullu kural daha çok dosyada eşleşebilir; fakat zararsız dosyalar da alarm üretebilir. Çok sıkı kural yanlış alarmları azaltabilir; bu kez bazı gerçek pozitifleri kaçırabilir.

## Üç kural
Tamamen uydurma üç etiketimiz var: BLUE-TOKEN, GREEN-TOKEN ve ORANGE-TOKEN. Aynı metinler için üç kuralı karşılaştırıyoruz:
- **Any-marker:** Üçünden en az biri bulunsun.
- **Two-marker:** Üçünden en az ikisi bulunsun.
- **All-marker:** Üçü de bulunsun.

İki dosyaya eğitim senaryosu gereği **pozitif**, üçüne **negatif** etiketi veriyoruz. Bu etiketler malware olup olmadıklarını göstermez; sadece bu deneye ait beklenen sınıflardır.

## Beklenen karışıklık matrisi
| Kural | TP | FP | TN | FN |
| --- | ---: | ---: | ---: | ---: |
| Any-marker | 2 | 2 | 1 | 0 |
| Two-marker | 2 | 1 | 2 | 0 |
| All-marker | 1 | 0 | 3 | 1 |

**TP:** pozitif olup yakalanan. **FP:** negatif olduğu hâlde alarm veren. **TN:** negatif olup alarm vermeyen. **FN:** pozitif olduğu hâlde kaçan.

**Precision (kesinlik)** = TP / (TP + FP). **Recall (duyarlılık)** = TP / (TP + FN). Payda 0 ise sonuç tanımsızdır.

## Uygulama
YARA CLI kurulu olmalı:
~~~bash
yara --version
python3 evaluate.py
~~~
Python dosyası beş zararsız metni geçici klasöre yazar, üç kuralı aynı dosyalarda çalıştırır, sonuçları ölçer ve assert ile denetler.

## Görevler
1. İki gösterge arayan kural niçin bir yanlış pozitif üretmiş?
2. En yüksek kesinlik, en iyi kuralın kesin kanıtı mıdır?
3. Üç etiketi de içeren **negatif** dosya ekle; hangi sonuçlar değişir?
4. Tek etiketli **pozitif** dosya ekle; hangi kurallar kaçırır?
5. Kural eşiğini test sonuçlarına göre tekrar tekrar değiştirmek neden aşırı uyum doğurabilir?
6. Eşleşmeyi dosya formatı, konum, kaynak ve ek kanıtla nasıl doğrularsın?

## Sınırlar
Gerçek zararlı yazılım veya indirilebilir şüpheli örnek yoktur. YARA eşleşmesi tek başına **zararlı yazılım kanıtı değildir**. Küçük sentetik kümeden gerçek dünya başarısı iddia edilmez.
