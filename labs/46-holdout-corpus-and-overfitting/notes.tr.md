# Lab 46 — Ayrı Test Kümesi (Holdout) ve YARA'da Aşırı Uyum

[English](notes.md) · [Türkçe](notes.tr.md) · [Kurallar](rules.yar) · [Değerlendirme](evaluate.py)

## Sorun: eğitimde %100 başarı her şeyi kanıtlamaz
45. lab'de iki kural sürümünü aynı örnekler üzerinde ölçmüştük. Bu kez veri kümesini **kuralı geliştirirken kullanılan eğitim örnekleri** ve **ilk kez testte görülecek holdout örnekleri** olarak ayırıyoruz. Eğitim sonuçlarına çok iyi uyan bir kural, yeni örneklerde başarısız olabilir. Buna **overfitting / aşırı uyum** denir.

Gerçek malware yerine uydurma belge etiketleri kullanacağız. Geniş kural `TEST-CANARY` metnini görünce eşleşir. Dar kural bunun yanında `ACTION-CHECK` arar. Dar kural eğitimdeki iki pozitif belgeyi doğru bulur, negatifleri eler. Fakat holdout'taki `ACTION-REVIEW` kullanan **gerçek pozitif etiketli** örneği kaçırır.

## Metrikler
- **TP (doğru pozitif):** Pozitif örnek ve eşleşme var.
- **FP (yanlış pozitif):** Negatif örnek ama eşleşme var.
- **TN (doğru negatif):** Negatif örnek ve eşleşme yok.
- **FN (yanlış negatif):** Pozitif örnek ama eşleşme yok.

**Kesinlik (precision)** = TP / (TP + FP), **duyarlılık (recall)** = TP / (TP + FN). Payda sıfırsa sonuç **tanımsızdır**, otomatik sıfır değildir. Buradaki etiketler sadece eğitim senaryosunun doğrularıdır; zararlılık tespiti anlamına gelmez.

## Uygulama
YARA komut satırı aracını ayrıca kur. Python tarafında dış paket gerekmez:
```bash
yara --version
python3 evaluate.py
```
Kod geçici klasörde zararsız metinleri üretir. Her iki kuralı eğitim ve holdout üzerinde çalıştırır; karışıklık matrisi ile kesinlik/duyarlılık değerlerini yazar. Dar kuralın eğitimde hatasız, holdout'ta ise bir FN ürettiğini doğrular.

## Görevler
1. Neden eğitimde çok başarılı olan bir kural pratikte zayıf kalabilir?
2. Holdout pozitiflerinden birinde hangi ikinci etiket eksik?
3. İki etiketi de alıntılayan zararsız bir dokümanı holdout negatifine ekle. Yanlış pozitif ne olur?
4. Kuralları geliştirirken holdout etiketlerini sonuca göre değiştirmek neden hatalı?
5. Veri sızıntısını önlemek için aynı dosyanın kopyalarını hangi kümeye koymalısın?
6. Dört örneklik bir test kümesiyle gerçek dünya performansı iddia edilebilir mi?

## Kapsam
Bu küçük veri kümesi aşırı uyumu göstermek için kasıtlı olarak hazırlanmıştır. Gerçek tespit kurallarında bağımsız etiketler, temsil gücü yüksek veri ve kapsamlı doğrulama gerekir. YARA eşleşmesi tek başına zararlı yazılım kanıtı değildir.
