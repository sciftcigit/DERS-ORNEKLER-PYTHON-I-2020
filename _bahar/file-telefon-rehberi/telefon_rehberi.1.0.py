import mdl_islemler
import os

while True : 

    print("\n\n\n\n")
    print(" ------------------")
    print(" Kayıt Ekle     (1)")
    print(" Kayıt Listele  (2)")
    print(" Kayıt Sil      (3)")
    print(" Kayıt Güncelle (4)")
    print(" ------------------")
    print(" Çıkış          (0)")
    print("\n\n\n\n")    
    
    secim = input("Yapmak istediğiniz işlemi seçiniz: ")
    
    if (secim == "1") : 
        mdl_islemler.kayit_ekle()
    elif (secim == "2"):
        mdl_islemler.kayitlari_listele()
    elif (secim == "3"):
        print("kayıt sil")
    elif (secim == "4"):
        print("kayıt düzenle")
    elif (secim == "0"):
        print("Program kapatılıyor.")
        break
    else :
        print("Geçerli bir seçim yapmadınız!")
        
    input("Devam etmek için enter tuşuna basınız.")
    clear = lambda: os.system('cls')
    clear()
    
        
        
    
    
    

