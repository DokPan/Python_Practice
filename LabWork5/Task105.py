s = str(input("Введите строку: "))
print((s+"\n")*4+s)
print(len(s))
for i in range(len(s)):
    print(f"{i}:{s[i]}")
print()
for i in range(1,len(s),2):
    print(f"{i+1}:{s[i]}")