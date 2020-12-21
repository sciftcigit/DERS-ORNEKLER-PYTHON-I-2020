# Ogrenci isminde bir class oluşturuyoruz 
class Ogrenci : 
    ogrNo = 0
    yas = ""
    isi = ""

    # obje yaratırken otomatik olarak çalışan def(function)  
    def __init__(self, yasi, ismi):
        self.yas = yasi
        self.isim = ismi
    
    #kendi yazdığımız def(function) . ihtiyaç halinde kullanabiliyoruz.
    def bilgileriListele(self) :
        print("Öğrencinin yaşı :" + str(self.yas))
        print("Öğrencinin Adı :" + self.isim)
        print("Öğrencinin numarası :" + str(self.ogrNo))

ogr1 = Ogrenci(24,"Alp")   

print(ogr1.yas)
print(ogr1.isim)
print(ogr1.ogrNo)

ogr1.bilgileriListele()

ogr2 = Ogrenci("32","Ayşe")
ogr2.bilgileriListele()
    
