import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2,-1),-3)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(-1,2),-3)
        self.assertEqual(self.calc.subtract(-2,-1),-1)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,3),15)
        self.assertEqual(self.calc.multiply(-1,2),-2)
        self.assertEqual(self.calc.multiply(-2,-1),2)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(-2,2),-1)
        self.assertEqual(self.calc.divide(-4,-1),4)
        self.assertEqual(self.calc.divide(8,0),None)