""" 
Cracking the Coding Interview: Exercise 2.2

Implement an algorithm to find the kth to last element of a singly linked list. 
"""

# Time: O(n)
# Space: O(1)

def k_to_last(node, k):
	"""
	Finds and returns the kth to last element

	>>> from linkedlist import *

	>>> ll_example = LinkedList()
	>>> ll_example.data_to_list([1,2,3,4,5,6,7,8,9,10])
	>>> ll_example_result = k_to_last(ll_example.head, 3)
	>>> ll_example_result
	Node(8)

	>>> ll_example2 = LinkedList()
	>>> ll_example2.data_to_list([1,2,3,4])
	>>> ll_example_result2 = k_to_last(ll_example2.head, 6)
	>>> ll_example_result2
	"""
	i = node
	j = node
	counter = 0

	while j != None:
		j = j.next
		counter += 1
		if counter > k:
			i = i.next

	if counter < k:
		return None
	return i

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()