#https://github.com/gabrielmartinez640/Lab11-ACS-GMC
#Partner 1: Gabriel Martinez
#Partner 2: Arianna Casanova-Silva

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0,0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(mul(4,3), 12)
        self.assertEqual(mul(5,-2), -10)
        self.assertEqual(mul(7,0), 0)

    def test_divide(self):
        self.assertEqual(div(2,10), 5)
        self.assertEqual(div(3,1), 1/3)
        with self.assertRaises(ZeroDivisionError):
            div(0,7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)


    def test_log_invalid_exponent(self):
        with self.assertRaises(ValueError):
            logarithm(2,0)
        with self.assertRaises(ValueError):
            logarithm(2,-8)
        with self.assertRaises(ValueError):
            logarithm(1,8)
        with self.assertRaises(ValueError):
            logarithm(-2,8)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(-3,-4), 5)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.41421356, places = 5)

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), 1.41421356, places = 5)
        with self.assertRaises(ValueError):
            square_root(-2)



if __name__ == "__main__":
    unittest.main()