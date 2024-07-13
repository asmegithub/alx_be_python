import unittest


class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b


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


# if __name__ == "__main__":
#     unittest.main()
