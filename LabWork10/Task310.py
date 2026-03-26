def factorial(n):
    if n <0:
        return None
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

n = 5
fact1 = factorial(n)
fact2 = factorial(n)
print(f"Факториал числа {n} = {fact1}")