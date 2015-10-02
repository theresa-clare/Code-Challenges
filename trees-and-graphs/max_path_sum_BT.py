"""
Maximum Path Sum in a Binary Tree

Given a binary tree, find the maximum path sum. The path may start and end at
any node in the tree.

http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

----

For each node, there can be four ways that the max path goes through the node:
1) Node only
2) Max path through Left Child + Node
3) Node + Max path through Right Child
4) Max path through Left Child + Node + Max path through Right Child
"""

def max_path_sum_BT(root, res):
	# base case
	if root is None:
		return 0

	# l and r store maximum path sum going through left and right child of root
	l = max_path_sum_BT(root.left, res)
	r = max_path_sum_BT(root.right, res)

	# max path for parent call of root; this path must include at most one child
	max_single = max(max(l,r) + root.data, root.data)

	# max top represents the sume where the node under consideration is the root
	# of the maxsum path and no ancestors of root are there in max sum path
	max_top = max(max_single, l + r + root.data)

	# store max result
	res = max(res, max_top)

	return max_single

def max_path_sum_BT_wrapper(root):
	res = 0 # INT_MIN in C++?

	max_path_sum_BT(root, res)
	return res
	# check scope of res