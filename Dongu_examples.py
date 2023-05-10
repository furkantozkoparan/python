#2 sayısının çarpım tablosunu yazdırmak için bir for döngüsü yazın.
sayi = 2
for i in range(1, 10):
    print(sayi, "x", i, "=", i*sayi)

#Examples kelimesi içerisindeki tüm harfleri yazdırmak için bir for döngüsü yazın.
f = "Examples"
for i in f:
    print(i)
    
#Examples kelimesini tersten yazın, tersten yazılan bu kelimenin harflerini yazdırın ve harf yazdırma işlemini 'a' harfinde durduracak şekilde bir döngü yazın.
g = "Examples"
a = (g[::-1])
for i in a:
    if i == 'a':
        break
    print(i)
    
#'12, 13, 14, 15, 16, 17' sayılarını içeren bir listedeki çift sayıları yazdırmak için bir for döngüsü yazın.
x = [12, 13, 14, 15, 16, 17]
ciftler = []
for i in x:
    if i % 2 == 0:
        ciftler.append(i)
print(ciftler)
