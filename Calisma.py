# DOSYA İSİMLERİNİ DEĞİŞTİRME KODU..

import os

def alt_klasor_fotograflara_F_ekle(kok_klasor, ana_klasor_adi):
    ana_klasor_yolu = os.path.join(kok_klasor, ana_klasor_adi)

    if not os.path.exists(ana_klasor_yolu):
        print(f"Uyarı: {ana_klasor_adi} adlı ana klasör bulunamadı.")
        return

     Ana klasördeki alt klasörleri al
    alt_klasorler = [f for f in os.listdir(ana_klasor_yolu) if os.path.isdir(os.path.join(ana_klasor_yolu, f))]

    for alt_klasor in alt_klasorler:
        alt_klasor_yolu = os.path.join(ana_klasor_yolu, alt_klasor)

        # Alt klasördeki fotoğrafları al
        fotograflar = [f for f in os.listdir(alt_klasor_yolu) if os.path.isfile(os.path.join(alt_klasor_yolu, f))]

        for fotograf in fotograflar:
            fotograf_yolu = os.path.join(alt_klasor_yolu, fotograf)

            # Yeni ismi oluştur ve fotoğrafı yeniden adlandır
            yeni_isim = fotograf.replace('.', '_F.')
            yeni_isim_yolu = os.path.join(alt_klasor_yolu, yeni_isim)

            os.rename(fotograf_yolu, yeni_isim_yolu)
            print(f"{fotograf} dosyasının adı {yeni_isim} olarak değiştirildi.")

# Kullanım örneği
kok_klasor = r"C:\Users\furkan.tozkoparan\Desktop\Yeni klasör (2)"
ana_klasor_adi = "YAPI FOTOĞRAFLARI"
alt_klasor_fotograflara_F_ekle(kok_klasor, ana_klasor_adi)




#ARCMAP BUL-DEĞİŞTİR..
!YourField!.replace("/", "_")
