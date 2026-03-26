import re

while True:
    p = input("Введите пароль: ")
    if len(p) >=6 and re.search(r'\d',p) and re.search(r'[a-z]',p) and re.search(r'[A-Z]',p):
        print("Пароль надежный")
        break
    else:
        print("Пароль ненадежный. Попробуйте ещё раз")