# Lab 29 — String Sayıları, Offset ve Bağlamsal YARA Kuralları

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **String Sayıları, Offset ve Bağlamsal YARA Kuralları** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. #marker measures match occurrences, not semantic intent.
2. @marker[2] refers to the offset of the second occurrence.
3. Use synthetic near-miss files to measure false positives.

## Kavramsal ayrımlar
- Bir verinin bulunması, o veriye dayanarak kurulan bütün iddiaları doğrulamaz.
- Önce güven sınırını ve hangi girdiye kimin hükmettiğini belirle.
- Pozitif ve negatif kontrolleri birlikte çalıştır; bir ölçümün sınırlarını kaydet.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/positive.txt
~~~

~~~bash
yara rules.yar samples/negative.txt
~~~

## Görevler
1. Kodu inceleyerek beklediğin çıktıyı tahmin et.
2. Çalıştırıp girdileri ve gerçek çıktıları not et.
3. Zararsız bir girdiyi değiştir; farkı ve sebebini açıkla.
4. İlk güvenlik özelliği için assertion ekle.
5. Bir negatif senaryo ve bir yanlış pozitif ihtimali yaz.
6. İkinci bir bağımsız doğrulama yöntemi öner.

## Kısa sınav
1. Bu örnekte giriş verisi nereden geliyor?
2. Hangi davranış doğrudan gözlendi?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
