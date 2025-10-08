import unittest
from prog.countc import countc


class Count_c_Test(unittest.TestCase):
    def test_simple(self):
        s: str = "ayin mannani"
        c: str = "n"
        result: int = 4
        self.assertEqual(countc(s, c), result)

    def test_nothing(self):
        s: str = ""
        c: str = "n"
        result: int = 0
        self.assertEqual(countc(s, c), result)

    def test_not_existence(self):
        s: str = "ayin mannani"
        c: str = "x"
        result: int = 0
        self.assertEqual(countc(s, c), result)


if __name__ == "__main__":
    unittest.main()
