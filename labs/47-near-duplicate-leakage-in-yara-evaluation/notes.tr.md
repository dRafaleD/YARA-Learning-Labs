# Lab 47 — YARA Değerlendirmesinde Benzer Örnek Sızıntısı

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralı](rules.yar) · [Python değerlendirmesi](evaluate.py)

## 46. lab'den devam
Önceki çalışmada örnekleri **eğitim** ve **ayrı test (holdout)** olarak bölmüştük. Ancak benzer bir dosya iki kümeye birden girerse test artık tam anlamıyla bağımsız olmaz. Örneğin bir belgenin içeriği aynı kalıp sadece adı veya `case=` etiketi değişmişse farklı dosyalar gibi görünebilir. Buna **veri sızıntısı (data leakage)** denir.

## Uygulamadaki iki kontrol
Zararsız örnekleri YARA ile tarıyoruz. Kuralın iki işaretçisi var: `DOC-CANARY` ve `ACTION-CHECK`. Sonrasında:

- **Birebir SHA-256:** Dosya baytları tamamen aynıysa hash aynıdır. Bir harf değişirse SHA-256 genellikle farklılaşır.
- **Normalize edilmiş parmak izi:** Oyuncak örnekte `case=` satırlarını kaldırıp kalan anlamlı içeriği karşılaştırıyoruz. Böylece metni aynı ama etiketleri farklı iki örnek tespit edilir.

**Önemli:** Gerçek dünyada körlemesine normalizasyon yapmak da hatalıdır; güvenlik açısından anlamlı farkları yanlışlıkla silebilir. Bu yüzden normalizasyon yöntemi, gruplama kuralları ve test kümesi önceden tanımlanıp belgelenmelidir.

## Çalıştır
YARA CLI kurulu olmalı:
```bash
yara --version
python3 evaluate.py
```
Program geçici klasöre sentetik metinler oluşturur; eğitim ile holdout için TP/FP/TN/FN sayar. İlk ölçümde benzer bir pozitif test örneği eğitim kümesiyle örtüşür. Ardından örtüşen test kaydı çıkarıldığında sonuçların nasıl değiştiğini gösterir. Reddedilen kayıtlar gizlenmez; hangisinin çıkarıldığı raporlanır.

## Sorular
1. Dosyaları farklı klasörlere ayırmak neden bağımsızlık garantisi sağlamaz?
2. İki belge neredeyse aynıysa SHA-256 neden farklı olabilir?
3. Normalizasyon gerçekte farklı örnekleri aynı sanırsa hangi hata doğar?
4. Aynı aileye ait zararlı örnekleri gruplamadan eğitim/teste bölmek neden yanıltabilir?
5. **Gruplu bölme**, **zamana göre bölme** ve **tekilleştirme** yaklaşımlarını karşılaştır.
6. Sağlam raporda hash, etiket, küme seçimi, sürüm ve test yöntemi nasıl belgelenmeli?

## Güvenlik ve sınırlar
Gerçek zararlı yazılım dosyası veya payload yoktur. Bu küçük veri kümesinden gerçek tespit başarısı iddia edilmez. Tek bir YARA eşleşmesi dosyanın kötü amaçlı olduğunu kanıtlamaz.
