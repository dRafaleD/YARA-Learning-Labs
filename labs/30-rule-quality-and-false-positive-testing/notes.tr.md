# Lab 30 — Sentetik Örneklerle YARA Kural Kalitesinin Ölçülmesi

[English](notes.md) · [Türkçe](notes.tr.md)

## Hedef
YARA kuralını yalnızca bir eşleşmeyle değil, önceden etiketlenmiş **zararsız sentetik dosyalar** üzerinde değerlendir. Karışıklık matrisi ve yanlış pozitif kavramlarını öğren.

## Temel kavramlar
- **TP (doğru pozitif):** Pozitif dosya doğru yakalandı.
- **FP (yanlış pozitif):** Negatif dosya yanlışlıkla yakalandı.
- **TN (doğru negatif):** Negatif dosya doğru şekilde eşleşmedi.
- **FN (yanlış negatif):** Pozitif dosya kaçırıldı.
- **Kesinlik (precision):** TP/(TP+FP); **duyarlılık (recall):** TP/(TP+FN). Payda sıfırsa sonuç tanımsızdır.

Bir metin eşleşmesi, dosyanın zararlı olduğunu kanıtlamaz. Örneklemin nasıl seçildiği sonucu değiştirir.

## Uygulama
```bash
python3 make_samples.py
yara rules.yar samples/positive_1.txt
yara rules.yar samples/negative_1.txt
python3 evaluate.py
```

`evaluate.py` sistemdeki YARA komutunu çalıştırıp etiketlerle karşılaştırır.

## Görevler
1. `negative_2.txt` örneğinin neden yanıltıcı olabileceğini açıkla.
2. Kuralı değiştirip TP/FP/TN/FN değerlerini yeniden hesapla.
3. İki yeni zararsız örnek ekle.
4. Bu küçük veri kümesinin gerçek malware tespiti için neden yeterli olmadığını yaz.

## Güvenlik
Gerçek zararlı örneği kullanılmaz. Bu çalışma saha performansı iddiası değildir.
