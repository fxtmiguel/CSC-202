import unittest
from linked_test import Queue


class TestLab(unittest.TestCase):
    def test_queue_1(self):
        q = Queue(9)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue('item_1')
        q.enqueue('item_2')
        q.dequeue()
        self.assertEqual(q.size(), 1)

    def test_queue_2(self):
        q = Queue(2)
        q.enqueue("work")
        q.enqueue("more")
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        q.dequeue()
        self.assertEqual(q.size(), 1)


if __name__ == '__main__':
    unittest.main()
