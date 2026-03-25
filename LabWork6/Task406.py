import math

try:
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    r = (x+y+z)/math.pow((x-y+z),2)
    if r < 0:
        raise ValueError("Отрицательное под корнем")
    print(math.sqrt(r))
except ValueError as e:
    print(e)
except:
    print("Error")

