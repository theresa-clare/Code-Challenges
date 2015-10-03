"""
K'th largest element in BST when modification to BST is not allowed

Given a Binary Search Tree and a positive integer k, find the kth largest element 
in the BST

http://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/
"""

def kth_largest_in_BST(root, k, count=0):
	if root is None or count >= k:
		return

	kth_largest_in_BST(root.right, k, count)
	
	count += 1
	if count == k:
		print "%s'th largest element is %s" % k, str(root.data)

	kth_largest_in_BST(root.left, k, count)