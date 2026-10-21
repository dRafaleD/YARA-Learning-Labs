# Lab 27 — Hex Patternleri, Sınırlı Atlama ve Negatif Test

[English](notes.md) | [Türkçe](notes.tr.md)

## Amaç
Hex Patternleri, Sınırlı Atlama ve Negatif Test konusunda yerel, zararsız ve tekrarlanabilir bir lab. Her sonuçta gözlem, çıkarım ve belirsizlikleri ayrı kaydedin.

## Temel kavramlar
- Önce mevcut durumu ve beklenen davranışı belirle.
- Girdi doğrulamasını ve güven sınırını belirle.
- Yalnızca bir değişkeni değiştirip sonucu karşılaştır.
- Negatif test, yanlış pozitif ve yanlış negatifleri değerlendir.
- Sürüm, komut, sonuç ve sınırlamaları yaz.

## Yerel uygulama
```bash
python3 fixtures.py
```

```bash
yara bounded.yar samples/match.bin
```

```bash
yara bounded.yar samples/no_match.bin
```

## Alıştırmalar
1. Koddan beklenen sonucu tahmin et.
2. Komutları çalıştırıp çıktıyı kaydet.
3. Zararsız bir girdiyi değiştir.
4. Pozitif ve negatif test karşılaştırması yap.
5. Bağımsız doğrulama yöntemi öner.
6. Çıkarımlar ve belirsizlikler hakkında kısa rapor yaz.

## Mini görev
Bir güvenlik özelliği için otomatik regresyon testi yaz ve hangi hatayı yakaladığını açıkla.

## Kontrol soruları
1. Bu labda güven sınırı nerede?
2. Hangi bulgu gözlem, hangisi varsayım?
3. Negatif test neden önemli?
4. Çevre veya sürüm değişikliği sonuçları nasıl etkiler?
5. Gerçek hayatta hangi ek önlemler gerekir?

## Etik
Yalnızca kendine ait veya açık izinli sistemlerde çalış.
