# dört işlem yapan kodu yazalım

sayi1 = input("Sayı 1 : ")
sayi2 = input("Sayı 2 : ")
islem = input(" Yapılacak işlemi giriniz (+ - / *) : ")

if (islem == "+"):
    sonuc = int(sayi1) + int(sayi2)
elif (islem =="-") :
    sonuc = int(sayi1) - int(sayi2)
elif (islem =="*") :
    sonuc = int(sayi1) * int(sayi2)
elif (islem =="/") :
    sonuc = int(sayi1) / int(sayi2)

print(" sonuc : " + str(sonuc))