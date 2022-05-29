from random import randrange

class Node(object):
    def __init__(self, value: int = None):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self) -> str:
        return self.__str__()

def generate_tree(levels: int) -> Node:
    if levels == 0:
        return None
    node = Node(randrange(50))
    node.left = generate_tree(levels-1)
    node.right = generate_tree(levels-1)
    return node

def print_tree(node: Node, level: int = 0):
    if node is None:
        return
    print_tree(node.right, level+1)
    print('  ' * level, end='')
    print(node)
    print_tree(node.left, level+1)

def invert_tree(node: Node) -> Node:
    if node is None:
        return
    left_inverted = invert_tree(node.left)
    right_inverted = invert_tree(node.right)
    node.right = left_inverted
    node.left = right_inverted
    return node


tree = generate_tree(3)
print_tree(tree)
print("---------")
inverted = invert_tree(tree)
print_tree(inverted)