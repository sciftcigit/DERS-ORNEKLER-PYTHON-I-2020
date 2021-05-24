import tkinter
from tkinter import font


def topla () :
    sayi1 = E1.get()
    sayi2 = E2.get()
    
    if ( islem.get() == 1 ) :
        sonuc = float(sayi2) + float(sayi1)
    elif ( islem.get() == 2 ) :
        sonuc = float(sayi1) - float(sayi2)
    elif ( islem.get() == 3 ) :
        sonuc = float(sayi1) / float(sayi2)
    elif ( islem.get() == 4 ) :
        sonuc = float(sayi1) * float(sayi2)
        
    Etiket3.config(text = "Sonuç :" + str(sonuc))
    
    
    
    
#pencere oluşturuyoruz - illaki olmalı   
pencere = tkinter.Tk()
pencere.geometry("250x450")

Font = ("Times New Roman", 14)
FontBold = ("Times New Roman", 14, "bold")

Etiket1 = tkinter.Label( pencere, text="Sayı 1", font=FontBold )
Etiket1.pack()
# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E1 = tkinter.Entry(pencere,  bd =5, font=Font)
E1.pack()

Etiket2 = tkinter.Label( pencere, text="Sayı  2" , font=FontBold)
Etiket2.pack()
# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E2 = tkinter.Entry(pencere,  bd =5, font=Font)
E2.pack()

islem = tkinter.IntVar()
islem.set(1)

R1 = tkinter.Radiobutton(pencere, text="Toplama", variable=islem, value=1, font=Font)
R1.pack()
R2 = tkinter.Radiobutton(pencere, text="Çıkarma", variable=islem, value=2, font=Font)
R2.pack()
R3 = tkinter.Radiobutton(pencere, text="Bölme", variable=islem, value=3, font=Font)
R3.pack()
R4 = tkinter.Radiobutton(pencere, text="Çarpma", variable=islem, value=4, font=Font)
R4.pack()

Etiket3 = tkinter.Label( pencere, text="Sonuç:" , font=FontBold)
Etiket3.pack()

# düğme tıklanınca birşeyler yapması lazım
Dugme1 = tkinter.Button(pencere, text ="Hesapla", command=topla, font=FontBold)
Dugme1.pack(side="bottom")

# pencerenin ekranda belirlemesini sağlıyoruz - illaki olmalı   
pencere.mainloop()