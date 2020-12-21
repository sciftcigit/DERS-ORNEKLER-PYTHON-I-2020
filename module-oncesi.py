# module.py 

def toplam(s1,s2) : 
    print(s1+s2)

def cikar(s1,s2) : 
    print(s1-s2)

islem = input("islem giriniz  (toplama için +, cikarma için -)....: ")
sayi1 = input("sayı 1 giriniz ....: ")
sayi2 = input("sayı 2 giriniz ....: ")

if (islem == "+" ) : 

    toplam(float(sayi1),float(sayi2))
else :
    cikar(float(sayi1),float(sayi2))