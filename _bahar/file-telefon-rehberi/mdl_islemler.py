

def kayit_ekle():
    # ##
    #  Kullanıcıdan veri isteme 
    # ##
    ad      = input("Ad giriniz :");
    soyad   = input("Soyad giriniz :");
    tel     = input("Telefon giriniz :");

    metin = "Ad: {:<30}  Soyad: {:<30}  Telefon: {:<15}   "
    print(metin.format(ad, soyad, tel))


    # ##
    #  Verileri txt dosyasına saklama 
    # ##

    dosya = open("veri.txt","a")
    dosya.write("\n" + metin.format(ad, soyad, tel))
    dosya.close()
    
    
    
def kayitlari_listele() :
    dosya = open("veri.txt","r")
    print(dosya.read())
    dosya.close()