
import mdl_mysql_func as md
while True : 

    # Menü gösterme 
    print("\n\n")
    print(" ------------------")
    print("  TELEFON REHBERİ VER-1.0")
    print(" ------------------")
    print(" Kayıt Ekle     (1)")
    print(" Kayıt Listele  (2)")
    print(" Kayıt Sil      (3)")
    print(" Kayıt Güncelle (4)")
    print(" ------------------")
    print(" Çıkış          (0)")
    print("\n\n")    
    
    # Kullanıcıdan bir seçim yapmasını istiyoruz z
    secim = input("Yapmak istediğiniz işlemi seçiniz: ")
    
    if (secim == "1") : 
        md.ekle()
    elif (secim == "2"):
        md.list()
    elif (secim == "3"):
        md.list()
        md.sil()
    elif (secim == "4"):
        md.list()
        md.gunc()
    elif (secim == "0"):
        print("Program kapatılıyor.")
        break
    else :
        print("Geçerli bir seçim yapmadınız!")
  

        
    
    
    

