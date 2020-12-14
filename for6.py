"""
    - kullanıcının girmiş olduğu sayıya kadar olan 
    - 3 ve üçün katlarını 
    - toplayan  ve sonucu ekranan yazan program
"""

sayi = int(input("sayı giriniz ..... :"))
sonuc = 0

for i in range(3, sayi+1, 3) :
    sonuc += i   
    
print(sonuc)