import unittest
import bear_game


class TestCases(unittest.TestCase):
    def test_1(self):
        a = 84
        b = bear_game.bear(a)
        self.assertTrue(b)

    def test_2(self):
        a = 41
        b = bear_game.bear(a)
        self.assertFalse(b)

if __name__ == '__main__':
    unittest.main()