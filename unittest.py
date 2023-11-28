import unittest
from mathematics import add, multiply, power
class TestProgram(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5,4),9)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 6), -12)

    def test_power(self):
        self.assertEqual(power(2, 8), 256)
        self.assertEqual(power(3, 0), 1)
        self.assertEqual(power(5, 1), 5)

if __name__ == '__main__':
    unittest.main()
    