# Lab 43 — fullword Değiştiricisi ve Kelime Sınırları

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **fullword Değiştiricisi ve Kelime Sınırları** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. `fullword`, bir string'in yalnızca çevresinde harf veya rakam karakterleri yokken eşleşmesini sağlar.
2. String'in yalnızca daha uzun bir kelimenin parçası olduğu eşleşmeleri ortadan kaldırır.
3. Alt çizgi ve noktalama yalnızca alfanümerik olmadıklarında sınır sayılır; sınır durumlarını test et.

## Kavramsal ayrımlar
- `fullword` yanlış pozitifleri azaltır ama daha uzun bir token içindeki gerçek eşleşmeyi de gizleyebilir.
- Tek başına bir kelime, daha uzun bir kelime içindeki kelime ve noktalamaya bitişik kelimeyi test et.
- Sınırın bu string için neden önemli olduğunu belgele.

## Lab uygulaması
Önce `rules.yar` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fixtures.py
~~~

~~~bash
yara rules.yar samples/standalone.txt
~~~

~~~bash
yara rules.yar samples/embedded.txt
~~~

~~~bash
yara rules.yar samples/punctuated.txt
~~~


## Görevler
1. Hangi örneklerin eşleşeceğini tahmin et.
2. Kuralı her örnekte çalıştırıp sonucu not et.
3. `fullword` ifadesini kaldır ve hangi örneğin eşleşmeye başladığını anlat.
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
