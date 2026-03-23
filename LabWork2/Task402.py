x = int(input("Введите x:"))
y = int(input("Введите y:"))
z = int(input("Введите z:"))

if (x == y == z):
    print("Равносторонний")
elif (x==y )or (y==z) or (z==x):
    print("Равнобедренный")
elif x**2+y**2==z**2:
    print("Прямоугольный")
else:
    print("Не существует")