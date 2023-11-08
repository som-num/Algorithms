import graphviz

# Creating tree nodes
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing Huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# User input for the string
string = input("Enter a string: ")

# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

total_bits_of_frequency = sum(frequency * 8 for char, frequency in freq)
total_size_of_characters = 0

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    total_size_of_characters += (c1 + c2) * len(huffman_code_tree(node))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print('\n Char | Frequency | Huffman code | Size (bits)')
print('----------------------------------------------')
char_total = 0
for (char, frequency) in freq:
    
    char_size = frequency * len(huffmanCode[char])
    print('  %-2s  |    %-6s  |%12s   |   %-6s' % (char, frequency, huffmanCode[char], char_size))
    char_total += char_size

print(f"\nTotal Bits of Frequency: {total_bits_of_frequency}")
print(f"Total Size of Characters: {char_total}")
savings = total_bits_of_frequency - char_total
print(f"Savings: {savings} bits")

def generate_dot_file(node, dot, parent_node=None):
    if type(node) is str:
        dot.node(node)
        if parent_node:
            dot.edge(parent_node, node)
    else:
        left, right = node.children()
        dot.node(str(node))
        if parent_node:
            dot.edge(parent_node, str(node))
        generate_dot_file(left, dot, str(node))
        generate_dot_file(right, dot, str(node))

# Generate a DOT file and render the Huffman code tree
dot = graphviz.Digraph(comment='Huffman Code Tree')
generate_dot_file(nodes[0][0], dot)
dot.render('huffman_code_tree', view=True)
