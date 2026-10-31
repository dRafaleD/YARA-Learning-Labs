# Lab 37 — Hex Alternatifleri ve Joker Karakterler

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Hex Alternatifleri ve Joker Karakterler** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `( 41 | 42 )` o konumda listelenen bayt değerlerinden birini eşleştirir.
2. `??` herhangi bir tek baytı eşleştirir; derlemeler arasında değişen bir değere tolerans sağlar.
3. Her joker kuralı genişletir; ayırt edici kalması için sabit baytları yeterince uzun tut.

## Kavramsal ayrımlar
- Tek değişken baytı kapsayan joker iyidir; desenin çoğunu kapsayan değildir.
- Alternatifler motorun kontrol etmesi gereken desen sayısını çoğaltır.
- Eşleşen bir örnek, ucuz kaçan bir örnek ve ilgisiz bir dosya test et.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/match_a.bin
~~~

~~~bash
yara rules.yar samples/match_b.bin
~~~

~~~bash
yara rules.yar samples/near_miss.bin
~~~


## Görevler
1. Hangi örneklerin eşleşeceğini tahmin et.
2. Kuralı her örnekte çalıştırıp sonucu not et.
3. Üçüncü bir alternatife izin ver ve bunu kanıtlayan bir örnek ekle.
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
