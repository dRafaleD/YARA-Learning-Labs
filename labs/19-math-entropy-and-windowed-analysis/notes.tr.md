# Lab 19 — YARA Math Modülü: Entropy, Byte Window ve Tespit Güvenilirliği

[English](notes.md) · [Türkçe](notes.tr.md)

## Hedef

Lab 18'deki false positive ve rule testi bilgisini üç bağlantılı konuyla ilerletiyoruz: **byte dağılımı ve entropy hesabı**, belirli **offset/window** içindeki koşullar ve **tekrar üretilebilir test matrisi**. Örneklerin tamamı zararsız sentetik binary dosyalardır.

**En önemli uyarı:** Yüksek entropy malware kanıtı değildir. Sıkıştırılmış arşiv, şifreli veri, resim, rastgele veri ve tamamen güvenli dosyalar da yüksek entropy gösterebilir.

## 1. Entropy nedir?

Shannon entropy, gözlenen değer dağılımının belirsizliğini ölçer. Bir byte 256 farklı değer alabilir; bu yüzden byte entropy teorik olarak **0–8 bit/byte** aralığındadır.

```text
H = - Σ p(byte) × log₂(p(byte))
```

- Tamamı `A` byte'ından oluşan bölgenin entropy değeri yaklaşık **0** olur.
- 0–255 değerleri dengeli dağılmış büyük örneklerin entropy değeri **8'e yaklaşır**.
- Kısa bölgelerde ölçüm daha oynaktır; örneklem boyutu sonucu etkiler.

Bu hesap **niyeti ölçmez**. “Yüksek değer = encrypted/malware” sonucunu çıkaramazsın.

## 2. Neden dosyanın tamamı yerine byte window?

Aynı dosyada okunabilir stringler, sıfırlarla dolu padding, normal code ve yüksek entropy içeren kaynaklar bulunabilir. Tüm dosyanın tek entropy değeri bu farklılıkları gizleyebilir.

```text
offset 0            256                 4352               8448
| header + padding  | ilk 4096 byte      | ikinci 4096 byte |
```

Üç fixture da `LAB19_DEMO` marker'ı ile başlar. İlk pencere 256. byte'tan başlar; 4096 byte boyunca ölçülür. Mixed fixture ikinci bir 4096-byte pencere daha taşır.

Bu labın kilit becerisi: “Hangi aralıktaki byte'ların istatistiğini inceliyorum?” sorusunu cevaplamak.

## 3. math modülü

YARA ile istatistiksel kontroller yapmak için:

```yara
import "math"
```

kullanıyoruz. Örnek:

```yara
math.entropy(256, 4096)
```

Burada `256` başlangıç **offset**'idir. `4096` ise bakılacak **byte sayısı**dır. Yüzde değildir; dosyanın sonundan sayılmaz.

Ölçüme başlamadan dosya yeterince büyük mü diye `filesize` kontrolü yapılmalı.

## 4. Tek başına threshold kullanma

High entropy rule şu şartları birleştirir:

1. offset 0'da sentetik eğitim marker'ı;
2. 4352 byte – 20 KiB aralığında dosya boyutu;
3. offset 256'daki 4096 byte için entropy **7.5'ten yüksek**.

Marker, rastgele dosyaların eğitim kuralıyla yanlış eşleşmesini azaltır; belirli window ise karşılaştırmayı anlaşılır yapar. **7.5 sadece eğitim eşiğidir**, gerçek dünyada doğrulanmış malware threshold'u değildir.

Low entropy kuralı `< 1.0` koşulunu kullanır. Üçüncü kural mixed dosyanın ikinci bölgesini kontrol eder.

## 5. Zararsız test dosyalarını üret

Lab klasöründe:

```bash
python3 generate_samples.py
```

Python standard library dışında bağımlılık yok. Şu dosyaları üretir:

```text
samples/low-entropy.bin
samples/high-entropy.bin
samples/mixed-entropy.bin
```

High entropy bölgesi deterministic SHA-256 bloklarıyla oluşturulur. Gizli anahtar veya şifreleme yoktur.

Beklenen genel değerler:

| Dosya | Boyut | İlk window (256) | İkinci window (4352) |
| --- | ---: | --- | --- |
| low-entropy.bin | 4352 | ~0 | yok |
| high-entropy.bin | 4352 | ~7.9 | yok |
| mixed-entropy.bin | 8448 | ~0 | ~7.9 |

Kesin sayıları generator'ın çıktısından al; tablodaki yaklaşık değerleri veri diye ezberleme.

## 6. YARA ile tara

`math` modülünü destekleyen YARA CLI gerekir:

```bash
yara --version
yara test_rules.yar samples/low-entropy.bin
yara test_rules.yar samples/high-entropy.bin
yara test_rules.yar samples/mixed-entropy.bin
```

Eşleşen stringleri görmek için:

```bash
yara -s test_rules.yar samples/high-entropy.bin
```

`-s` marker gibi **string eşleşmelerini** gösterir. Entropy değerini eşleşen string gibi yazdırmaz. Sayısal değeri Python generator'ın çıktısıyla karşılaştır.

## 7. Test matrisi

| Dosya | İlk window high | İlk window low | İkinci window high |
| --- | --- | --- | --- |
| low-entropy.bin | Hayır | Evet | Hayır |
| high-entropy.bin | Evet | Hayır | Hayır |
| mixed-entropy.bin | Hayır | Evet | Evet |

Bu tablo yalnızca **kendi sentetik dosyalarımız için beklenen** sonuçtur; bilinmeyen dosyalara yönelik malware iddiası değildir.

## 8. Otomatik test

```bash
python3 run_tests.py
```

Script örnekleri yeniden üretir, bilgisayarda yüklü `yara` CLI'yı çağırır ve bulunan rule isimlerini beklenen setlerle birebir karşılaştırır. YARA kurulu değilse açıklayıcı hata verir.

Tespit raporu tutarken şunları kaydet:

- YARA sürümü,
- rule commit'i,
- sample hash'i,
- komut ve tarih,
- beklenen / görülen sonuç.

## 9. False positive / false negative

### False positive
Benign sıkıştırılmış veri entropy açısından yüksek olabilir. Sadece yüksek entropy'ye dayanan kural gereksiz uyarı üretebilir.

### False negative
Gerçek ilgili data beklediğin offset'te değilse fixed-window kuralı kaçırır. Fazla yüksek threshold da farklı örnekleri eler.

### Küçük örneklem
16 byte'lık entropy ile 4096 byte'lık entropy'yi eşit güvenilirlikte görme. Çok kısa aralıklar yüksek 8 bit sınırına ulaşamayabilir bile.

### Full-file / region farkı
Low-entropy padding, dosya genelindeki yüksek-entropy alanını ortalamada gizleyebilir. Tersi de geçerli: bütün dosyanın yüksek olması tek başına packing kanıtı değildir.

### Performance
Kuralı hızlandırmak için pencereyi aşırı daraltırsan coverage kaybedebilirsin. Optimize ederken doğruluk testini tekrarla.

## 10. Reverse Engineering ile bağlantı

Önce Ghidra'da bölüm, kaynak veya anlamlı byte aralığını belirle. Sonra entropy'yi incele. Yüksek sonuç için alternatif açıklamaları düşün: archive, compression, encryption, embedded asset veya rastgele normal veri. Sonuca varırken format, import, string, çalışma zamanı davranışı ve bağlamla birlikte değerlendir.

## Mini challenge'lar

1. **Kaydırılmış veri:** Mixed dosyadaki high-entropy bloğunu 512 byte ileri taşı. Hangi offset değişmeli? Eski kural neden kaçırdı?
2. **Threshold:** 7.5 yerine 7.99 kullan. Eşleşme nasıl değişti? Tek threshold'a güvenmek neden kırılgan?
3. **Pencere boyutu:** 32, 256 ve 4096 byte için entropy ölç. Örneklem büyüklüğünün etkisini yaz.
4. **Benign karşı örnek:** Python `zlib` ile sıradan metin sıkıştırıp entropy hesapla. Neden yüksek entropy “zararlı” etiketi değildir?

## Alıştırmalar

1. Üç fixture üret ve boyutlarını yaz.
2. 256-byte prefix'i incele.
3. Üç rule'daki sınır kontrollerini belirle.
4. Her rule'ı her fixture'a uygula.
5. Test matrisini doğrula.
6. `yara -s` çıktısını yorumla.
7. Otomatik testi çalıştır.
8. Çalışma kopyasında window boyutunu değiştir.
9. Sadece 512 byte içeren marker'lı near-miss dosya oluştur.
10. `filesize` koşulunun onu elediğini gör.
11. Python'da whole-file ile first-window entropy karşılaştır.
12. Bilinen kısıtları ve rule versiyonunu rapora yaz.

## Tekrar soruları

1. Shannon entropy neyi ölçer?
2. 0 ve 8'e yakın değerler ne ifade eder?
3. Yüksek entropy malware kanıtı mı?
4. `math.entropy(offset,size)` hangi bölgeyi ölçer?
5. `filesize` sınırı neden gerekli?
6. Marker ile entropy neden birleştiriliyor?
7. Whole-file entropy neden yanıltabilir?
8. Fixed offset neden false negative oluşturabilir?
9. Kısa window neden daha oynak?
10. YARA `-s` ne gösterir?
11. Reproducible test corpus nasıl oluşturulur?
12. Entropy sonucunu Ghidra / dynamic RE ile nasıl ilişkilendirirsin?

## Ana çıkarım

**Entropy destekleyici istatistiksel göstergedir.** Yararlı rule için bağlamsal indicator, doğru byte sınırı, test edilmiş threshold ve benign örneklerle karşılaştırma gerekir.
