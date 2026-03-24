s = str(input("Введи строку: "))
if s.isdigit():
    print("Цифры")
elif s.isalpha():
    if s.islower():
        print("Буквы в нижнем регистре")
    elif s.isupper():
        print("Буквы в вехнем регистре")
    else:
        print("Буквы в обоих регистрах")
elif s.isalnum():
    print("Цифры и буквы")
else:
    print("Другие символы")