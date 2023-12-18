import unittest
from app.calculator import Calculator


class TestCalculatorMethods(unittest.TestCase):

    def setUp(self):
        # Ініціалізація об'єкта Calculator для використання в тестах
        self.calc = Calculator(4, 2)

    def test_add_positive_numbers(self):
        result = self.calc.add()
        self.assertEqual(result, 6, "Error in add method for positive numbers")

    def test_add_negative_numbers(self):
        calc = Calculator(-4, -2)
        result = calc.add()
        self.assertEqual(result, -6, "Error in add method for negative numbers")

    def test_add_zero(self):
        calc = Calculator(0, 0)
        result = calc.add()
        self.assertEqual(result, 0, "Error in add method for zero")

    def test_add_mixed_signs(self):
        calc = Calculator(-4, 2)
        result = calc.add()
        self.assertEqual(result, -2, "Error in add method for mixed signs")

    def test_subtract(self):
        result = self.calc.subtract()
        self.assertEqual(result, 2, "Error in subtract method")

    def test_multiply_positive_numbers(self):
        result = self.calc.multiply()
        self.assertEqual(result, 8, "Error in multiply method for positive numbers")

    def test_multiply_negative_numbers(self):
        calc = Calculator(-4, 2)
        result = calc.multiply()
        self.assertEqual(result, -8, "Error in multiply method for negative numbers")

    def test_multiply_zero(self):
        calc = Calculator(4, 0)
        result = calc.multiply()
        self.assertEqual(result, 0, "Error in multiply method for zero")

    def test_divide(self):
        result = self.calc.divide()
        self.assertEqual(result, 2, "Error in divide method")

    def test_divide_by_zero(self):
        calc = Calculator(4, 0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide()

    def test_power_positive_exponents(self):
        result = self.calc.power()
        self.assertEqual(result, 16, "Error in power method for positive exponents")

    def test_power_negative_exponents(self):
        calc = Calculator(4, -2)
        result = calc.power()
        self.assertEqual(result, 0.0625, "Error in power method for negative exponents")

    def test_power_zero_exponent(self):
        calc = Calculator(4, 0)
        result = calc.power()
        self.assertEqual(result, 1, "Error in power method for zero exponent")

    def test_random_number_within_range(self):
        result = Calculator.random_number(1, 10)
        self.assertTrue(1 <= result <= 10, "Error in random_number method")

    def test_random_number_same_values(self):
        result = Calculator.random_number(5, 5)
        self.assertEqual(result, 5, "Error in random_number method for same values")

    def test_random_number_negative_range(self):
        result = Calculator.random_number(-10, -5)
        self.assertTrue(-10 <= result <= -5, "Error in random_number method for negative range")

    def test_random_number_mixed_range(self):
        result = Calculator.random_number(-5, 5)
        self.assertTrue(-5 <= result <= 5, "Error in random_number method for mixed range")


if __name__ == '__main__':
    unittest.main()
