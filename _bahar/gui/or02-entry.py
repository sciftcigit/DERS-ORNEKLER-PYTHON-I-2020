import tkinter
from tkinter.constants import COMMAND

def selamla () :
    metin = E1.get()
    print("Selam " + metin)
    

    
#pencere oluşturuyoruz - illaki olmalı   
pencere = tkinter.Tk()

# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E1 = tkinter.Entry(pencere,  bd =5)
E1.pack(side = "left")

# düğme tıklanınca birşeyler yapması lazım
Dugme1 = tkinter.Button(pencere, 
                        text ="Merhaba", 
                        command=selamla,
                        )
Dugme1.pack(side="bottom")

# pencerenin ekranda belirlemesini sağlıyoruz - illaki olmalı   
pencere.mainloop()