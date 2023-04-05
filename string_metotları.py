# Upper: Tüm karakterleri büyük harf yapar.
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.upper()
print(result)

# lower: Tüm karakterleri küçük harf yapar.
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.lower()
print(result)

# title: Tüm karakterlerin ilk harfini büyük diğerlerini küçük harf yapar.
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.title()
print(result)

# Split: İfade içerisinde yer alan boşluk karakterlerinden bölünür ve bir karakter dizisi olarak gelir.
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.split()
print(result)

# Split: Split içerisindeki paranteze girilen ifadeye göre bölünme işlemi gerçekleşebilir. (Örneğin: result = split('.') olsaydı ifade noktalara göre bölme yapacaktı)
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.split('.')
print(result)

# Split: Eger print içerisinde result[0] yazilsaydi bize ifade içerisindeki söz dizimlerinden birincisini yazdiracakti. (Örneğin: print(result[0]) olsaydı 
# ifade söz dizimindeki birinci ifade olan hello ifadesini verecekti)
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.split()
print(result[0])

# Join: Birleştirme işlemi için join komutu kullanılmaktadır. Boşluklarla ayrılmış olan karakter dizilerini birleştirmeye yarar. Birleştirme yaparken söz 
# dizimleri arasına bir ifade eklemek istiyorsak tırnak içerisine join komutundan önce yazılır. 
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.split()
result = '*'.join(result)
print(result)

# find: İfade icerisinde kelime ya da baska karakterleri aramaya yarar. Arama yaparken bize kacinci karakterden sonra istedigimiz kelime bulundugunu verir.
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.find('Furkan')
print(result)

# Replace: İfade içerisindeki söz dizimi ya da karakterlerin degistirilmesine yarar. Orneğin: 'Furkan' olan ifadeyi 'Adem' yazarak cevrilebilir.
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.replace('Furkan', 'Adem')
print(result)

# Center: İfadeye karakter sınırlaması eklemeye yarar. Fakat 50 karakter olarak belirlenen bir sütunda yazı 20 karakter ise kalan kısımlara 
# boşluk ekleyerek tamamlar ve yazıyı ortalar.
result = 'Hello there. My name is Furkan Tozkoparan'
result = result.center(100)
print(result)
