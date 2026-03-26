import os

name = str(input("Введите имя файла: "))

try:
    f = open(name, 'r', encoding='utf-8')
    text = f.read()
    print(text)
    f.close()

    if os.path.splitext(name)[1] == '.py':
        exec(text)
except:
    print("Ошибка")