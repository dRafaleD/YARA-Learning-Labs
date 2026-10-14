# Lab 20 — Tespit Metrikleri, Corpus Etiketleri ve Regression Test

[English](notes.md) · [Türkçe](notes.tr.md)

**Amaç:** Lab 18–19'daki quality ve entropy bilgisini ölçülebilir detection test pipeline'ına dönüştürmek.

Gerekenler: Python 3.9+, YARA CLI. Tamamen zararsız metin örnekleriyle çalışılır.

## 1. Ground truth önceden tanımlanmalı

Rule testi için etiketleri taramadan önce tanımla. Buradaki manifest dosyası expected positive/negative örnekleri tutar. Bu etiketler gerçek malware analist kararı değil, yalnızca sentetik eğitim senaryosuna aittir.

## 2. Confusion matrix

TP hedef pozitifin eşleşmesi, FP negatifin yanlış eşleşmesi, FN hedefin kaçırılması, TN negatifin doğru dışlanmasıdır. Bu sayılar test corpus'una bağlıdır; her yerde geçerli oran değildir.

## 3. Precision ve recall

Precision = TP/(TP+FP), recall = TP/(TP+FN). Payda sıfırsa değer tanımsızdır, otomatik %100 değildir. Precision testteki alertlerin isabetini, recall ise labeled-positive kapsamını gösterir.

## 4. Broad marker ve gürültü

Sadece LAB20_SIGNAL arayan rule sıradan eğitim notlarına da match olabilir; böylece false positive oluşur. Broad indicator keşif için yararlı olabilir ancak tek başına güvenilir tespit olarak sunulmamalı.

## 5. Contextual condition

Sıkı rule marker + component + active mode ve size sınırını beraber arar. Bizim corpus'ta FP'yi azaltır ama alanları farklı hedefleri kaçırabilir. Çok şart eklemek evrensel kalite garantisi değildir.

## 6. Regression test

Rule değişince pozitif, benign negatif ve near-miss örnekleri tekrar tara. Script beklenen strict sonuç değişirse nonzero exit verir. Böylece accidental drift yakalanır; gerçek deployment öncesi temsil gücü yüksek corpus yine şarttır.

## 7. Dataset leakage

Bütün pozitif dosyalar aynı yapay marker'ı taşıyorsa rule buna overfit olup kusursuz görünebilir. Gerçek kalite için bağımsız kaynaklar, farklı sürümler ve representative benign örnekler gerekir. Bu labda overfitting bilinçli gösteriliyor.

## 8. Ölçüm sınırları

Az sayıda sentetik örnek öğreticidir fakat production detection confidence vermez. Precision/recall raporunda scope, corpus, rule version, YARA engine ve label yöntemini mutlaka belirt.

## 9. İnceleme akışı

YARA match doğrudan malware verdict değil, triage sinyali olmalı. Artifact hash'i, eşleşen string, dosya formatı, kaynak ve davranış gibi kanıtları birleştir.

## 10. CI disiplini

CI belirli YARA sürümünü kurup test scriptini çalıştırabilir. Dependency ve sonuçları kaydet. Gerçek şüpheli dosyaları açık repoya koyma; corpus label'larını da version control içinde tut.

## Yerel test

Lab klasöründe:

```bash
python3 generate_corpus.py
yara --version
yara -s test_rules.yar samples/positive-01.txt
yara -s test_rules.yar samples/negative-marker.txt
python3 evaluate_rules.py
```

Generator 3 pozitif ve 5 negatif zararsız dosya ile `labels.json` üretir. Evaluator her dosyada YARA CLI'yı çalıştırır, TP/FP/TN/FN hesaplar ve sıkı kuralın beklenen confusion matrix değerini assert eder. YARA yüklü değilse test bunu açıkça bildirir.

### Beklenen sonuç

| Rule | TP | FP | TN | FN |
| --- | ---: | ---: | ---: | ---: |
| Lab20_Contextual_Detection | 3 | 0 | 5 | 0 |
| Lab20_Broad_Marker | 3 | 2 | 3 | 0 |

Bu sayılar **sadece hazırlanan bu sekiz dosya** içindir. Üretimdeki malware detection yüzdesi değildir.

## Mini challenge

1. Bir pozitif dosyada mode=active yerine mode=idle yap; label'ı nasıl değiştirmen gerektiğini tartış ve testin fail olmasını incele.
2. Broad rule'a ikinci indicator ekle. FP sayısı ve recall etkisini karşılaştır.
3. Yeni benign near-miss ekleyip `labels.json` güncelle; regression testini tekrar çalıştır.
4. `eval` scriptine basit F1 hesabı ekle, sıfır payda kontrolünü koru.

## Alıştırmalar

1. Rule'ları elle incele.
2. Corpus'u üret.
3. Sample'ların SHA-256 hash'lerini çıkar.
4. Labels JSON'u oku.
5. İki rule'ı pozitif dosyada dene.
6. Broad rule için FP olan dosyayı bul.
7. Confusion matrix'i elle hesapla.
8. Precision hesapla.
9. Recall hesapla.
10. Otomatik regression test çalıştır.
11. Bir negatif varyant ekle.
12. Tespit sınırlarını beş cümleyle raporla.

## Tekrar soruları

1. Ground truth nedir?
2. TP ne demektir?
3. FP neden maliyetlidir?
4. FN neden tehlikeli olabilir?
5. TN nasıl sayılır?
6. Precision formülü?
7. Recall formülü?
8. Sıfır payda durumunda ne yapılır?
9. Rule ne zaman overfit olur?
10. Broad indicator ne zaman uygun?
11. Regression test neden gerekli?
12. Corpus'un temsil gücü neden önemli?
13. YARA eşleşmesi neden otomatik malware kanıtı değildir?
14. Rule version neden kaydedilmeli?
15. Üretim sonuçlarına geçmeden hangi validasyonlar gerekir?

**Ana çıkarım:** Detection rule'un kalitesi, yalnızca çalışmasıyla değil, *etiketli corpus üzerinde tekrar üretilebilir ölçümler ve açık sınırlamalarla* değerlendirilir.
