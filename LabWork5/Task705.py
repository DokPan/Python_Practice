s = str(input("Введите строку: "))
if s.lower()==s.lower()[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")