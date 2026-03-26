import os

filename = str(input("Введите имя файла: "))

if os.path.exists(filename):
    if input("Файл существует. Дописать (d) или переписать (p)? ") == 'p':
        f = open(filename, 'w', encoding='utf-8')
    else:
        f = open(filename, 'a', encoding='utf-8')
else:
    f = open(filename, 'w', encoding='utf-8')

print("Введите текст (для завершения введите 'end'): ")
while True:
    line = input()
    if line == 'end':
        break
    f.write(line + '\n')

f.close()
print("Готово")

