import socket
import tkinter as tk

HOST = "localhost"
PORT = 50007

def send_message():
    login = entry_login.get()
    message = entry_message.get()
    s.sendall(f"{login}:{message}".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

login = input("Введите логин: ")
s.sendall(login.encode())

root = tk.Tk()
root.title("Чат")

entry_login = tk.Entry(root)
entry_login.pack()
entry_login.insert(0, login)

entry_message = tk.Entry(root)
entry_message.pack()

button = tk.Button(root, text = "Отправить", command = send_message)
button.pack()

root.mainloop()