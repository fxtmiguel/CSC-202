import unittest
from Linked_list import Stack


# Use the imports below to test either your array-based stack
# or your link-based version

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)


class TestLab3(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(8)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
