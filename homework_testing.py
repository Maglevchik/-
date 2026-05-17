import unittest
from typing import Union

# Функция калькулятора
def calculator(a: Union[int, float], b: Union[int, float], operation: str) -> Union[int, float, str]:
    """
    Выполняет базовые арифметические операции над двумя числами.
    
    :param a: Первое число (int или float).
    :param b: Второе число (int или float).
    :param operation: Название операции ('add', 'subtract', 'multiply', 'divide').
    :return: Результат вычисления или строка с ошибкой при делении на ноль.
    :raises ValueError: Если передана неизвестная операция.
    """
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
    else:
        # Обработка неизвестной операции согласно замечанию ментора
        raise ValueError(f"Unknown operation: {operation}")

# Тесты для калькулятора
class TestCalculator(unittest.TestCase):
    """Тестовый класс для проверки работы функции calculator."""

    def test_add(self) -> None:
        """Проверка операции сложения."""
        self.assertEqual(calculator(10, 5, 'add'), 15)

    def test_subtract(self) -> None:
        """Проверка операции вычитания."""
        self.assertEqual(calculator(10, 5, 'subtract'), 5)

    def test_multiply(self) -> None:
        """Проверка операции умножения."""
        self.assertEqual(calculator(10, 5, 'multiply'), 50)

    def test_divide(self) -> None:
        """Проверка операции обычного деления."""
        self.assertEqual(calculator(10, 5, 'divide'), 2)
        
    def test_divide_negative(self) -> None:
        """Проверка операции деления с отрицательными числами."""
        self.assertEqual(calculator(-10, 2, 'divide'), -5)
        self.assertEqual(calculator(10, -2, 'divide'), -5)
        self.assertEqual(calculator(-10, -5, 'divide'), 2)

    def test_divide_by_zero(self) -> None:
        """Проверка возврата сообщения об ошибке при делении на ноль."""
        self.assertEqual(calculator(10, 0, 'divide'), "Error: Division by zero")

    def test_unknown_operation(self) -> None:
        """Проверка выброса исключения ValueError при неизвестной операции."""
        with self.assertRaises(ValueError):
            calculator(10, 5, 'power')


# Функция проверки на четность
def is_even(num: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param num: Проверяемое целое число.
    :return: True, если число четное, иначе False.
    """
    return num % 2 == 0

# Параметрический тест
class TestIsEven(unittest.TestCase):
    """Тестовый класс для проверки функции is_even."""

    def test_is_even_parameterized(self) -> None:
        """Параметризованный тест для проверки различных чисел."""
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
def safe_divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Выполняет деление первого числа на второе с жесткой проверкой деления на ноль.

    :param a: Делимое.
    :param b: Делитель.
    :return: Результат деления.
    :raises ZeroDivisionError: Если делитель равен нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо")
    return a / b

# Тест на исключение
class TestSafeDivide(unittest.TestCase):
    """Тестовый класс для проверки функции safe_divide."""

    def test_divide_by_zero_exception(self) -> None:
        """Проверка, что при делении на ноль вызывается ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            safe_divide(10, 0)

    def test_normal_division(self) -> None:
        """Проверка корректного выполнения деления."""
        self.assertEqual(safe_divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()
