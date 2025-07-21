# from tkinter import *

# window = Tk(className='Duck')
# window.geometry("600x400")
# window.resizable(True, True)

# label = Label(window, textvariable='Quack')
# label.pack()

# window.mainloop()

from tkinter import Tk, Label
from tkinter.ttk import Label as TtkLabel

root = Tk()
Label(root, text="Classic Tkinter").pack()
TtkLabel(root, text="Themed TTK").pack()
root.mainloop()