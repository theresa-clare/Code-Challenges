def iterate_ll_backwards(head):
	"""
	Iterate through a linked list backwards. In this function, we'll print the
	data in the node, but this step could be replaced with other use cases

	>>> from linkedlist import *
	>>> ll_example = LinkedList()
	>>> ll_example.data_to_list([1,2,3,4])
	>>> iterate_ll_backwards(ll_example.head)
	4
	3
	2
	1
	"""
	if head is None:
		return

	iterate_ll_backwards(head.next)
	print head.data

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()