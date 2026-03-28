import threading
import time

lock = threading.Lock()

def numbers():
    for i in range(10):
        with lock:
            print(i)
        time.sleep(2)

def letters():
    for c in "ABCDEFGHIJ":
        with lock:
            print(c)
        time.sleep(2)

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=letters)

t1.start()
t2.start()

t1.join()
t2.join()