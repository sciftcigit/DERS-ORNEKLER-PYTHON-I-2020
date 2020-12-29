import datetime as de


deger = de.datetime.now()
print(deger)

for i in range(10): 
    print(str(i) + " günler ne kadar çabuk geçiyor ")

deger2 = de.datetime.now() 
print(deger2)

fark = deger2.microsecond-deger.microsecond
print( " arada geçen süre farkı :"  + str(fark) + " mikro saniye ")
fark = fark / 1000000
print( " yani arada geçen süre farkı :"  + str(fark) + "  saniye ediyor ")

