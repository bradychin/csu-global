from build_tree import *
from build_frequency_table import *
from compress_data import *

def main():
    input_string = 'hello' #input('Enter message to encode: ')

    print('\nFrequency Table')
    frequency_table = build_frequency_table(input_string)
    print_frequency_table(frequency_table)

    print('\nHuffman codes')
    tree_root = huffman_build_tree(input_string)
    print_huffman_codes(tree_root)

    print('\nCompressed data')
    # print(huffman_compress(input_string))

    print('\nDecompressed coded data')

if __name__ == '__main__':
    main()