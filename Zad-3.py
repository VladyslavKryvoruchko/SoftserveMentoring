class Node(object):
    def __init__(self, value: int = None):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self) -> str:
        return self.__str__()


left_leaf = Node(23)
right_leaf = Node(42)
root = Node(0)
root.left = left_leaf
root.right = right_leaf
tree = root 
counter = 0

def generate_tree(levels: int) -> Node:
    global counter
    if levels == 0:
        return None

    counter += 1
    node = Node(counter)
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

tree = generate_tree(3)
print_tree(tree)

def invert_tree(node: Node) -> Node:
    if node is None:
        return

    left_inverted = invert_tree(node.left)
    right_inverted = invert_tree(node.right)
    # Switch places for left and right
    node.right = left_inverted
    node.left = right_inverted
    return node

inverted = invert_tree(tree)
print_tree(inverted)