"""
Count BST nodes that lie in a given range

Given a Binary Seart Tree and a range, count number of nodes that lie in a given range

http://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/
"""

def count_nodes_in_range(root, low, high):
	if root is None:
		return 0

	if root.data == high and root.data == low:
		return 1

	if low <= root.data <= high:
		return 1 + count_nodes_in_range(root.left, low, high) + \
					count_nodes_in_range(root.right, low, high)

	elif root.data < low:
		return count_nodes_in_range(root.right, low, high)

	else:
		return count_nodes_in_range(root.left, low, high)