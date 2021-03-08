try :
    dosya = open("C:\Windows\deneme1.txt", "x", encoding="utf-8")
except FileExistsError :
    print("Bu isimde dosya olduğu için oluşturulamıyor!")
except PermissionError:
    print("Dosya yazma yetkisi olmadığı için hata verdi !")
