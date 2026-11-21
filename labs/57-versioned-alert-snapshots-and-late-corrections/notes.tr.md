# Lab 57 — Sürümlü Alarm Özetleri ve Gecikmiş Düzeltmeler

[English](notes.md) · [Türkçe](notes.tr.md) · [YARA kuralları](rules.yar) · [Değerlendirme](evaluate.py)

## 56. lab'den devam
Önceki gün kapatılmış bir zaman aralığına geç kayıt gelirse **yeniden değerlendirme** yapılmasını öğrendik. Bugün bu düzeltmenin **sürüm numarasını** tutuyoruz.

**Snapshot:** belirli zaman aralığının mevcut alarm özeti. **Revision:** özet değiştikçe artan sürüm. **Finalized bucket:** tamamlandı kabul edilen zaman aralığı. **Correction:** geç gelen yeni kanıtla eski sayının güncellenmesi.

Hayalî veride sensör A'nın `100–120` zaman aralığı ilk kapanışta 1 alarm içeriyor. Sonra gecikmiş yeni bir olay gelince 2 alarma yükseliyor ve özet **revision 2** oluyor. Yinelenen olaylar ve aynı ID altında çelişkili kayıtlar otomatik olarak yeni alarm sayılmıyor.

Örnek sonuç: 9 ham YARA kural eşleşmesi, 5 benzersiz olay, 4 alarm veren olay, 1 geç olay, 1 tekrar ve 1 çelişki.

## Çalıştırma
YARA CLI kurulmuş olmalı:
```bash
python3 labs/57-versioned-alert-snapshots-and-late-corrections/evaluate.py
```

## Sorular
Önceki rapor sürümünü saklamak neden önemli? Geç olayla yinelenen olay arasındaki fark ne? Çelişkili olay ID neden kanıtı silmeden ayrıca raporlanmalı?

## Sınırlar
Gerçek zararlı yazılım veya SIEM yoktur. Kayıtlar ve YARA dizeleri zararsız eğitim verileridir.
