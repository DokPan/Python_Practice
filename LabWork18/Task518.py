import threading
import time
import random

semaphore = threading.Semaphore(3)


def request_handler(user_id):
    print(f"Пользователь {user_id} ждет доступа")

    semaphore.acquire()
    print(f"Пользователь {user_id} подключился к серверу")

    time.sleep(random.uniform(1, 3))

    print(f"Пользователь {user_id} отключился")
    semaphore.release()


for i in range(1, 11):
    threading.Thread(target=request_handler, args=(i,)).start()