import tkinter

def topla () :
    sayi1 = E1.get()
    sayi2 = E2.get()
    toplam = float(sayi2) + float(sayi1)
    # print("toplam = " + str(toplam))
    Etiket3.config(text = "Sonuç :" + str(toplam))
    
#pencere oluşturuyoruz - illaki olmalı   
pencere = tkinter.Tk()

Etiket1 = tkinter.Label( pencere, text="Sayı1" )
Etiket1.pack()
# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E1 = tkinter.Entry(pencere,  bd =5)
E1.pack()

Etiket2 = tkinter.Label( pencere, text="Sayı2" )
Etiket2.pack()
# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E2 = tkinter.Entry(pencere,  bd =5)
E2.pack()

Etiket3 = tkinter.Label( pencere, text="Sonuç:" )
Etiket3.pack()

# düğme tıklanınca birşeyler yapması lazım
Dugme1 = tkinter.Button(pencere, text ="Topla", command=topla)
Dugme1.pack(side="bottom")

# pencerenin ekranda belirlemesini sağlıyoruz - illaki olmalı   
pencere.mainloop()