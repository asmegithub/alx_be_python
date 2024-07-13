import unittest


class ZeroDivisionError(Exception):

    def __str__(self):
        return "Division by zero is invalid!! "


def devision(x, y):
    return x/y


def square(x):
    return x**2


class TestSqure(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(5), 25)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-1), 1)
        self.assertEqual(square(-2), 4)


class LearnTest(unittest.TestCase):
    def setUp(self) -> None:
        print("Start test")
        pass

    def test_fun_1(self):
        self.assertEqual(devision(10, 5), 2)
        self.assertEqual(devision(0, 5), 0)

    def test_fun_2(self):
        pass

    def test_fun_3_test(self):
        pass


if __name__ == '__main__':
    unittest.main()
