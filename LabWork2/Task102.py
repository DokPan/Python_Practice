import math

x = int(input("Введите x:"))

if x<(-10):
    y = math.pi*math.pow(x,2)
elif  -10<= x <(-5):
    y = math.pow(x,4)
elif -5 <= x <10:
    y =math.e * math.fabs(x)
else:
    y = 1/math.sin(math.sqrt(x))

print(y)