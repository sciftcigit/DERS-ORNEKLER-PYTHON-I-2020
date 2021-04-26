import mysql.connector

def baglan() :
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="pythondb"
    )
    return mydb
    
def ekle() :

    mydb = baglan()
    ad = input("Ad giriniz ..:")
    soyad = input("Soyad giriniz..:")
    tel = input("Telefon giriniz..:")

    mycursor = mydb.cursor()

    sql = "INSERT INTO telefon_rehberi (ad, soyad, telefon) VALUES (%s, %s, %s)"
    val = (ad, soyad, tel)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, " kayıt eklendi.")

    

def gunc() :
 
    mydb = baglan()
    myid = input("Güncellemek istediğiniz kaydın id'sini giriniz ..:")

    
    ad    = input("Ad giriniz ..:")
    soyad = input("Soyad giriniz..:")
    tel   = input("Telefon giriniz..:")


    mycursor = mydb.cursor()

    sql = """ UPDATE telefon_rehberi SET

                    ad      = '""" + ad    + """',
                    soyad   = '""" + soyad + """',
                    telefon = '""" + tel   + """'
                    
               WHERE id = '""" + myid  + """'
          """
     

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, " kayıt güncellendi.")

    
def list() :

    mydb = baglan()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM telefon_rehberi ORDER BY ad DESC")
    myresult = mycursor.fetchall()

    # burada header / başlık oluşturuyoruz
    cizgi_at()
    metin = "|{:<5} {:<10} {:<10} {:<5} "
    metin_f = metin.format("id","Ad", "Soyad", "Telefon")
    print(metin_f)
    cizgi_at()

    # burada veriyi ekrana yazdırıyoruz
    for veri in myresult:

        metin = "|{:<5} {:<10} {:<10} {:<5} "
        metin_f = metin.format(veri[0],veri[1], veri[2], telefon_format(veri[3]))
        print(metin_f)

    cizgi_at()


def sil() :

    mydb = baglan()
    myid = input("Silmek istediğiniz kaydın id'sini giriniz ..:")
    
    mycursor = mydb.cursor()

    sql = "DELETE FROM telefon_rehberi WHERE id = " + myid
    
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, " kayıt silindi!")

def cizgi_at() :
    print("-------------------------------------------------")

def telefon_format(n):                                                                                                                                  
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]  
