"""
Count BST subtrees that lie in a given range

Given a Binary Search Tree of integer values and a range [low, high], return the
count of nodes where nodes under that node (or subtree rooted with that node) lie
in a given range

http://www.geeksforgeeks.org/count-bst-subtrees-that-lie-in-given-range/
"""


def _count_subtrees_in_range(root, low, high, count):
	if root is None:
		return True

	l = _count_subtrees_in_range(root.left, low, high, count) if root.left else True
	r = _count_subtrees_in_range(root.right, low, high, count) if root.right else True

	if l and r and low <= root.data <= high:
		count[0] += 1
		return True

	return False

def count_subtrees_in_range(root, low, high):
	count = [0]
	_count_subtrees_in_range(root, low, high, count)
	return count[0]
