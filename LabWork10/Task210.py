def factorial(n):
    if n <0:
        raise ValueError("Не определен для отрицательных чисел")
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

n = 5
print(f"Факториал числа {n} = {factorial(n)}")