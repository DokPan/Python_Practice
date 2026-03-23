x = int(input("Введите x:"))
y = int(input("Введите y:"))
z = int(input("Введите z:"))

middle=(
    x if (y < x < z ) or (z < x < y) else
    y if (x < y < z) or (z < y < x ) else
    z
)
print(middle)