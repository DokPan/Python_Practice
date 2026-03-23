import random

a = (random.randint(1,1000))
print(a)
simple = True
if a < 2:
    print("Сложное")
else:
    simple = True
    for i in range (2,a):
        if a % i ==0:
            simple = False
            break

if simple:
    print("Простое")
else:
    print("Сложное")

