class Author:
    def __init__(self,f,s):
        self.f=f
        self.s=s

n = int(input("Количество авторов: "))
a = []

for i in range(n):
    a.append(Author(input("ФИО: "),input("Страна: ")))

print("\nВсе: ")
for i in a:
    print(i.f,i.s)

print("\nРусские: ")
for i in a:
    if i.s == "Россия":
        print(i.f,i.s)