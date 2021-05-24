import tkinter

def selamla () :
    print("Selam")
    
#pencere oluşturuyoruz - illaki olmalı   
pencere = tkinter.Tk()

# kullanıcıdan veri almak için giriş kutucuğu yani inputbox
E1 = tkinter.Entry(pencere, bd =5)
E1.pack(side = "left")

# düğme tıklanınca birşeyler yapması lazım
Dugme1 = tkinter.Button(pencere, 
                        text ="Merhaba", 
                        command=selamla,
                        bd=5,
                        padx=100,
                        pady=100,
                        state="normal",
                        underline=3,
                        bg="#09bce0",
                        fg="#fff",
                        height=5,
                        justify="right",
                        width=25,
                        activeforeground="#4287f5",
                        activebackground="#cdd154")
Dugme1.pack(side="bottom")

# pencerenin ekranda belirlemesini sağlıyoruz - illaki olmalı   
pencere.mainloop()