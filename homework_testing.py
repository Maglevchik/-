import unittest

# Функция калькулятора
def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return "Error: Division by zero"
        return a / b

# Тесты для калькулятора
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator(10, 5, 'add'), 15)

    def test_subtract(self):
        self.assertEqual(calculator(10, 5, 'subtract'), 5)

    def test_multiply(self):
        self.assertEqual(calculator(10, 5, 'multiply'), 50)

    def test_divide(self):
        self.assertEqual(calculator(10, 5, 'divide'), 2)


# Функция проверки на четность
def is_even(num):
    return num % 2 == 0

# Параметрический тест
class TestIsEven(unittest.TestCase):
    def test_is_even_parameterized(self):
        # Набор данных: (число, ожидаемый результат)
        test_cases = [
            (2, True),
            (3, False),
            (0, True),
            (-4, True),
            (-5, False),
            (11, False)
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(is_even(num), expected)


# Функция безопасного деления
def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b

# Тест на исключение
class TestSafeDivide(unittest.TestCase):
    def test_divide_by_zero_exception(self):
        # Проверяем, что при b=0 вызывается ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            safe_divide(10, 0)

    def test_normal_division(self):
        self.assertEqual(safe_divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()