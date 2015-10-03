"""
Sorted Linked List to Balanced BST

Given a singly linked list which has data members sorted in ascending order, 
construct a balanced binary search tree which has the same data members as 
the given linked list

http://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/
"""

def count_nodes(head):
	current = head
	count = 0

	while current != None:
		count += 1
		current = current.next

	return count

def _sorted_ll_to_BST(head, n):
	if n <= 0:
		return None

	root = Node(head.data)
	root.left = _sorted_ll_to_BST(head, n/2)

	head = head.next
	root.right = _sorted_ll_to_BST(head, n-n/2-1)

	return root

def sorted_ll_to_BST(head):
	n = count_nodes(head)
	return _sorted_ll_to_BST(head, n)