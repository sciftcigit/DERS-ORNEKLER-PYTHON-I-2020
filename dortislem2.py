# dört işlem yapan kodu yazalım

sayi1 = input("Sayı 1 : ")
sayi2 = input("Sayı 2 : ")
islem = input(" Yapılacak işlemi giriniz (+ - / *) : ")
sonuc = None         # python da null yerine none kullanılıyormuş.

if (sayi1  != "" and sayi2 != "") :

    if (islem == "+"):
        sonuc = float(sayi1) + float(sayi2)
    elif (islem =="-") :
        sonuc = float(sayi1) - float(sayi2)
    elif (islem =="*") :
        sonuc = float(sayi1) * float(sayi2)
    elif (islem =="/") :
        sonuc = float(sayi1) / float(sayi2)
    else :
        print("Hata : Geçerli bir işlem girmediniz!")

    if (sonuc != None) :
        print(" sonuc : " + str(sonuc))

else :
    print("Hata : Sayı 1 ve/veya sayı 2 değeri girilmediği için hesaplama yapılamadı!")