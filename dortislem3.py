# dört işlem yapan kodu yazalım
while (True) :
    islem = input(" Yapılacak işlemi giriniz (+ - / * yada çıkış için 'ç' ) : ")
    if (islem == "ç"):
        print("Program sonlandırılıyor.")
        break   
    
    sayi1 = input("Sayı 1 : ")
    sayi2 = input("Sayı 2 : ")   
    sonuc = None         # python da null yerine none kullanılıyormuş.

    if (sayi1.isnumeric() == False or sayi2.isnumeric()  == False ) :
        print("Hesap yapılabilmesi için sayısal değerler girmelisiniz!")
        continue

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

        # herşey yolunda ve sonuç hesaplandı ise ekrana yazıyoruz
        if (sonuc != None) :
            print(" sonuc : " + str(sonuc))
