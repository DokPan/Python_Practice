from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("Регистрация")
root.geometry("300x500")
root.config(bg="lavenderblush")

Label(root, text="Логин", bg="mistyrose").pack(pady=20)
Entry(root).pack()
Label(root, text="Пароль", bg="mistyrose").pack(pady=10)
Entry(root).pack()
Label(root, text="О себе", bg="mistyrose").pack(pady=10)
Text(root, height=4, width=30).pack()
Label(root, text="Пол", bg="mistyrose").pack()
Radiobutton(root,text="Мужской", bg="mistyrose").pack(pady=10)
Radiobutton(root,text="Женский", bg="mistyrose").pack(pady=10)
Label(root, text="Материк", bg="mistyrose").pack()
Combobox(root, values=["Евразия", "Африка", "Северная Америка", "Южная Америка", "Антарктида", "Австралия"]).pack()
Button(root, text="Зарегистрироваться").pack(pady=20)

root.mainloop()