import tkinter
from tkinter import font
import mysql.connector


def ekle () :
    ad = E1.get()
    soyad = E2.get()
    telefon = E3.get()
    
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb")
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO telefon_rehberi (ad, soyad, telefon) VALUES (%s, %s, %s)"
    val = (ad, soyad, telefon)
    mycursor.execute(sql, val)

    mydb.commit()
    print("eklendi")


    
#pencere oluşturuyoruz - illaki olmalı   
pencere = tkinter.Tk()
pencere.geometry("250x450")

Font = ("Times New Roman", 14)
FontBold = ("Times New Roman", 14, "bold")

Etiket1 = tkinter.Label( pencere, text="Ad ", font=FontBold )
Etiket1.pack()
# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E1 = tkinter.Entry(pencere,  bd =5, font=Font)
E1.pack()

Etiket2 = tkinter.Label( pencere, text="Soyad" , font=FontBold)
Etiket2.pack()
# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E2 = tkinter.Entry(pencere,  bd =5, font=Font)
E2.pack()

Etiket3 = tkinter.Label( pencere, text="Telefon" , font=FontBold)
Etiket3.pack()
# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E3 = tkinter.Entry(pencere,  bd =5, font=Font)
E3.pack()

Etiket3 = tkinter.Label( pencere, text="" , font=FontBold)
Etiket3.pack()

# düğme tıklanınca birşeyler yapması lazım
Dugme1 = tkinter.Button(pencere, text ="EKLE", command=ekle, font=FontBold)
Dugme1.pack(side="bottom")

# pencerenin ekranda belirlemesini sağlıyoruz - illaki olmalı   
pencere.mainloop()
