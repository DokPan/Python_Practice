f = open(input("Имя файла: "), 'r', encoding='utf-8')
lines = f.readlines()
f.close()

print("1 строка:", lines[0].strip() if len(lines) > 0 else "Нет строк")
print("5 строка:", lines[4].strip() if len(lines) > 4 else "Нет 5-й строки")
print("Первые 5 строк:")
for i in range(min(5,len(lines))):
    print(lines[i].strip())

s1 = int(input("s1: "))
s2 = int(input("s2: "))
print(f"Строки с {s1} по {s2}:")
for i in range(s1-1, min(s2,len(lines))):
    print(lines[i].strip())

print("Весь файл:")
for line in lines:
    print(line.strip())