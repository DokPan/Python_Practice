import unittest

def factorial(n):
    if n <0:
        raise ValueError("Не определен для отрицательных чисел")
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0),1)

    def test_one(self):
        self.assertEqual(factorial(1),1)

    def test_positive(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(4), 24)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)