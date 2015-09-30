"""
Union and Intersection of Two Linked Lists

Given two linked lists, create union and intersection lists that the union
and intersection of the elements present in the given lists. Order of 
elements doesn't matter

Input:
	list 1:		10 -> 15 -> 4 -> 20
	list 2: 	8 -> 4 -> 2 -> 10

Output:
	intersection:	4 -> 10
	union:			2 -> 8 -> 20 -> 4 -> 15 -> 10

http://www.geeksforgeeks.org/union-and-intersection-of-two-linked-lists/
"""

from linkedlist import *

def union_intersection_ll(ll1, ll2):
	"""
	Returns the union and intersection of two linked lists 

	>>> ll1 = LinkedList()
	>>> ll1.data_to_list([10, 15, 4, 20])
	>>> ll2 = LinkedList()
	>>> ll2.data_to_list([8, 4, 2, 10])
	>>> union_intersection_ll(ll1, ll2)
	(LinkedList([10, 4]), LinkedList([2, 8, 20, 4, 15, 10]))
	"""

	seen = set()
	intersection = LinkedList()
	union = LinkedList()

	# traverse first linked list and add data to seen set
	current = ll1.head
	while current != None:
		seen.add(current.data)
		union.insert(current.data)
		current = current.next

	# traverse second linked list and check if data was seen already
	current  = ll2.head
	while current != None:
		if current.data in seen:
			intersection.insert(current.data)
		else:
			union.insert(current.data)
		current = current.next

	return intersection, union

# use merge sort on both linked lists, then traverse both lists for union & intersection
def MS_union_intersection_ll(ll1, ll2):
	# Will come back to complete this function
	pass

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()