import unittest
import perm_gen_lex


class TestCases(unittest.TestCase):
    def test_1(self):
        a = 'mig'
        b = perm_gen_lex.perm_gen_lex(a)
        c = ['mig', 'mgi', 'img', 'igm', 'gmi', 'gim']
        self.assertEqual(b, c)

    def test_2(self):
        a = 'you'
        b = perm_gen_lex.perm_gen_lex(a)
        c = ['you', 'yuo', 'oyu', 'ouy', 'uyo', 'uoy']
        self.assertEqual(b, c)

if __name__ == '__main__':
    unittest.main()