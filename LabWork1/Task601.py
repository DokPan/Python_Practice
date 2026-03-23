year = int(input("Введите год: "))
answer =(year%4 == 0 and year%100 != 0 )or (year%400 == 0)
print(answer)

