n = int(input("Введите число: "))
list = [1,2,3,1,2,3,1,2,3]

while n in list:
    list.remove(n)
print(list)