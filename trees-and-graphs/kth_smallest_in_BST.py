"""
Find the kth smallest element in BST (Order statistics in BST)

Given root of binary search tree and K as input, find Kth smallest element in BST

http://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
"""

# in order traversal using a stack
def kth_smallest_in_BST(root, k):
	to_visit = []
	current = root

	while current != None:
		to_visit.append(node)
		current = current.left

	count = 0

	while to_visit and count<k:
		current = to_visit.pop()
		count += 1
		right = current.right
		while right:
			stack.append(right)
			right = right.left

	return current.data

#########################################################################################

# in order traversal without additional data structure
def kth_smalles_in_BST(root, k, count=0):
	if root is None or c >= k:
		return

	kth_smallest_in_BST(root.left, k, c)
	
	count += 1
	if c == k:
		print "%s'th smallest element is %s" % k, str(root.data)

	kth_smallest_in_BST(root.right, k, c)