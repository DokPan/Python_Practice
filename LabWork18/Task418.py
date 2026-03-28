import threading

counter = 0
semaphore = threading.Semaphore(1)

def go(num):
    global counter
    for i in range(10):
        semaphore.acquire()
        counter += 1
        print(num, counter)
        if counter == 10:
            counter = 0
        semaphore.release()

for i in range(10):
    threading.Thread(target=go, args=(i,)).start()