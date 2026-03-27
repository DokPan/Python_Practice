from tkinter import *

root = Tk()
root.title("Авторизация")
root.geometry("200x300")

Label(root, text="Логин").pack(pady=20)
Entry(root).pack()
Label(root, text="Пароль").pack(pady=10)
Entry(root).pack()
Checkbutton(root, text="Запомнить меня").pack(pady=10)
Button(root, text="Авторизоваться").pack(pady=20)

root.mainloop()