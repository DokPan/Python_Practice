import os

file_name = input("Введите имя файла: ")
while True:
    print("\nВыберите действие: ")
    print("1 - вывод содержимого")
    print("2 - удаление файла")
    print("3 - переименование")
    print("4 - выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        if os.path.exists(file_name):
            with open(file_name,"r",encoding='utf-8') as f:
                print(f.read())
        else:
            print("Файл не существует")

    if choice == "2":
        if os.path.exists(file_name):
            os.remove(file_name)
            print("Файл удалён")
        else:
            print("Файл не существует")

    if choice == "3":
        if os.path.exists(file_name):
            new_name = input("Введите новое имя: ")
            os.rename(file_name,new_name)
            print("Файл переименован")
            file_name = new_name
        else:
            print("Файл не существует")

    elif choice == "4":
        break