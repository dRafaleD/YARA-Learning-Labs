# Lab 54 — Geciken Olaylar, Çakışan Kimlikler ve Alarm Tekilleştirme

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## 53. lab'den devam
Önceki gün ham kural eşleşmesi, olay kimliği ve zaman penceresiyle sayım yapmayı öğrendik. Şimdi **gecikmiş log** ve **aynı kimlikle farklı kayıt** sorunlarını görüyoruz.

**Event time:** olayın kaynakta gerçekleştiği zaman. **Ingestion time:** kayıt toplayıcıya ulaştığı zaman. **Duplicate:** aynı kaydın tekrar gelmesi. **Conflict:** aynı `(producer, event ID)` ile çelişkili veri gelmesi.

Hayalî veride 7 gözlem, 9 ham YARA kural eşleşmesi, 4 benzersiz uyarı veren olay, 1 tekrar ve 1 çelişki vardır. Bir uyarı olaydan 20 saniyeden fazla sonra ulaşır. Çelişkili kayıt otomatik olarak yeni bir olay kabul edilmez; ayrıca incelenir.

## Çalıştırma
YARA CLI kurulu olmalıdır:
~~~bash
python3 labs/54-delayed-events-conflicting-ids-and-alert-deduplication/evaluate.py
~~~

## Sorular
Geç gelen log neden zararlı demek değildir? Aynı olay ID farklı sensörlerde ne anlama gelir? Çelişkili kayıtları neden silmeden saklamalıyız?

## Sınırlar
Gerçek malware veya ağ taraması yoktur; bütün veri zararsız sentetik metindir.
