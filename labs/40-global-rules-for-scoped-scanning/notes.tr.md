# Lab 40 — Kapsamlı Tarama İçin Global Kurallar

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Kapsamlı Tarama İçin Global Kurallar** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `global rule` her dosya için değerlendirilir ve aynı kümedeki diğer kurallar yalnızca tüm global kurallar sağlandığında eşleşebilir.
2. Her kurala uygulanması gereken azami dosya boyutu gibi kapsam sınırları için temiz bir yerdir.
3. Global kural eşleşme listesinde kendisi de görünür; çıktıyı bir filtre sonucu ve eşleşen kural olarak oku.

## Kavramsal ayrımlar
- Global kural dosyadaki her kuralı değiştirir; bunu belirgin şekilde belgele.
- Aynı işaretçiyi taşıyan küçük ve büyük bir dosya test et.
- Alakasız kapsam koşullarını yanlışlıkla aynı kural kümesine koyma.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/small_marker.txt
~~~

~~~bash
yara rules.yar samples/large_marker.txt
~~~


## Görevler
1. Hangi örneğin eşleşeceğini tahmin et.
2. Kural kümesini iki örnekte çalıştırıp sonucu not et.
3. `global` anahtar kelimesini kaldır ve neyin değiştiğini anlat.
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
