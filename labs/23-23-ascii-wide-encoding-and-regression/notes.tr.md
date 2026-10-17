# Lab 23 — ASCII ve Wide String Tespiti ve Regresyon Örnekleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Hedef
ASCII ve Wide String Tespiti ve Regresyon Örnekleri konusunu tamamen yerel ve zararsız örneklerle öğrenmek. Gözlemlenen bulguyu yorumdan ayırmak ve kesin olmayan sonuçları abartmamak.

## Temel kavramlar
1. **ASCII versus UTF-16LE:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
2. **ascii and wide modifiers:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
3. **byte-level verification:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
4. **false positives and false negatives:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
5. **independent indicators:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
6. **negative sample regression:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.

## Uygulama
Lab klasöründe `encoding_rules.yar` dosyasını inceleyin ve şu komutları sırasıyla uygulayın:

```bash
python3 make_samples.py
```

```bash
yara encoding_rules.yar samples/ascii.txt
```

```bash
yara encoding_rules.yar samples/wide.bin
```

```bash
yara encoding_rules.yar samples/negative.txt
```

**Beklenen sonuç:** ASCII and UTF-16LE positive fixtures match; negative fixture does not.

## Analiz defteri
Kullandığınız araç sürümünü, komutu, girdiyi, gördüğünüz çıktıyı, beklenmeyen olayları ve olası açıklamaları kaydedin. Ölçülen veri ile çıkarımı ayrı başlıklar altında yazın.

## Uygulama görevleri
1. Orijinal örneği çalıştırıp çıktıyı kaydedin.
2. Zararsız bir girdiyi değiştirerek sonucu önceden tahmin edin.
3. Bir negatif test ekleyin ve gerçekten hangi kontrolün başarısız olduğunu belirleyin.
4. Başlangıç dosyasına dönüp regresyon testi yapın.
5. İki olası yanlış pozitif açıklaması üretin.
6. Sonucu doğrulayacak bağımsız bir kanıt kaynağı önerin.
7. Belirsizlikleri açıkça yazan kısa bir rapor hazırlayın.

## Tekrar soruları
1. ASCII versus UTF-16LE nedir, ne işe yarar, neyi garanti etmez?
2. ascii and wide modifiers nedir, ne işe yarar, neyi garanti etmez?
3. byte-level verification nedir, ne işe yarar, neyi garanti etmez?
4. false positives and false negatives nedir, ne işe yarar, neyi garanti etmez?
5. independent indicators nedir, ne işe yarar, neyi garanti etmez?
6. negative sample regression nedir, ne işe yarar, neyi garanti etmez?
7. Sonucun güvenilirliğini nasıl artırırsınız?
8. Hangi kontrolü otomatik regresyon testine dönüştürürsünüz?

## Kapsam
Bu lab yalnızca izinli, sentetik veriler içindir. Tek bir bulguyu kesin saldırı kanıtı saymayın.
