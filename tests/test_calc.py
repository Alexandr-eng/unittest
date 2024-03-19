import math
import unittest
from parameterized import parameterized

from app.error import InvalidInputException
from app.main import Calculator
from math import inf


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def tearDown(self) -> None:
        ...

    @parameterized.expand(
        # 1. arrange
        [
            ("integers", 2, 3, 5),
            ("floats", 2.5, 3.1, 5.6),
            ("negative", -2.5, 3.0, 0.5)
        ]
    )
    def test_sum(self, name, a, b, expected_result):
        # 2. act
        actual_result = self.calc.sum(a, b)

        # 3. assert
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("strings", 'aaa', 'bbb', TypeError),
        ("int_None", 1, None, TypeError),
        ("None_float", None, 1.1, TypeError),
        ("None_None", None, None, TypeError)

    ])
    def test_sum_invalid_values(self, name, a, b, expected_result):
        with self.assertRaises(expected_result):
            self.calc.sum(a, b)

    @parameterized.expand([
        ("list_integers", [1, 2, 3, 4], 10),
        ("list_empty", [], 0),
        ("list_single", [1], 1)
    ])
    def test_sum_list(self, name, a, expected_result):
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("tuple_integers", (1, 2, 3, 4), 10),
        ("tuple_empty", (), 0),
        ("tuple_single", (1,), 1),
        ("set_integers", {1, 2, 3, 4}, 10),
        ("set_empty", {}, 0),
        ("set_single", {1}, 1),
    ])
    def test_sum_tuple(self, name, a, expected_result):
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    def test_multiply(self):
        a = 5
        b = 0.000000005

        actual_result = self.calc.multiply(a, b)
        expected_result = 0

        self.assertAlmostEqual(actual_result, expected_result)

    def test_divide(self):
        a = 5
        b = 0

        expected_result = ZeroDivisionError

        with self.assertRaises(expected_result):
            self.calc.divide(a, b)

    def test_divide_inf(self):
        a = inf
        b = inf

        expected_result = None
        actual_result = self.calc.divide(a, b)

        self.assertNotEqual(actual_result, expected_result)
        self.assertIsInstance(actual_result, type(math.inf))
        self.assertIsInstance(actual_result, float)

    @parameterized.expand([
        ("valid_inputs_1", 10, 2),  # Ожидаем успешное выполнение (10 > 0, 10 != 1, 2 > 0)
        ("valid_inputs_2", 100, 10),  # Ожидаем успешное выполнение (100 > 0, 100 != 1, 10 > 0)
        ("valid_inputs_3", 2, 2)  # Ожидаем успешное выполнение (2 > 0, 2 != 1, 2 > 0)
    ])
    def test_log_valid_values(self, name, a, base):
        try:
            result = self.calc.log(a, base)
            # Можно добавить проверку результата, если необходимо
        except InvalidInputException as e:
            self.fail(f"Unexpected InvalidInputException: {str(e)}")

    @parameterized.expand([
        ("string_base", 10, 'string'),  # Ожидаем InvalidInputException из-за нечислового base
        ("base_zero", 10, 0),  # Ожидаем InvalidInputException из-за base равного 0
        ("a_negative", -5, 2),  # Ожидаем InvalidInputException из-за отрицательного a
        ("a_equals_1", 1, 2),  # Ожидаем InvalidInputException из-за a равного 1
        ("a_zero_base", 0, 3)  # Ожидаем InvalidInputException из-за a равного 0
    ])
    def test_log_invalid_values(self, name, a, base):
        with self.assertRaises(InvalidInputException):
            self.calc.log(a, base)

if __name__ == "__main__":
    unittest.main()
