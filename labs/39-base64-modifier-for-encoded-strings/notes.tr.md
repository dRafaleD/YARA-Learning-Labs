# Lab 39 — Kodlanmış String'ler İçin base64 Değiştiricisi

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Kodlanmış String'ler İçin base64 Değiştiricisi** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `$s = "text" base64`, string'in Base64 kodlanmış halini olası üç hizalamanın herhangi birinde eşleştirir.
2. Değiştirici kodlanmış varyantları senin için üretir; kural okunabilir kalır.
3. Her iki biçimi de yakalamak istiyorsan düz bir `ascii` varyantı da tut.

## Kavramsal ayrımlar
- Değiştirici yalnızca standart Base64'ü eşleştirir; özel alfabeleri veya diğer kodlamaları değil.
- Kısa string'ler kodlamadan sonra çok sayıda tesadüfi eşleşme üretir.
- Eşleşme kodlu metnin var olduğunu gösterir; çözüldüğünü veya kullanıldığını değil.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/b64.txt
~~~

~~~bash
yara rules.yar samples/plain.txt
~~~

~~~bash
yara rules.yar samples/unrelated.txt
~~~


## Görevler
1. Hangi örneklerin eşleşeceğini tahmin et.
2. Kuralı her örnekte çalıştırıp sonucu not et.
3. Hex kodlu bir örnek ekle ve neden eşleşmediğini açıkla.
4. Bir güvenlik özelliği için assertion ekle.
5. Bir negatif senaryo ve bir yanlış pozitif ihtimali yaz.
6. Bağımsız bir doğrulama yöntemi öner.

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
