# module.py 
import mdl_hesaplama

print("Eklenen module: " + mdl_hesaplama.module_ad)
print("Eklenen module sürümü: " + mdl_hesaplama.module_surum)


islem = input("islem giriniz  (toplama için +, cikarma için -)....: ")
sayi1 = input("sayı 1 giriniz ....: ")
sayi2 = input("sayı 2 giriniz ....: ")

if (islem == "+" ) : 

    mdl_hesaplama.toplam(float(sayi1),float(sayi2))
else :
    mdl_hesaplama.cikar(float(sayi1),float(sayi2))