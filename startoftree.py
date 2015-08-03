

# treeMap = {}
# Root = Node(0, "Root")
# treeMap[Root.id] = Root
# for element in els:
#  nodeId, parentId, title = element
#  if not nodeId in treeMap:
#      treeMap[nodeId] = Node(nodeId, title)
#  else:
#      treeMap[nodeId].id = nodeId
#      treeMap[nodeId].title = title

#  if not parentId in treeMap:
#      treeMap[parentId] = Node(0, '')
#  treeMap[parentId].children.append(treeMap[nodeId])     

# def print_map(node, lvl=0):
#  for n in node.children:
#      print '    ' * lvl + n.title
#      if len(n.children) &gt; 0:
#          print_map(n, lvl+1)

# print_map(Root)


class Node: 
	def __init__(self, id, parent):
		self.id = id
		self.parent = parent
		self.children = []

	def addChild(self, node):
		self.children.append(node)

class :
	def __init__(self, root):
		self.tree = {}
		self.root = Node(root.id, root.parent)
		self.tree[root.id] = self.root

	def addNode(self, node):
		if not node.id in self.tree:
			self.tree[node.id] = Node(node.id, node.parent)
		self.tree[node.parent].addChild(self.tree[node.id])	

class Lattice:

	def __init__(self, dimension):
		self.dimension = dimension
		self.tree = Tree(Node((0,0), None))
		self.buildTree(self.tree.root)
	
	def buildTree(self, parent):
		if parent.id[0] < self.dimension:
			node = Node((parent.id[0] + 1, parent.id[1]), parent.id)
			self.tree.addNode(node)
			self.buildTree(node)
		if parent.id[1] < self.dimension:
			node = Node((parent.id[0], parent.id[1] + 1), parent.id)
			self.tree.addNode(node)
			self.buildTree(node)



def main():
	l = Lattice(2)
	for n in l.tree.root.children:
		

	# def print_map(node, lvl=0):
#  for n in node.children:
#      print '    ' * lvl + n.title
#      if len(n.children) &gt; 0:
#          print_map(n, lvl+1)

# print_map(Root)
if __name__=="__main__":
	main()



