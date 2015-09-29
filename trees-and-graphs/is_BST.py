"""
Cracking the Coding Interview v5: Exercise 4.5

Implement a function to check if a binary tree is a binary search tree
"""


"""
Solution 1: In-Order Traversal
Keep track of last element we saw and compare it as we go

Note: the algorithm can't distinguish between two trees with duplicate values
	--> Assume unique values for in-order traversal
"""

previous = None

def is_BST(node):
	if node is None:
		return True

	if not is_BST(node.left):
		return False

	if previous != None and node.data <= previous:
		return False

	previous = node.data

	if not is_BST(node.right):
		return False

	return True


"""
Solution 2: The Min/Max Solution
Pass down min-max ranges to make sure ***all*** left nodes must be <= current node < all right nodes

Time: O(N) where N is the number of nodes in the tree
Space: O(log N) due to recursion up to the depth of the tree
"""
def is_BST_v2(node, min_num, max_num):
	if node is None:
		return True

	if (min_num != None and node.data <= min_num) or (max_num != None and node.data > max_num):
		return False

	if (not is_BST_v2(node.left, min_num, node.data)) or (not is_BST_v2(node.right, node.data, max_num)):
		return False

	return True

def is_BST_v2_wrapper(node):
	return is_BST_v2(node, None, None)