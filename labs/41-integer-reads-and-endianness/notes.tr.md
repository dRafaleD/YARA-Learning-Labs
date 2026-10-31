# Lab 41 — Tamsayı Okumaları ve Endianness

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Tamsayı Okumaları ve Endianness** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `uint32(0)` offset 0'daki dört baytı little-endian, `uint32be(0)` ise big-endian okur.
2. `4C 41 42 34` baytları little-endian okununca `0x3442414C`, big-endian okununca `0x4C414234` verir.
3. Dosya biçiminin alanlarını nasıl belgelediğine uyan biçimi seç.

## Kavramsal ayrımlar
- Dosya sonunun ötesini okumak tanımsız değer verir ve koşul başarısız olur; `filesize`'ı da kontrol et.
- ASCII metin her iki durumda aynıdır; yalnızca sayı farklıdır.
- Baytlar okunabilir kalsın diye sabiti hex olarak yaz.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/lab4.bin
~~~

~~~bash
yara rules.yar samples/short.bin
~~~


## Görevler
1. Üç kuraldan hangilerinin örnekle eşleşeceğini tahmin et.
2. Kural kümesini iki örnekte çalıştırıp sonuçları not et.
3. İki kuraldaki sabitleri değiştir ve sonucu açıkla.
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
