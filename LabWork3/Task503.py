n = int(input())
a = float(input())
b = float(input())
x1 = float(input())
x2 = float(input())

if n == 1:
    xs = [x1]
else:
    step = (x2 - x1) / (n - 1)
    xs = [x1 + i*step for i in range(n)]

if x1 > x2:
    xs.reverse()

for x in xs:
    y = a*x + b
    print(f"y({x:.3f}) = {a}*{x:.2f}+{b}={y:.3f}")
