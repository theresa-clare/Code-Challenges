"""
Lowest Common Ancestory in a Binary Search Tree

Given values of two nodes in a Binary Search Tree, find the Lowest Common Ancestor.
You may assume that both the values exist in the tree.

Following is definition of LCA from Wikipedia:
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is 
defined as the lowest node in T that has both n1 and n2 as descendants (where we 
allow a node to be a descendant of itself).

The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest
from the root. Computation of lowest common ancestors may be useful, for instance, as 
part of a procedure for determining the distance between pairs of nodes in a tree: the 
distance from n1 to n2 can be computed as the distance from the root to n1, plus the 
distance from the root to n2, minus twice the distance from the root to their lowest 
common ancestor.

http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
"""

# Assumes both n1 and n2 are present in BST
def lowest_common_ancestor_BST(root, n1, n2):
	if root is None:
		return None

	if n1 < root.data < n2:
		return root
	# if both n1 and n2 are smaller than root, the LCA lies in the left
	elif root.data > n1 and root.data > n2:
		return lowest_common_ancestor_BST(root.left, n1, n2)
	# if both n1 and n2 are greater than root, the LCA lies in the right
	else:
		return lowest_common_ancestor_BST(root.right, n1, n2)