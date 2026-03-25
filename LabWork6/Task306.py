import math

x=float(input("x = "))
y=float(input("y = "))
z=float(input("z = "))

if(x-y+z) ==0:
    print("Нельзя")
else:
    print(math.sqrt((x+y+z)/math.pow((x-y+z),2)))