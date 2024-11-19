import unittest
import base_convert

class TestCases(unittest.TestCase):
    def test_1(self):
        a = 30
        b = 4
        b = base_convert.convert(a, b)
        c = "132"
        self.assertEqual(b, c)

    def test_2(self):
        a = 45
        b = 2
        b = base_convert.convert(a, b)
        c = "101101"
        self.assertEqual(b, c)

if __name__ == '__main__':
    unittest.main()