# İnteger: Tam sayilari ifade eder. 
# Floats: Kesirli sayilari idade eder.
# Boolean: Bir seyin doğru ya da yanlis oldugunu ifade eder.(True-False)
r = 2 < 3
print(r)

# Type: Veri tiplerini verir.
r = type(2)
print(r)

# Type Casting: Objelerin veri tiplerinin donusturulmesi. (2.8 Değerine sahip olan Float haldeki verinin tipini integera dönüştürmek için kullanıldı. Yazılan ifade sonuc olarak 2 verir)
r = float(2)                                 
print(r)

# \n ifadesi kullanılmasi durumunda alt satira gecis yapilir.(Ornegin: ''Hey \nnasılsın ifadesi bize bölünerek verilir)
r = 'hey\nnasılsın'
print(r)                
# Bu ifade bize sonuc olarak   ' hey
#                                nasılsın '    olarak döner.

# \t ifadesi ile 4 tane boşluk birakma islemi yapilir. (Ornegin: 'Hey\tnasılsın')
r = 'hey\tnasılsın'
print(r)               
# (Bu ifade bize sonuc olarak 'Hey    nasılsın' olarak donmektedir)

# String ifade içerisinde + kullanilmasi birleştirmeye yaramaktadir. 
r = 'Furkan'
s = 'Tozkoparan'
print(r + ' ' + s) 
# Bu ifade bize sonuc olarak r ve s yi birleştirir ve arada eklediğimiz boşluk ile boşluk ekler. Sonuc olarak 'Furkan Tozkoparan' döner.

# String ifade içerisinde * kullanilmasi ard arda yazmaya yaramaktadir. 
r = 'Furkan'*2
print(r) 
# Bu ifade bize sonuc olarak r değerini arka arkaya iki kere yazmaya yarar. Sonuc olarak 'FurkanFurkan' döner.

# İndexing: elemanlara erismeye yarar. Ornegin: Furkan ismine sahip bir veri icerisinden herhangi bir karakter seçilebilir.
r = 'Furkan'
print(r[1])
# Bize r degeri icerisindeki Furkan yazisinin 1. karakteri alinir. Bu da bize sonuc olarak 'u' verir.

# Slicing: dilimlemeye yarar. Ornegin: Furkan degeri iceren bir seyden sadece kan olan kismi alabiliriz.
r = 'Furkan'
print(r[3:6])
# Bize r degeri icerisindeki Furkan yazisinin 3. karakterinden 6. karakterine kadar olan kismi yani 'Kan' verir.

# Degerleri kesme islemi yaparken atlama da yapilabilir. Ornegin: Tozkoparan degerine sahip bir veriyi sinir ve atlama belirterek kesebiliriz.
r = 'Tozkoparan'
print(r[0: :2])
# Bu ifade bize 0'dan sona kadar olan veriyi almamiza yarar fakat sona ekledigimiz :2 ifadesi her karakterden sonra 2 tane atlamamizi saglar. Sonuc olarak 'Tzoaa' verir.

# Input: Kullanilacak degeri isteyebilmemize yarayan metoddur. Atm ornegi buna uyarlanabilir. Ornegin: input olarak bir veri girin diyip deger istenilebilir.
name = input("Adınızı giriniz: ")
print("Merhaba, " + name)
# Bu ifade ile birlikte kullanicidan isim bilgisi istenildi ve yazdırma isleminde kullanildi. Sonuc olarak adinizi yazin kutusunda Furkan seçersek 'Merhaba, Furkan' olarak verir.

# '==':esittir testi, '!=': esit degildir testi, buyuktur vs testleri de vardır. Bu test ifadeleri bize True ya da False sonuc vermektedir.
r= 5 == 4
print(r)
# Bu ifade r degerinde bulunan esitlik icerisinde testi yapar ve bize geri doner. Sonuc olarak 5, 4'e eşit olmadigi icin 'False' olarak doner.

# if: Eğer ifadesidir ve yalnizca True olan sonuclarda calisir. Ornegin: Bir sayının 2 ile bölümü 0'a eşit mi sağlamasını yapıp eğer eşit ise print et yapılabilir.
r = int(input('Sayı Giriniz:'))
if r % 2 == 0:
    print('Sayınız Çift')
print('Program Sonlandı')
#Sayi giriniz seçeneginde sayi 4 verildi 2 ile bolumunden kalan 0'a esit oldugu icin True sonuc aldik ve sonuc olarak True dondugu icin 'Sayiniz cift' sonrasinda ise 'program sonlandi' döner.

# else: if sorgusu bize True olarak donmezse bu secenek yazilabilir. Ornegin: eğer bir sayinin 2 ile bolumunden kalan 0 ise 'sayiniz cift' yazsin fakat degil ise 'sayiniz tek' yazsin.
r = int(input('Sayı Giriniz:'))
if r % 2 == 0:
    print('Sayınız Çift')
else:
    print('Sayınız Tek')
print('Program Sonlandı')
# Yapilan sorguda sayi 5 olarak girildi ve 2 ile bolumunden kalan 0 olmadigi icin else kisminda yazan alindi. Sonuc olarak 'Sayiniz tek' ve sonrasinde 'Program sonlandi' döner.

# elif: if sorgusuna ektra olarak bir sorgu daha yazmamiza yarar. 
r = int(input("Bir sayı girin: "))
if r < 10:
    print("Sayı 10'dan küçük")
elif r == 10:
    print("Sayı 10'a eşit")
else:
    print("Sayı 10'dan büyük")
print("Programınız sona ulaştı")

# if-else ile belirli bir durum test edilip alt sorgudaki sonucu bu teste gore belirleyebiliriz. Ornegin: Cevabi x: evet y:hayır olan bir soru sordugumuzda alinan cevaba gore sonuc yazdirilabilir.
cevap = input("x in değeri 2 olsun mu? y/n")
if cevap == "y":
    x = 2
else:
    x = 0
print(x)
# Yapilan sorguda x'in degerinin iki olmasini isteme durumuna gore deger atayacaktir. yes seçersek bize sonuc olarak 2 yazdirir n seçersek bize sonuc olarak 0 yazdirir.
