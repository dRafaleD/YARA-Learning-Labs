# Lab 42 — filesize Birimleri ve Boyut Sınırları

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **filesize Birimleri ve Boyut Sınırları** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. YARA, `filesize` karşılaştırmalarında KB ve MB gibi boyut eklerini kabul eder.
2. Boyut aralığı kuralı daraltır ama aralığın dışındaki meşru varyantları kaçırabilir.
3. Aralığın hemen altında, içinde ve üstünde dosyalarla test et.

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
yara rules.yar samples/small.bin
~~~

~~~bash
yara rules.yar samples/target.bin
~~~

~~~bash
yara rules.yar samples/large.bin
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
