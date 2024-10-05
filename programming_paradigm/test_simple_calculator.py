import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 7), 10)
        self.assertEqual(self.calc.add(-3, -7), -10)
        self.assertEqual(self.calc.add(-3, 7), 4)
        self.assertEqual(self.calc.add(0, 0), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 7), 3)
        self.assertEqual(self.calc.subtract(-10, -7), -3)
        self.assertEqual(self.calc.subtract(-10, 7), -17)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-3, 7), -21)
        self.assertEqual(self.calc.multiply(0, 7), 0)
        self.assertEqual(self.calc.multiply(-3, -7), 21)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
if __name__ == '__main__':
    unittest.main()
