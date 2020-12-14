"""
 girilen sayının faktöriyelini alan program yazınız 
  5 in faktöriyeli  
  5! = 5 * 4 * 3 * 2 * 1 
"""

sayi = 24
sonuc = 1

for x in range(1, sayi+1 ) :
    sonuc = sonuc * x

print(sonuc)