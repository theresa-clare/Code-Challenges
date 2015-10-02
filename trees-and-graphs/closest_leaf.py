"""
Find the closest leaf in a Binary Tree

Given a binary tree and a key 'k', find the distance of the closet leaf from 'k'

http://www.geeksforgeeks.org/find-closest-leaf-binary-tree/
"""

def get_min(x, y):
	if x < y:
		return x
	else:
		return y

def closest_down(root):
	if root is None:
		return None
	if root.left is None and root.right is None:
		return 0

	return 1 + get_min(closest_down(root.left), closest_down(root.right))

def find_closest(root, k, ancestor_list, index):
	if root is None:
		return None

	if root.key == k:
		res = closest_down(root)
		i = index - 1

		while i >= 0:
			res = get_min(res, index - i + closest_down(ancestor_list[i]))
			i -= 1

		return res

	ancestor_list[index] = root

	return get_min(find_closest(root.left, k, ancestor_list, index+1), \
					find_closest(root.right, k, ancestor_list, index+1))

def find_closest_wrapper(root, k):
	ancestor_list = []
	return find_closest(root, k, ancestor_list, 0)