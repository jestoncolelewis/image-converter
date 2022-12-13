from tkinter import *
from tkinter.ttk import *

window = Tk(screenName='Photo Converter')

e1 = Entry(window)
e1.grid(row=0)

b1 = Button(window, text="Execute")
b1.grid(row=2, column=3)

window.mainloop()
