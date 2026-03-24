import random

n = int(input("Введите длину списка: "))
list = []
for i in range(n):
    list.append(random.randint(0,100))

for i in range(n):
    print(f"{i}:{list[i]}")
