import unittest

import base_convert
import bear_game
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

    def test_3(self):
        a = 30
        b = 4
        b = base_convert.convert(a, b)
        c = "132"
        self.assertEqual(b, c)

    def test_4(self):
        a = 45
        b = 2
        b = base_convert.convert(a, b)
        c = "101101"
        self.assertEqual(b, c)

    def test_5(self):
        a = 84
        b = bear_game.bear(a)
        self.assertTrue(b)

    def test_6(self):
        a = 41
        b = bear_game.bear(a)
        self.assertFalse(b)