import unittest
from divide import divide


class DivideTest(unittest.TestCase):
    def test_division(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_zero_division(self):
        self.assertTrue("Error" in divide(5, 0))

    def value_error(self):
        self.assertTrue("Error" in divide("hello", 32))


if __name__ == "__main__":
    unittest.main()
