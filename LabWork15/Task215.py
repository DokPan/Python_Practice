from tkinter import *

def left_click(event):
    label.config(text=f"Активное поле: {event.widget.num}")

def right_click(event):
    print(f"Активное поле: {event.widget.num}")

root = Tk()
root.title("Поле ввода")
root.geometry("400x300")

entry1 =Entry(root)
entry1.num=1
entry1.pack(pady=5)
entry2 =Entry(root)
entry2.num=2
entry2.pack(pady=5)
entry3 =Entry(root)
entry3.num=3
entry3.pack(pady=5)

label=Label(root,text="Активное поле: ")
label.pack(pady=20)

root.bind_class("Entry","<Button-1>",left_click)
root.bind_class("Entry","<Button-3>",right_click)

root.mainloop()