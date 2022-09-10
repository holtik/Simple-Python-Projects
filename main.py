import sys
import tkinter
from tkinter import *
import tkinter.filedialog
from tkinter import filedialog

root = Tk("Text Editor")
text = Text(root)
text.pack()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


button = Button(root, text="Save", command=saveas)
button.pack()

font = Menubutton(root, text="Font")
font.pack()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

color = Menubutton(root, text="Color")
color.pack()
color.menu = Menu(color, tearoff=0)
color["menu"] = color.menu


black = IntVar()
red = IntVar()
yellow = IntVar()
green = IntVar()
blue = IntVar()

helvetica = IntVar()
courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=lambda: text.config(font="Courier"))
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=lambda: text.config(font="Helvetica"))

color.menu.add_radiobutton(label="Black", variable=black, command=lambda: text.config(fg="black"))
color.menu.add_radiobutton(label="Red", variable=red, command=lambda: text.config(fg="red"))
color.menu.add_radiobutton(label="Yellow", variable=yellow, command=lambda: text.config(fg="yellow"))
color.menu.add_radiobutton(label="Green", variable=green, command=lambda: text.config(fg="green"))
color.menu.add_radiobutton(label="Blue", variable=blue, command=lambda: text.config(fg="blue"))


root.mainloop()
