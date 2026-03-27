from tkinter import *

def show():
    l.config(text=f"{t.get()},{c.get()},{r.get()}")
root = Tk()
root.title("Связанные переменные")
root.geometry("300x250")

t = StringVar()
c = IntVar()
r =StringVar()

Entry(root,textvariable=t).pack()
Checkbutton(root,text="Флажок",variable=c,command=show).pack()
Radiobutton(root,text="Да", variable=r,value="да",command=show).pack(pady=10)
Radiobutton(root,text="Нет", variable=r,value="нет",command=show).pack(pady=10)
l = Label(root,text="")
l.pack()
Button(root,text="Показать",command=show).pack()
root.mainloop()