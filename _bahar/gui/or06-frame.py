from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", bg="red" )
redbutton.pack( side = LEFT)

brownbutton = Button(frame, text="Brown", bg="brown")
brownbutton.pack( side = LEFT )

bluebutton = Button(bottomframe, text="Blue", bg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", bg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()