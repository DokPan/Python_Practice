from functools import partial
from tkinter import *

root = Tk()
root.title("Меню")
root.geometry("400x300")

def red(event=None):
    root.config(bg="red")

def green(event=None):
    root.config(bg="green")

def blue(event=None):
    root.config(bg="blue")

def s500(event=None):
    root.geometry("500x500")

def s700(event=None):
    root.geometry("700x400")

m =Menu(root)
root.config(menu = m)

m.add_command(label="Red",command=red,accelerator="Ctrl+R")
m.add_command(label="Green",command=green,accelerator="Ctrl+G")
m.add_command(label="Blue",command=blue,accelerator="Ctrl+B")
m.add_separator()
m.add_command(label="500x500",command=s500,accelerator="Ctrl+Y")
m.add_command(label="700x400",command=s700,accelerator="Ctrl+X")

root.bind_all("<Control-r>",partial(red))
root.bind_all("<Control-g>",partial(green))
root.bind_all("<Control-b>",partial(blue))
root.bind_all("<Control-y>",partial(s500))
root.bind_all("<Control-x>",partial(s700))
root.mainloop()