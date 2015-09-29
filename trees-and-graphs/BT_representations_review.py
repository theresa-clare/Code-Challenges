######################################################################
#			 List of Lists Representation of Binary Trees			 #
######################################################################


def make_binary_tree(bt):
	return [bt, [], []]

def insert_left(root, new_branch):
	# if there is something in the second position, need to keep track of it
	# to push it down the tree as the left child of the list we are adding
	left_subtree = root.pop(1)

	if len(left_subtree) > 1:
		root.insert(1, [new_branch, left_subtree, []])
	else:
		root.insert(1, [new_branch, [], []])
	return root

def insert_right(root, new_branch):
	right_subtree = root.pop(2)

	if len(right_subtree) > 1:
		root.insert(2, [new_branch, [], right_subtree])
	else:
		root.insert(2, [new_branch, [], []])
	return root

def get_root_value(root):
	return root[0]

def set_root_value(root, new_value):
	root[0] = new_value

def get_left_subtree(root):
	return root[1]

def get_right_subtree(root):
	return root[2]


######################################################################
#		 Nodes and References Representation of Binary Trees		 #
######################################################################


class BinaryTree(object):
	def __init__(self, rootObj):
		self.key = rootObj
		self.left_subtree = None
		self.right_subtree = None

	def insert_left(self, new_node):
		if self.left_subtree == None:
			self.left_subtree = BinaryTree(new_node)
		else: # if there is an existing left child, push it down one level
			tree = BinaryTree(new_node)
			tree.left_subtree = self.left_subtree
			self.left_subtree = tree

	def insert_right(self, new_node):
		if self.right_subtree == None:
			self.right_subtree = BinaryTree(new_node)
		else:
			tree = BinaryTree(new_node)
			tree.right_subtree = self.right_subtree
			self.right_subtree = tree

	def get_root_value(self):
		return self.key

	def set_root_value(self, obj):
		self.key = obj

	def get_left_subtree(self):
		return self.left_subtree

	def get_right_subtree(self):
		return self.right_subtree