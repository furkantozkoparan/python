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
