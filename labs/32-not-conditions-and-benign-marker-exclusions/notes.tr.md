# Lab 32 — not Koşulları ve Zararsız İşaretçi Dışlamaları

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **not Koşulları ve Zararsız İşaretçi Dışlamaları** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `not $benign`, bilinen iyi dosyaları tanıtan bir işaretçi string bulunduğunda kuralın eşleşmemesini sağlar.
2. Dışlamalar yanlış pozitifleri azaltır ama bir atlatma yolu açar: işaretçiyi yerleştiren saldırgan kuraldan kaçar.
3. Dışlamaları ikinci bir bağımsız sinyalle eşleştir ve dışlanan durumu ayrıca test et.

## Kavramsal ayrımlar
- Zararsız bir işaretçi dosyanın geri kalanı hakkında hiçbir şey kanıtlamaz; yalnızca bir gelenektir.
- Dışlamayı olabildiğince dar tut; örneğin bir başlığa veya dosya boyutu aralığına bağla.
- Her dışlamanın nedenini yaz; doğru olmaktan çıktığında kaldırılabilsin.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/suspicious.txt
~~~

~~~bash
yara rules.yar samples/suspicious_with_benign.txt
~~~

~~~bash
yara rules.yar samples/benign_only.txt
~~~


## Görevler
1. Kuralın üç örnekten hangisiyle eşleşeceğini tahmin et.
2. Kuralı her örneğe karşı çalıştırıp sonucu not et.
3. `not $benign` ifadesini kaldır ve hangi örneğin eşleşmeye başladığını anlat.
4. Yalnızca zararsız işaretçi taşıyan dosyanın eşleşmediğini kanıtlayan bir test ekle.
5. Saldırganın dışlamayı nasıl kötüye kullanabileceğini ve bir sertleştirme yolunu anlat.
6. Bağımsız bir kontrol öner (hash izin listesi veya imzalı dosya kontrolü gibi).

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
