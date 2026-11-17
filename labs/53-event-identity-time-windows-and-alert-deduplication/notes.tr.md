# Lab 53 — Olay Kimliği, Zaman Pencereleri ve YARA Alarm Tekilleştirme

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## 52. lab'den devam
SHA-256'ya göre aynı içerikleri tek saymak, **kaç farklı bayt dizisi** gördüğümüzü gösterir. Ama aynı dosya farklı bilgisayarlarda veya saatlerde görülebilir. Bu nedenle hash sayısı **olay sayısı** değildir.

Bu lab, farklı sayım düzeylerini karşılaştırıyor:
- **Raw rule matches:** 11 kural eşleşmesi.
- **Unique event IDs:** 5 farklı alarm üreten olay kimliği.
- **Unique hashes:** 2 farklı eşleşen içerik.
- **Toy incident grouping:** makine, içerik özeti ve 60 saniyelik zaman dilimine göre 4 grup.

**Time bucket (zaman kovası):** olayları belirli zaman aralığına bölerek gruplama. Gerçek bir olay zaman diliminin sınırını aşabilir; iki ilgisiz olay aynı gruba düşebilir. Bu yüzden örnek gruplar **kesin olay kimliği değildir**.

## Çalıştırma
YARA CLI kurulu olmalı:
~~~bash
python3 labs/53-event-identity-time-windows-and-alert-deduplication/evaluate.py
~~~

## Sorular
Aynı hash niçin aynı olayı kanıtlamaz? Bir olayın iki kez loglanmasını nasıl ayırırız? Zaman penceresi ne tür yanlış birleştirmeler yapabilir?

## Sınır
Gerçek zararlı yazılım yoktur. Eğitim metinleri ve hayalî olay kayıtları kullanılır; bu sayılar gerçek tespit başarısı değildir.
