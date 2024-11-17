from build_frequency_table import *

class Node:
    def __init__(self, frequency):
        self.frequency = frequency

class LeafNode(Node):
    def __init__(self, frequency, character):
        super().__init__(frequency)
        self.character = character
        # self.frequency = frequency

class InternalNode(Node):
    def __init__(self, frequency_sum, left, right):
        super().__init__(frequency_sum)
        self.left = left
        self.right = right

class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def enqueue(self, node):
        self.nodes.append(node)
        self.nodes.sort(key=lambda x: x.frequency)

    def dequeue(self):
        return self.nodes.pop(0) if self.nodes else None

    def __len__(self):
        return len(self.nodes)

def huffman_build_tree(input_string):
    # Build frequency table
    table = build_frequency_table(input_string)

    # Make priority queue of nodes
    nodes = PriorityQueue()
    for char, freq in table.items():
        nodes.enqueue(LeafNode(freq, char))

    while len(nodes) > 1:
        left = nodes.dequeue()
        right = nodes.dequeue()
        # Make parent
        freq_sum = left.frequency + right.frequency
        parent = InternalNode(freq_sum, left, right)
        nodes.enqueue(parent)

    return nodes.dequeue()

# Function to print Huffman Codes from the tree
def print_huffman_codes(node, code=""):
    if isinstance(node, LeafNode):
        print(f"Character: {node.character}, Code: {code}")
    elif isinstance(node, InternalNode):
        # Traverse left and right with '0' and '1' for Huffman encoding
        print_huffman_codes(node.left, code + "0")
        print_huffman_codes(node.right, code + "1")

