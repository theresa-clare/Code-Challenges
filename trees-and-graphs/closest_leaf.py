"""
Find the closest leaf in a Binary Tree

Given a binary tree and a key 'k', find the distance of the closet leaf from 'k'

http://www.geeksforgeeks.org/find-closest-leaf-binary-tree/
"""

# utility function to return the minimum of x and y
def get_min(x, y):
	if x < y:
		return x
	else:
		return y

# utility function to find the distance of the closest leaf of the tree rooted
# under given root
def closest_down(root):
	if root is None:
		return None
	if root.left is None and root.right is None:
		return 0

	# return minimum of left and right, plus one
	return 1 + get_min(closest_down(root.left), closest_down(root.right))

# returns distance of closest leaf to a given key 'k'. The array 'ancestors_list'
# is used to keep track of ancestors of the current node and 'index' is used to 
# keep track of the current index in ancestors_list
def find_closest(root, k, ancestor_list, index):
	if root is None:
		return None

	if root.key == k:
		# find closest leaf under the subtree rooted with given key
		res = closest_down(root)

		# traverse all ancestors and update result if any parent node gives
		# smaller distance
		i = index - 1
		while i >= 0:
			res = get_min(res, index - i + closest_down(ancestor_list[i]))
			i -= 1

		return res

	# if key node is found, store current node and recur for left and
	# right children
	ancestor_list[index] = root

	return get_min(find_closest(root.left, k, ancestor_list, index+1), \
					find_closest(root.right, k, ancestor_list, index+1))

# wrapper function
def find_closest_wrapper(root, k):
	ancestor_list = []*100 # Assume maximum height of tree is 100
	return find_closest(root, k, ancestor_list, 0)