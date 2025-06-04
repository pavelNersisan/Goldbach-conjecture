import unittest
# Adjust the import path based on how we'll run the tests.
# If tests are run from the root directory, 'from pymath.lib import ...' is correct.
from pymath.lib import gcd, lcm, factorial

class TestMathLib(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(18, 48), 6)
        self.assertEqual(gcd(17, 5), 1) # Prime numbers
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(10, -5), 5)
        self.assertEqual(gcd(-10, 5), 5)
        self.assertEqual(gcd(-10, -5), 5)
        self.assertEqual(gcd(7, 7), 7)

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(6, 4), 12)
        self.assertEqual(lcm(5, 7), 35) # Prime numbers
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 0), 0)
        self.assertEqual(lcm(10, 1), 10)
        self.assertEqual(lcm(1, 10), 10)
        self.assertEqual(lcm(10, -5), 10) # abs values are used
        self.assertEqual(lcm(-10, 5), 10)
        self.assertEqual(lcm(-10, -5), 10)
        self.assertEqual(lcm(7,7), 7)


    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == '__main__':
    # This allows running the tests directly from this file: python pymath/tests/test_lib.py
    # To run with test discovery (e.g., python -m unittest discover):
    # Ensure this file is named test_*.py and is in a package.
    unittest.main()
