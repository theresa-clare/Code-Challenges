"""
Write a function to get the intersection point of two linked lists.

There are two singly linked lists in a system. By some programming error, the
end node of one of the linked lists got linked to the second list, forming an
Y-shaped list. Write a program to get the point where the two linked lists merge.

Diagram with an intersection point at Node(15) can be viewed at: 
http://geeksforgeeks.org/wp-content/uploads/2009/10/Y-ShapedLinked-List.gif

http://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
"""

from linkedlist import *

# Accounts only for non-repetitive data between linked lists
def intersection_point(ll1, ll2):
	"""
	Given two linked lists, returns node at which they intersect

	>>> ll1 = LinkedList()
	>>> ll1.data_to_list([3, 6, 9, 15, 30])
	>>> ll2 = LinkedList()
	>>> ll2.data_to_list([10, 15, 30])
	>>> intersection_point(ll1, ll2)
	Node(15)
	"""

	seen = set()

	current = ll1.head
	while current != None:
		seen.add(current.data)
		current = current.next

	current = ll2.head
	while current != None:
		if current.data in seen:
			return current
		current = current.next

	return None

#########################################################################################

def intersection_point_v2(ll1, ll2):
	"""
	Returns intersection point of linked lists using two loops

	>>> ll3 = LinkedList()
	>>> ll3.data_to_list([1, 2, 3, 4, 5])
	>>> ll4 = LinkedList()
	>>> ll4.data_to_list([10, 4, 20, 35])
	>>> intersection_point_v2(ll3, ll4)
	Node(4)
	"""
	current1 = ll1.head
	current2 = ll2.head

	while current1 != None:
		while current2 != None:
			if current1.data == current2.data:
				return current1
			current2 = current2.next
		current2 = ll2.head
		current1 = current1.next

	return None

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()