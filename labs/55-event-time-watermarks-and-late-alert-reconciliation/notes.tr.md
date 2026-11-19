# Lab 55 — Olay Zamanı Watermark ve Geciken Alarm Uzlaştırma

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## 54. lab'den devam
Önceki gün **olay zamanı** ile logun sisteme **ulaşma zamanını** ayırdık. Bu kez geç gelen kayıtların nasıl raporlanacağını öğreniyoruz.

**Watermark:** akıştaki olayların ne kadar gecikmiş olabileceğine ilişkin eşik. Hayalî sistem, her sensör için görülen en büyük olay zamanından 10 saniye çıkarıyor. Daha eski zamanlı yeni bir olay gelirse **LATE** diyor fakat kaydı **silmeden saklıyor**.

Aynı sensör ve olay ID'si ile gelen değişmemiş kayıt **DUPLICATE**, içeriği farklı kayıt **CONFLICT** oluyor. Sonuç: 9 ham YARA kural eşleşmesi, 5 benzersiz kabul edilen olay, 4 alarm veren olay, 1 gecikmiş olay, 1 tekrar ve 1 çelişki.

## Çalıştır
YARA komut satırı aracı gerekli:
```bash
python3 labs/55-event-time-watermarks-and-late-alert-reconciliation/evaluate.py
```

## Sorular
Neden olay zamanı ile logun geliş zamanı farklı olabilir? Geç kayıtları neden silmemeliyiz? Sensör saatleri yanlışsa watermark neyi yanlış sınıflandırabilir?

## Sınır
Gerçek malware veya SIEM kullanılmaz; sadece zararsız metinler ve sentetik olaylar.
