#!/usr/bin/env python3
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create an instance of SimpleCalculator before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, -8), 16)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertIsNone(self.calc.divide(0, 0))  # Division zero by zero edge case

if __name__ == "__main__":
    unittest.main()
