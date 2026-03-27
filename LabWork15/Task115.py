from tkinter import *
from tkinter import filedialog
def save(e=None):
    t = txt.get("1.0",END)
    f = filedialog.asksaveasfilename()
    if f:
        open(f,"w",encoding="utf-8").write(t)

def close(e):
    root.destroy()

root = Tk()
root.title("Сохранение текста")
root.geometry("400x300")

txt=Text(root)
txt.pack()

Button(root,text="Сохранить",command=save).pack()

root.bind("<Control-s>",save)
root.bind("<Escape>",close)

root.mainloop()