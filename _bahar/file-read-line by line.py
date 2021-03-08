dosya = open("C:\_DERS_ORNEKLER\PYTHON\_bahar\deneme.txt", "r", encoding="utf-8")

x = 0 
for satir in dosya:
    x += 1
    print(str(x) + ".satır : " + satir)
    
dosya.close()