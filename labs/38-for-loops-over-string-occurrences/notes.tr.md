# Lab 38 — String Oluşumları Üzerinde for Döngüleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **String Oluşumları Üzerinde for Döngüleri** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `#a`, `$a`'nın oluşum sayısıdır ve `@a[i]`, i'inci oluşumun ofsetidir (1'den başlar).
2. `for any i in (1..#a) : ( @a[i] < 16 )` en az bir oluşumun ilk 16 baytta olup olmadığını sorar.
3. Döngüler, ayrı string'ler olmadan konuma dayalı mantığı tek bir kuralda ifade etmeni sağlar.

## Kavramsal ayrımlar
- `for all`, `for any`'den daha katıdır; niyetine uyanı seç.
- Ofsetler sıfır tabanlıdır ve bayt cinsindendir.
- Başta bir eşleşme, dosyada geç bir eşleşme ve hiç eşleşmeme durumlarını test et.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/early.txt
~~~

~~~bash
yara rules.yar samples/late.txt
~~~

~~~bash
yara rules.yar samples/both.txt
~~~


## Görevler
1. Hangi örneğin eşleşeceğini tahmin et.
2. Kuralı her örnekte çalıştırıp sonucu not et.
3. `any` ifadesini `all` yap ve hangi örneğin eşleşmeyi bıraktığını anlat.
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
