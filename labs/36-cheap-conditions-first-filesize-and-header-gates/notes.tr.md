# Lab 36 — Ucuz Koşullar Önce: filesize ve Başlık Kapıları

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Ucuz Koşullar Önce: filesize ve Başlık Kapıları** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Çoğu dosya hızla elensin diye `filesize` ve başlık karşılaştırması gibi ucuz kontrolleri string koşullarından önce yaz.
2. `uint16(0) == 0x5A4D` ilk iki baytı okuyup `MZ` başlığını test eder.
3. Bir kapı kuralın kapsamını daraltır; bu yüzden hem kapıdan geçen dosyayı hem de kapısız aynı işaretçiyi test et.

## Kavramsal ayrımlar
- Sıra hızı etkiler, mantıksal ifadenin sonucunu değil.
- Başlık kapısı MZ olmayan dosyalardaki işaretçiyi bilerek gizler.
- Hızlanma iddia etmeden önce gerçek bir korpusta ölç.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/mz_with_marker.bin
~~~

~~~bash
yara rules.yar samples/text_with_marker.txt
~~~

~~~bash
yara rules.yar samples/mz_without_marker.bin
~~~


## Görevler
1. Hangi örneğin eşleşeceğini tahmin et.
2. Kuralı her örnekte çalıştırıp sonucu not et.
3. String kontrolünü başa al ve eşleşmelerin aynı kaldığını doğrula.
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
