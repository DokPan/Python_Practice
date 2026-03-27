from tkinter import *

def press(e):
    l.config(text=f"Клавиша: {e.char}")

root = Tk()
root.title("Клавиши")
root.geometry("400x300")

l = Label(root,text="Клавиша: ")
l.pack(pady=30)


root.bind("<Key>",press)

root.mainloop()