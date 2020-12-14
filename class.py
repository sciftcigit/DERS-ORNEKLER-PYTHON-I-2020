# Ogrenci isminde bir class oluşturuyoruz 
class Ogrenci : 
    ogrNo = 0
    

# Ogrenci class'ından bir Object yaratıyoruz. bu object'in ismi "ogr1"
ogr1 = Ogrenci()
print(ogr1.ogrNo)

# Ogrenci class'ından başka bir Object yaratıyoruz. bu object'in ismi "ogr2"
ogr2 = Ogrenci()
print(ogr2.ogrNo)

# ogr2 nin ogreNo değerini değiştiriyorum 
ogr2.ogrNo = 12345
print(ogr2.ogrNo)

print(ogr1.ogrNo)

