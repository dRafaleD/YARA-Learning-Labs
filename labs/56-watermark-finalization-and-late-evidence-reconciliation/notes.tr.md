# Lab 56 — Watermark Kapanışı ve Geç Kanıtın Yeniden Hesaplanması

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## 55. lab'den devam
Önceki gün geç gelen olayları **LATE** diye işaretledik. Peki olayın ait olduğu zaman aralığını **artık tamamlandı** diye kapattıysak?

**Watermark:** olay zamanının ne kadar ilerlediğine ilişkin sınır. **Finalization:** bir zaman grubunun tamamlandı kabul edilmesi. **Reconciliation:** yeni kanıt geldiğinde önceki rapor veya sayıları yeniden değerlendirme.

Hayalî sensör A, watermark değerini 120'ye çıkartıyor; `[100,120)` aralığı tamamlandı sayılıyor. Sonra zaman damgası 110 olan yeni bir olay geliyor. Bu olay silinmek yerine **RECONCILE** etiketi alıyor.

Sonuç: 8 ham kural eşleşmesi; 5 benzersiz kabul edilen olay; 4 alarm veren olay; 1 geç olay ve 1 tekrar kayıt.

## Çalıştır
YARA CLI gereklidir:
```bash
python3 labs/56-watermark-finalization-and-late-evidence-reconciliation/evaluate.py
```

## Sorular
Geç kayıt sayımları neden değiştirebilir? Watermark neden kesin gerçek zaman değildir? Aynı olayın tekrar kaydı niçin yeni olay sayılmamalı?

## Sınırlar
Yalnızca zararsız eğitim dizeleri ve sentetik kayıtlar kullanılır; gerçek malware veya SIEM yoktur.
