from tkinter import *

root = Tk()
root.title("Координаты мыши")
root.geometry("400x300")

l = Label(root,text="Координаты: ")
l.pack(pady=20)

def move(e):
    l.config(text=f"x={e.x}, y={e.y}")

root.bind("<Motion>",move)

root.mainloop()