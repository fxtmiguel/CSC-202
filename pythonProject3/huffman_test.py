import unittest
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq1(self):
        freqs = cnt_freq("test1.txt")
        ans_list = [0] * 256
        ans_list[96:105] = [0, 2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqs[96:104], ans_list[96:104])

    def test_cnt_freq2(self):
        freqs = cnt_freq("test.txt")
        ans_list = [0] * 256
        ans_list[91:100] = [0, 0, 0, 0, 0, 0, 2, 4, 0]
        self.assertListEqual(freqs[91:100], ans_list[91:100])

    def test_create_huff_tree1(self):
        freqs = cnt_freq("test1.txt")
        hufftree = create_huff_tree(freqs)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)

    def test_create_huff_tree2(self):
        freqs = cnt_freq("test.txt")
        hufftree = create_huff_tree(freqs)
        self.assertEqual(hufftree.freq, 6)
        self.assertEqual(hufftree.char, 97)

    def test_create_code1(self):
        freqlist = cnt_freq("test1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('d')], '1')

    def test_create_code2(self):
        freqlist = cnt_freq("test.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '0')
        self.assertEqual(codes[ord('b')], '1')

    def test_create_empty(self):
        self.assertEqual(create_huff_tree([]), None)

    def test_textfile(self):
        huffman_encode("test2.txt", "test2_out.txt")
        self.assertTrue(compare_files("test2_out.txt", "test2_soln.txt"))

    def test_01_textfile(self):
        huffman_encode("test.txt", "test_out.txt")
        self.assertTrue(compare_files("test_out.txt", "test_soln.txt"))

    def test_empty_file(self):
        with open('empty_encoded.txt', 'w') as file:
            file.write('')
        freq_list = cnt_freq('empty.txt')
        expected_freq_list = [0] * 256
        self.assertEqual(freq_list, expected_freq_list)
        huffman_tree = create_huff_tree(freq_list)
        expected_huffman_tree = None
        self.assertEqual(huffman_tree, expected_huffman_tree)

    def test_create_header(self):
        freqlist = cnt_freq("test.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4")

    def test_create_header2(self) -> None:
        freqlist = cnt_freq("test2.txt")
        self.assertEqual(create_header(freqlist), "32 3 97 4 98 3 99 2 100 1")


if __name__ == '__main__':
    unittest.main()
