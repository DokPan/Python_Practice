import threading
import time

event = threading.Event()
message = ""

def sender():
    global message
    for text in ["Привет", "Как дела?", "Пока"]:
        message = text
        print("Отправил:", message)
        event.set()
        time.sleep(2)

def receiver():
    for i in range(3):
        event.wait()
        print("Получил:", message)
        event.clear()

t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=receiver)

t1.start()
t2.start()

t1.join()
t2.join()