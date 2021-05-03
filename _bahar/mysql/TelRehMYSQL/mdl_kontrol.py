def cizgi_at() :
    print("-------------------------------------------------")

def telefon_format(n):                                                                                                                                  
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]  

def telefon_kontrol(telefon):
    
    return_degeri = False
    if ( not telefon.isnumeric() ) :
        print("telefon numarası sayı olmalıdır.")  
    else : 
        return_degeri = True

    return return_degeri

def id_kontrol(veri):
    
    return_degeri = False
    if ( not veri.isnumeric() ) :
        print(" sayı girmelisiniz .")  
    else : 
        return_degeri = True

    return return_degeri

def ad_kontrol(ad):
    return_degeri = False
    veri = ad.replace(" ", "") 
    
    if not veri.isalpha(): 
        print("ad/soyad sadece harflerden oluşabilir.")  
    elif len(veri) <2 or len(veri)>50 :
        print("ad/soyad en az 2 en fazla 25 karakterden oluşabilir.")
    else : 
        return_degeri = True

    return return_degeri     