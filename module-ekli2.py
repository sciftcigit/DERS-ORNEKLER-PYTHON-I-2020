# module.py 
import mdl_hesaplama as mh

print("Eklenen module: " + mh.module_ad)
print("Eklenen module sürümü: " + mh.module_surum)


islem = input("islem giriniz  (toplama için +, cikarma için -)....: ")
sayi1 = input("sayı 1 giriniz ....: ")
sayi2 = input("sayı 2 giriniz ....: ")

if (islem == "+" ) : 

    mh.toplam(float(sayi1),float(sayi2))
else :
    mh.cikar(float(sayi1),float(sayi2))