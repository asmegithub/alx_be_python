import unittest

from simple_calculator import SimpleCalculator
import unittest
from simple_calculator import SimpleCalculator


class SimpleCalculatorTest(unittest.TestCase):
    def test_addition(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiplication(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertIsNone(self.calc.divide(1, 0))
        self.assertIsNone(self.calc.divide(0, 0))


if __name__ == "__main__":
    unittest.main()
