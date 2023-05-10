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

For
# while dongusunden farkli olarak for da dongunun yapilmasini istedigimiz sayisi belirtilir. Ornegin:
  toplam = 0
  for x in range(101):
      toplam += x
      print(toplam)
  # Bu ifade ile birlikte 0'dan 100'e kadar olan sayilar toplanacaktir. While da bunu yaparken ne kadar True cikarsa topluyordu.
  
Break 
# Istenilen bir kosul saglandiginda sorguyu durdurmaya yarar. Ornegin: for ile yazilmis bir seyde 10'a kadar yazdirma yapilirken 5'e gelince dur denilebilir.
  for i in range(10):
      if i == 3:
          break
      print(i)
  # Bu sorgu ile 0'dan 9'a kadar sayilar siralanirken sayi eger 3'e esit olursa sorgu sonlanacaktir. Sonuc olarak bu bize 0, 1, 2 verir ve siradaki 3 oldugu icin sorgu sonlanir.
  
Continue
# Bazi dongulerde istenilen degeri atlamaya yarar. Ornegin: bir sorguda 10'a kadar yazdirma yapilirken 5'i atlayip sorguya devam edebiliriz.
for i in range(10):
     if i == 3:
        continue
     print(i)
# Bu sorgu ile 0'dan 9'a kadar sayilar siralanirken sayi eger siralanmaya baslayacak fakat 3'e gelince bunu dahil etmeden sorguya devam edecektir. Sonuc olarak bu bize 0, 1, 2, 4, 5... 9 verir.  
