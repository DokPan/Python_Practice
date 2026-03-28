import subprocess
import time


def show_processes():
   subprocess.run('tasklist',shell=True)
   input("Нажмите Enter")


def start_program():
    path = input("Путь к программе: ")
    try:
        subprocess.Popen(path)
        print("Запущено!")
    except:
        print("Ошибка!")
    time.sleep(1)


def kill_process():
    pid = input("ID процесса: ")
    try:
        subprocess.run(f'taskkill /F /PID {pid} /T',shell=True)
        print("Завершён!")
    except:
        print("Не найден!")
    time.sleep(1)


while True:
    print("\n1. Процессы")
    print("2. Запустить")
    print("3. Завершить")
    print("4. Выход")

    choice = input("Выбор: ")

    if choice == "1":
        show_processes()
    elif choice == "2":
        start_program()
    elif choice == "3":
        kill_process()
    elif choice == "4":
        break