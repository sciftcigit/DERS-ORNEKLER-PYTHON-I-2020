
isimler = ["Serdar","Ayşe","Şeyhmus","Fatma","ALi", "Şeyhmus"]
print(isimler)

isimler.remove("Şeyhmus")
print(isimler)


for deger in isimler :
    print(deger)

uzunluk = len(isimler)
for i in range(uzunluk):
  print(str(i) + isimler[i])