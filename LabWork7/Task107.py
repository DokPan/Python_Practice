import math

def powfunction (x:'степень',a:'число'=2):
    """Функиция возводит число а в степень х"""
    result = math.pow(a,x)
    print(result)

powfunction(3)
powfunction(4,3)

