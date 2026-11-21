
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0,0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 4), -4)
        self.assertEqual(sub(-2, -2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), -12)
        self.assertEqual(multiply(7,6), 4)
        self.assertEqual(multiply(1,4), -3)

    def test_divide(self):
        self.assertEqual(divide(1,4), -3)
        self.assertEqual(divide(7,12), 6)
        with self.assertRaises(ZeroDivisionError):
            divide(0,7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(5, 1), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 5)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()