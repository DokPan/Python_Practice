import threading
import time

counter = 0
semaphore = threading.Semaphore(1)

def go(num):
    global counter
    for i in range(10):
        semaphore.acquire()
        counter += 1
        print(f"Поток {num}: counter = {counter}")
        if counter == 10:
            counter = 0
        semaphore.release()
        time.sleep(0.1)

for i in range(10):
    threading.Thread(target=go, args=(i,)).start()
