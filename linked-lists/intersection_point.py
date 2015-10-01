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

if __name__ == "__main__":
	import doctest
	doctest.testmod()