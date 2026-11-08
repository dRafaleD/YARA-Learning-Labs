# Lab 45 — YARA Kural Sürümleri ve Metrik Regresyonu

[English](notes.md) · [Türkçe](notes.tr.md) · [Kural v1](rules_v1.yar) · [Kural v2](rules_v2.yar) · [Ölçüm](evaluate.py)

## Bu lab neden önemli?
44. labda etiketli pozitif ve negatif test dosyalarını çalışmıştık. Bir kuralda değişiklik yapmak onu otomatik olarak iyileştirmez. Aynı etiketli veri kümesinde **önceki ve sonraki TP/FP/TN/FN sayılarını karşılaştırmak** gerekir.

## Kural sürümleri
- **v1**, yalnızca `DOC-ALPHA` metnini arar. Bu ifade zararsız bir kullanım kılavuzunda da varsa yanlış pozitif üretir.
- **v2**, ayrıca `ACTION-VERIFY` metnini zorunlu tutar. Bu örneklerde yanlış pozitifi azaltır; fakat gelecekte bazı gerçek pozitifleri de kaçırabilir.

Daha fazla koşul eklemek, gerçek dünyada mutlaka daha iyi tespit yapmak demek değildir.

## Uygulama
Önce sisteminde YARA komut satırı programı (`yara`) yüklü olmalı:

```bash
python3 evaluate.py
```

Program geçici dizinde **iki pozitif, iki negatif zararsız metin** oluşturur; iki kuralı aynı dosyalara uygular ve metrikleri hesaplar.

- **TP:** Pozitif örnek yakalandı. **FP:** Negatif örnek yanlış yakalandı.
- **TN:** Negatif örnek eşleşmedi. **FN:** Pozitif örnek kaçırıldı.
- **Kesinlik:** TP/(TP+FP); **duyarlılık:** TP/(TP+FN). Payda sıfırsa değer **tanımsızdır**.

Beklenen sonuç: **v1 TP=2, FP=1, TN=1, FN=0** ve **v2 TP=2, FP=0, TN=2, FN=0**.

## Görevler
1. Zararsız yakın eşleşme örneğinin v1 tarafından neden yakalandığını açıkla.
2. Yalnız `DOC-ALPHA` içeren yeni pozitif dosya ekle; v2 duyarlılığı nasıl değişiyor?
3. YARA sürümünü, test etiketlerini ve kural sürümünü raporla.
4. Dört örnekten gerçek malware performansı çıkarılamayacağını gerekçelendir.
5. Ayrı ve kilitli bir test kümesi nasıl oluşturulur, tartış.

## Güvenlik
Gerçek zararlı dosya kullanılmaz. Bu metrikler yalnız dört sentetik örneğe aittir; YARA eşleşmesi tek başına zararlılık kanıtı değildir.
