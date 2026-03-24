s1 = str(input("Введи 1 строку: "))
s2 = str(input("Введи 2 строку: "))

for i in range(len(s2)-len(s1)+1):
    if s2[i:i+len(s1)] == s1:
        print(f"Позиция: {i+1}")