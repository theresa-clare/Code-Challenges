"""
Cracking the Coding Interview v5: Exercise 4.1

Implement a function to check if a binary tree is balanced. For the purpose of this question,
a balanced tree is defined to be a tree such that the height of the two subtrees of any node
never differ by more than one.
"""

def depth(node):
	if node == None:
		return 0

	return max(depth(node.left), depth(node.right)) + 1

def is_balanced(node):
	if node is None:
		return True

	if abs(depth(node.left) - depth(node.right)) > 1:
		return False

	if is_balanced(node.left) and is_balanced(node.right):
		return True
	return False