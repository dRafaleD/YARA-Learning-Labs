# Lab 35 — xor Değiştiricisi ve Tek Baytla Kodlanmış Stringler

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **xor Değiştiricisi ve Tek Baytla Kodlanmış Stringler** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `$s = "text" xor`, 0 ile 255 arasındaki herhangi bir tek baytlık XOR anahtarıyla kodlanmış string'i eşleştirir.
2. `xor(0x01-0xff)` sıfır anahtarını dışarıda bırakır; aksi halde düz metin de eşleşir.
3. Kısa string'ler 256 anahtar boyunca çok sayıda tesadüfi eşleşme üretir; string'leri uzun ve ayırt edici tut.

## Kavramsal ayrımlar
- xor yalnızca tek baytlık anahtarları işler; çok baytlı anahtarlar, rolling XOR ve diğer kodlamalar farklı yaklaşım ister.
- Eşleşme kodlanmış string'in var olduğunu gösterir, programın onunla ne yaptığını değil.
- Kuralın sınırlarını bilmek için düz, kodlanmış ve ilgisiz örneklerle test et.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/plain.txt
~~~

~~~bash
yara rules.yar samples/xor_0x41.bin
~~~

~~~bash
yara rules.yar samples/unrelated.txt
~~~


## Görevler
1. Kuralın üç örnekten hangisiyle eşleşeceğini tahmin et.
2. Kuralı her örneğe karşı çalıştırıp sonucu not et.
3. Değiştiriciyi `xor(0x01-0xff)` yap ve hangi örneğin eşleşmeyi bıraktığını anlat.
4. İki baytlık anahtarla kodlanmış bir örnek ekle ve kuralın neden kaçırdığını açıkla.
5. Çok kısa bir xor string'i için yanlış pozitif riskini anlat.
6. Bağımsız bir kontrol öner (entropi veya çözülmüş içerik taraması gibi).

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
