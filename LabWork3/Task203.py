import random

a = (random.randint(1,10))

b = int(input("Введи число:"))
while b!=a:
    if b >a:
        print("Число меньше")
        b=int(input("Введи число:"))
    elif b < a:
        print("Число больше")
        b = int(input("Введи число:"))

print("Молодец ты угадал число")