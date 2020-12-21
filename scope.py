def selamla(isim) : 
    ad = isim 
    print(ad + " hoşgeldiniz.")
    


selamla("Ayşe")


# scope dışında olan değişkene erişmeye çalışıyoruz.
print(ad)   # NameError: name 'ad' is not defined hatası verir. 