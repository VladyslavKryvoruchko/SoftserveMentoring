from cmath import nan


class Node(object): 
	
	def __init__(self, key): 
		self.key = key
		self.left = None
		self.right = None
	
	def __str__(self): 
		return f'{self.key}'
	
	def __repr__(self) -> str: 
		return self.__str__()

def findPath( root, path, k, dir):

	if root is None:
		return False

	path.append(dir)

	if root.key == k :
		return path

	if ((root.left != None and findPath(root.left, path, k, 'l')) or
			(root.right!= None and findPath(root.right, path, k, 'r'))):
		return path
	
	path.pop()
	return False
	

def findLCA(root, n1, n2):

	path1 = []
	path2 = []

	if (not findPath(root, path1, n1, None) or not findPath(root, path2, n2, None)):
		return -1

	i = 0
	while(i < len(path1) and i < len(path2)):
		if path1[i] != path2[i]:
			break
		i += 1
	
	new_path1 = ['up' for _ in path1[i:]]
	return new_path1+path2[i:]

def print_tree(node: Node, level: int = 0):
    if node is None:
        return
    print_tree(node.right, level+1)
    print('  ' * level, end='')
    print(node)
    print_tree(node.left, level+1)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_tree(root)

print (f"LCA(4, 5) = {findLCA(root, 4, 5)}")
print (f"LCA(4, 6) = {findLCA(root, 4, 6)}")
print (f"LCA(3,4) = {findLCA(root, 3,4)}")
print (f"LCA(2, 4) = {findLCA(root, 2, 4)}")