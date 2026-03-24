s = str(input("Введите строку: "))
while "  " in s:
    s = s.replace("  "," ")
print(s)