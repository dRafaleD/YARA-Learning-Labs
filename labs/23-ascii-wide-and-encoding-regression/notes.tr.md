# Lab 23 — ASCII, Wide String ve Kodlama Regresyon Testleri

[English](notes.md) | [Türkçe](notes.tr.md)

## Amaç

ASCII, Wide String ve Kodlama Regresyon Testleri konusunu gerçek sistemlere dokunmadan, yerel ve zararsız örneklerle çalışmak. Hedef yalnızca komutları ezberlemek değil; ölçümün neyi gösterdiğini ve neyi kanıtlamadığını anlamaktır.

## Birbiriyle bağlantılı konular

1. **ascii and wide modifiers**: Bu kavramın hangi problemi çözdüğünü, veri akışını ve sınırlamalarını açıklayın.
2. **UTF-16LE encoding**: Bu kavramın hangi problemi çözdüğünü, veri akışını ve sınırlamalarını açıklayın.
3. **false negative risk**: Bu kavramın hangi problemi çözdüğünü, veri akışını ve sınırlamalarını açıklayın.
4. **corpus tests**: Bu kavramın hangi problemi çözdüğünü, veri akışını ve sınırlamalarını açıklayın.
5. **precision and recall**: Bu kavramın hangi problemi çözdüğünü, veri akışını ve sınırlamalarını açıklayın.

## Ortamın hazırlanması ve çalışma

`rules.yar` dosyası sentetik eğitim örneğidir. İlgili lab klasöründe çalıştırın:

``bash
yara rules.yar samples/ascii.txt
```

``bash
yara rules.yar samples/wide.bin
```

``bash
yara rules.yar samples/negative.txt
```

## Adım adım analiz

1. Çalıştırmadan önce beklediğiniz sonucu not edin.
2. Gerçek çıktıyı ve kullandığınız aracın sürümünü kaydedin.
3. Gözlediğiniz olgular ile tahminlerinizi ayrı yazın.
4. Bir zararsız negatif test ekleyin; sonucu yeniden ölçün.
5. Yanlış pozitif, yanlış negatif ve eksik bağlam ihtimallerini düşünün.
6. Delil niteliğindeki örneği değiştirmeden önce kopyasını alın ve hash kaydedin.
7. Konfigürasyondaki bilgi ile çalışma zamanı sonucunu karşılaştırın.
8. Kesin bildikleriniz, belirsizlikler ve sonraki kontroller için kısa rapor yazın.

## Mini görevler

- **Başlangıç ölçümü:** örneği çalıştırıp çıktı, varsayım ve sınırlamaları belgeleyin.
- **Tek değişken:** zararsız bir işaretçi, log alanı veya ayarı değiştirip etkisini gözleyin.
- **Regresyon:** ilk ayara dönün ve beklenen sonucun korunduğunu doğrulayın.
- **Kanıt yorumu:** tek bir eşleşmenin ya da alarmın neden saldırı kanıtı olmadığını tartışın.

## Tekrar soruları

1. ascii and wide modifiers nedir, ne sağlar ve tek başına neyi kanıtlamaz?
2. UTF-16LE encoding nedir, ne sağlar ve tek başına neyi kanıtlamaz?
3. false negative risk nedir, ne sağlar ve tek başına neyi kanıtlamaz?
4. corpus tests nedir, ne sağlar ve tek başına neyi kanıtlamaz?
5. precision and recall nedir, ne sağlar ve tek başına neyi kanıtlamaz?
6. Analizin güvenilirliği için hangi ikinci kanıta ihtiyacınız var?
7. Aynı ölçümü başka bir makinede nasıl tekrarlarsınız?

## Güvenlik

Yalnızca kendi örnekleriniz ve açık izinli ortamlar üzerinde çalışın. Sentetik sonuçları gerçek vaka bulgusu gibi sunmayın.