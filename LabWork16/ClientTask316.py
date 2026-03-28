import socket

HOST = "localhost"
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

login = input("Введите логин: ")
s.sendall(login.encode())

while True:
    message = input("Введите сообщение: ")
    if message == "end":
        break
    s.sendall(f"{login}:{message}".encode())

s.close()