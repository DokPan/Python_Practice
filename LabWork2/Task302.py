year = int(input("Введите год: "))
month = int(input("Введите месяц: "))

days=(
    31 if month in [1,3,5,7,8,10,12] else
    30 if month in [ 4,6,9,11] else
    29 if month == 2 and (year%4==0 and year%100 != 0 or year%400 ==0) else
    28 if month == 2 else
    0
)

print(days)