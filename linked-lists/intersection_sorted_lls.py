"""
Intersection of Two Sorted Linked Lists

Given two lists sorted in increasing order, create and return a new list representing
the intersection of the two lists. The new list should be made with its own memory - 
the original lists should not be changed

Input:
	list 1:		1 -> 2 -> 3 -> 4 -> 6
	list 2: 	2 -> 4 -> 6 -> 8
Output:
	result:		2 -> 4 -> 6

http://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/
"""

from linkedlist import *

# Accounts for unique values in each linked list
def intersection_sorted_lls(ll1, ll2):
	"""
	Returns intersection of two sorted linked lists

	>>> ll1 = LinkedList()
	>>> ll1.data_to_list([1, 2, 3, 4, 6])
	>>> ll2 = LinkedList()
	>>> ll2.data_to_list([2, 4, 6, 8])
	>>> intersection_sorted_lls(ll1, ll2)
	LinkedList([2, 4, 6])
	"""
	current1 = ll1.head
	current2 = ll2.head
	intersection = LinkedList()

	while current1 != None and current2 != None:
		if current1.data == current2.data:
			intersection.insert(current1.data)
			current1 = current1.next
			current2 = current2.next
		elif current1.data > current2.data:
			current2 = current2.next
		else:
			current1 = current1.next

	# return reversed intersection since insert method adds new Node to beginning of LL
	intersection.reverse()
	return intersection

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()