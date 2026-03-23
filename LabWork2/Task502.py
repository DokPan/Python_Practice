a = int(input("Введите a:"))
b = int(input("Введите b:"))

operation = input ("& | ^ << >> : ")

if operation == '&' : result = a & b
if operation == '|' : result = a | b
if operation == '^' : result = a ^ b
if operation == "<<" : result = a << b
if operation == ">>" : result = a >> b

print(f"\n{result} = {bin(result)}")