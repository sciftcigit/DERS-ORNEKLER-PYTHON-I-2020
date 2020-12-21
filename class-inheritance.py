# Ogrenci isminde bir class oluşturuyoruz 
# parent (dede/ata class)
class Kisi :
    isim =""
    soyisim =""
    def __init__(self, ad, soyad) :
        self.isim    = ad 
        self.soyisim = soyad 

    def selamla(self) : 
        print(self.isim)
        print(self.soyisim)
        print("Hoş geldiniz!")

# child (torun class)
class Ogrenci(Kisi):
    ogrNo=0
    def yazOgrNo(self):
        print("Öğrenci Numarası :" + str(self.ogrNo))


# parent class kullanımı 
kull1 = Kisi("Barış","Manço")
kull1.selamla()


# child class kullanımı 
ogr1 = Ogrenci("Aşık","Veysel")
ogr1.selamla()
ogr1.ogrNo=123123
ogr1.yazOgrNo()
        