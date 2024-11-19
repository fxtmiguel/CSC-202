from huffman_writer import HuffmanBitWriter
from ordered_list import OrderedList


class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, HuffmanNode):
            return self.char == other.char and self.freq == other.freq \
                   and self.left == other.left and self.right == other.right
        return False

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.char < other.char
        return self.freq < other.freq

    def is_leaf(self):
        return not self.left and not self.right


def cnt_freq(filename):
    try:
        with open(filename, 'r') as file:
            freq = [0] * 256
            for char in file.read():
                index = ord(char)
                freq[index] += 1
        file.close()
        return freq
    except FileNotFoundError:
        raise FileNotFoundError


def create_huff_tree(list_of_freqs):
    freq_list = OrderedList()
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            n_node = HuffmanNode(i, list_of_freqs[i])
            freq_list.add(n_node)
    if freq_list.is_empty():
        return None
    while freq_list.size() > 1:
        a_node = freq_list.pop(0)
        b_node = freq_list.pop(0)
        freq_2 = a_node.freq + b_node.freq
        min_char = a_node.char < b_node.char
        if min_char is True:
            min_char = a_node.char
        else:
            min_char = b_node.char
        freq_list.add(HuffmanNode(min_char, freq_2, a_node, b_node))
        if freq_list.size() == 0:
            break

    return freq_list.pop(0)


def create_code(root_node: HuffmanNode):
    code_list = helper_create_code(root_node, '', [''] * 256)
    if not root_node:
        return []
    else:
        return code_list


def helper_create_code(root_node: HuffmanNode, code, list1):
    if root_node.left is None and root_node.right is None:
        list1[root_node.char] = code
        return list1

    helper_create_code(root_node.left, code + '0', list1)
    helper_create_code(root_node.right, code + '1', list1)

    return list1


def huffman_encode(in_file, out_file):
    try:
        freq_list = cnt_freq(in_file)
        codes = create_code(create_huff_tree(freq_list))
        header = create_header(freq_list)
        encoded = []
        chars_file = open(in_file, 'r')
        chars_lines = chars_file.readlines()
        for line in chars_lines:
            for char in line:
                encoded.append(codes[ord(char)])
        cmpfile = out_file.split('.')
        cmpfile.insert(1, '_compressed.')
        outcmp_file = open(out_file, 'w')
        outcmp_file.write(header + '\n' + ''.join(encoded))
        file = HuffmanBitWriter(''.join(cmpfile))
        file.write_str(header)
        file.write_code(''.join(encoded))
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError


def create_header(list_of_freqs):
    header = []
    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] > 0:
            header.append(str(i))
            header.append(str(list_of_freqs[i]))
    return ' '.join(header)


def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        while True:
            line1 = f1.readline().strip()
            line2 = f2.readline().strip()
            if line1 == '' and line2 == '':
                return True
            if line1 != line2:
                return False
