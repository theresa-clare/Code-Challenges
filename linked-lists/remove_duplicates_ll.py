"""
Cracking the Coding Interview: Exercise 2.1

Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

# Time: O(n)
# Space: O(n)

def remove_duplicates(ll):
	"""
	Removes duplicates from an unsorted linked list

	>>> from linkedlist import *

	>>> ll_example = LinkedList()
	>>> ll_example.data_to_list([1,2,2,2,3,4,5,4])
	>>> ll_example_result = remove_duplicates(ll_example)
	>>> ll_example_result
	LinkedList([1, 2, 3, 4, 5])

	>>> ll_example2 = LinkedList()
	>>> ll_example2.data_to_list([1,2,3])
	>>> ll_example_result2 = remove_duplicates(ll_example2)
	>>> ll_example_result2
	LinkedList([1, 2, 3])

	>>> ll_example3 = LinkedList()
	>>> ll_example3.data_to_list([1,1,2,3])
	>>> ll_example_result3 = remove_duplicates(ll_example3)
	>>> ll_example_result3
	LinkedList([1, 2, 3])
	"""
	current = ll.head
	previous = None
	data_set = set()

	while current != None:
		if current.data in data_set:
			if previous == None:
				ll.head = current.next 
			else:
				previous.next = current.next
				current = previous.next
		else:
			data_set.add(current.data)
			next = current.next
			previous = current
			current = next

	return ll

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()