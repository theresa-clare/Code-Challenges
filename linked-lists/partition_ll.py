""" 
Cracking the Coding Interview v5: Exercise 2.4

Write code to partition a linked list around a value x, such that all nodes less than x
come before all nodes greater than or equal to x
"""

# my initial solution
def partition_ll(node, x):
	new_ll = LinkedList(node,node)
	node = node.next

	while node != None:
		new_node = Node(node.data)
		if new_node.data >= x:
			new_ll.tail.next = new_node
			new_ll.tail = new_node
		else:
			new_node.next = new_ll.head
			new_ll.head = new_node

	return new_ll


#################################################################################################################################################

# Cracking the Coding Interview solutions

""" Solution 1: Create two different linked lists: one for elements less than x, one for elements greater than x. Merge together in the end
	- mostly "stable" in that elements stay in their original order """

def partition(node, x):
	before_start = None
	before_end = None
	after_start = None
	after_end = None

	while node != None:
		next = node.next
		node.next = None
		if node.data > x:
			if before_start == None:
				before_start = node
				before_end = before_start
			else:
				before_end.next = node
				before_end = node
		else:
			if after_start == None:
				after_start = node
				after_end = after_start
			else:
				after_end.next = node
				after_end = node
		node = node.next

	if before_start == None:
		return after_start

	before_end.next = after_start
	return before_start

""" Solution 2: Rearrange elemets by inserting element at either head or tail
	- does not keep order """


def partition(node, x):
	head = node
	tail = node

	while node != None:
		next = node.next
		if node.data < x:
			node.next = head
			head = node
		else:
			tail.next = node
			tail = node
		node = next

	tail.next = None

	return head
