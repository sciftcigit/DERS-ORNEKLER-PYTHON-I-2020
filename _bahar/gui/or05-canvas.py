import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=300, width=300)

coord = 10, 50, 240, 110
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()