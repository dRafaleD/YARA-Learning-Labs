# Lab 51 — YARA Kural Çakışması ve Alarm Tekilleştirmesi

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## 50. günden devam
Bir örnek birden fazla YARA kuralıyla eşleşebilir. **Kural eşleşmesi sayısı**, **benzersiz dosya sayısı** ile aynı değildir. Her eşleşmeyi ayrı zararlı dosya gibi saymak istatistiği şişirir.

**Rule overlap:** farklı kuralların aynı dosyayı işaretlemesi. **Alert deduplication:** aynı dosya/olay için yinelenen alarmı birleştirme. **Sample-level metrics:** TP, FP, TN ve FN değerlerini kural eşleşmesi değil, benzersiz örnek bazında ölçme.

Hayalî beş metin dosyasında üç basit kural toplam **8 eşleşme** üretir ama sadece **4 benzersiz dosya** eşleşir. Örnek seviyesinde TP=2, FP=2, TN=1, FN=0 elde edilir. Bunlar gerçek zararlı yazılım etiketleri değildir.

## Çalıştır
YARA CLI kurulu olmalı:
~~~bash
python3 labs/51-rule-overlap-alert-deduplication-and-sample-metrics/evaluate.py
~~~

## Sorular
Sekiz kural alarmı neden sekiz dosya anlamına gelmez? Dosya hash'ine göre tekilleştirmenin sınırları nedir? Gerçek SOC ortamında tekrar alarmlar neden sorun olabilir?

## Sınırlar
Gerçek malware veya tespit kuralı yoktur; tamamen zararsız eğitim verileri kullanılır.
