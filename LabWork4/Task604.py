list = [1,2,3,4,5]
print(list)

n = int(input("Введите число: "))

for i in range(n):
    index = int(input("Индекс: "))
    value = int(input("Значение: "))
    list.insert(index, value)
print(list)