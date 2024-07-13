import unittest

from simple_calculator import SimpleCalculator


class SimpleCalculatorTest(unittest.TestCase):
    def test_add(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(0, 0), 0)

    def test_subtract(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(1, 2), -1)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(0, 0), 0)

    def test_multiply(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(1, 2), 2)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(0, 0), 0)

    def test_divide(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(1, 2), 0.5)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(0, 1), 0)
        self.assertIsNone(calc.divide(1, 0))
        self.assertIsNone(calc.divide(0, 0))
    pass


if __name__ == "__main__":
    unittest.main()
