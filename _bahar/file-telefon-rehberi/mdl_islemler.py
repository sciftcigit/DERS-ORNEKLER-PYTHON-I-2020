
def kayit_ekle():
    # ##
    #  Kullanıcıdan veri isteme 
    # ##
    ad      = input("Ad giriniz :");
    soyad   = input("Soyad giriniz :");
    tel     = input("Telefon giriniz :");

    metin = "Ad: {:<30}  Soyad: {:<30}  Telefon: {:<15}   "
    metin_f = metin.format(ad, soyad, tel)
    print(metin_f)

    # ##
    #  Verileri txt dosyasına saklama 
    # ##
    dosya = open("veri.txt","a")
    dosya.write("\n" + metin_f)
    dosya.close()
    
    
    
def kayitlari_listele() :
    dosya = open("veri.txt","r")
    
    id = 0 
    for satir in dosya:
        id += 1
        print("Kayıt ID = " + str(id) + " : " + satir)

    dosya.close()
    
    
def kayit_sil() :
    # önce dosyanın içeriğini aldık dizi atadık 
    # daha sorular dosyayı "w" formatında açtık 
    # ve dizide buluna veriyi yeniden txt dosyanin içerisinde yazdık.
    kayit_id = input("Silmek istediğiniz kayıt id'sini giriniz:")
    dosya = open("veri.txt","r")
    
    dizi = [] 
    for satir in dosya:
        # dosya içeriğini diziye atıyoruz 
        dizi.append(satir)
    # diziden silinmek istenilen kaydı siliyoruz. 
    dizi.pop( int(kayit_id)-1 )
    dosya.close()
    
    
    # "w" formatında dosyayı açıyoruz içindeki veriler siliniyor.
    dosya = open("veri.txt","w")
    
    # Liste içinde olan tüm veriyi satır satır dosyaya yeniden yazıyoruz 
    for satir in dizi : 
        dosya.write(satir) 
    dosya.close()
    
    print("Kayıt silindi!")
    
    
def kayit_duzenle() :

    kayit_id = input("Düzenlemek istediğiniz kayıt id'sini giriniz:")
    dosya = open("veri.txt","r")
    
    dizi = [] 
    for satir in dosya:
        # dosya içeriğini diziye atıyoruz 
        dizi.append(satir)
    dosya.close()
    # buraya kadar olan kodda dosya içeriğini diziye aktardık.
    

    # ##
    #  Kullanıcıdan veri isteme 
    # ##
    ad      = input("Ad giriniz :");
    soyad   = input("Soyad giriniz :");
    tel     = input("Telefon giriniz :");

    metin = "Ad: {:<30}  Soyad: {:<30}  Telefon: {:<15}   "
    metin_f = metin.format(ad, soyad, tel)
    
    # girilen id'deki veriyi kullanıcıdan aldığımız 
    # yeni bilgilerle düzenliyoruz
    dizi[ int(kayit_id)-1 ]  =   metin_f + "\n"
    
    # "w" formatında dosyayı açıyoruz içindeki veriler siliniyor.
    dosya = open("veri.txt","w")
    
    # Liste içinde olan tüm veriyi satır satır dosyaya yeniden yazıyoruz 
    for satir in dizi : 
        dosya.write(satir) 
    dosya.close()
    
    print("Kayıt düzenlendi!")

    
    