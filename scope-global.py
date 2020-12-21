# en üste tanımladığım değişken global scope alanında 
# böyle olduğu için hem def hemde ana kod bloğu kısmından erişebildik.

surum = "Surum 3.5"   

def selamla(isim) : 
    ad = isim 
    global x   # global kelimesi ile de global bir değişken oluşturabilirsiniz.
    x = 5555
    print(ad + " hoşgeldiniz.")
    print("Sürüm :" + surum)   # surum değişkenine erişiyoruz
    


selamla("Ayşe")
print("Yazılım sürümü :" + surum)  # surum değişkenine erişiyoruz

print(x)

