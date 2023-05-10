While
# if-else mantigi ile aynidir fakat burada bir dongu olusturulur. True sonuc alana kadar ve aldiktan sonra da devam eder.
  x = int(input("Bir sayi giriniz: "))
  while x < 0:
      print("Sayiniz negatif. Pozitif bir sayi giriniz: ")
      x = int(input("Bir sayi giriniz: "))
  print("İslem Tamamlandı")
  # Bu sorgu icerisinde sayiyi -5 verirsek bize 'Sayiniz negatif. Pozitif bir sayi giriniz' olarak doner ve sayi girme sayfasi yeniden acilir. 

# Bu dongu ile birlikte bir sayida denklem seklinde birden fazla sayi yazdirilabilir.
  x = -10
  while x < 3:
      print(x)
      x = x + 1
  # Bu ifade ile x degeri 3'den kucuk ise bir arttirip tekrar deniyor ve false olana kadar bu islem yapiliyor. Sonuc olarak bize -10'dan 2'ye kadar olan sayilari verir.
  
# Dongu icerisinde toplama yapilabilir. Ornegin: 100'den kucuk olan sayilarin toplanmasi gibi.
  toplam = 0
  x = 0
  while x <= 100:
      toplam += x
      x += 1
      print(toplam)
  # Bu ifade ile x degeri 100'den kucuk olan sayilar toplanacaktır.
