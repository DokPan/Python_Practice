def factorial(n):
    if n < 0 or str(n).isdigit() ==False:
        return -1
    return 1 if n <= 1 else n * factorial(n-1)

print(factorial(5))
print(factorial(-5))
print(factorial(1))