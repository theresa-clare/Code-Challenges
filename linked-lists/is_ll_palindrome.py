""" 
Cracking the Coding Interview v5: Exercise 2.7

Implement a function to check if a linked list is a palindrome
"""

# naive solution

from linkedlist import *
from is_palindrome import is_palindrome

def is_ll_palindrome(ll):
	data_list = ll.list_to_data()

	return is_palindrome(data_list)


#################################################################################################################################################

# Cracking the Coding Interview:

""" Solution 1: Reverse and Compare
	- reverse the linked list
	- compare (first halves of the) reversed list to original
		- if they're the same, lists are identical """

def is_palindrome_ctci_v1(ll):
	pass
	# Will return to complete this function

""" Solution 2: Iterative Approach 
	- reverse front half of the list and using a stack
	- iterate through first half of elements and push first half of the elements to a stack
		- use fast runner / slow runner technique
		- push data from slow runner to stack until fast runner hits end of list
		( stack will have all elements from front of list in reverse order )
	- iterate through rest of list 
		- compare node to top of stack
		- if we complete the iteration without finding a difference, then linked list is palindrome
"""

def is_palindrome(head):
	fast = head
	slow = head

	stack = Stack()

	while fast != None and fast.next != None:
		stack.push(slow.data)
		slow = slow.next
		fast = fast.next.next

	# has odd number of elements, so skip the middle element
	if fast != None:
		slow = slow.next

	while slow != None:
		top = stack.pop()

		if top != slow.data:
			return False

		slow = slow.next

	return True

""" Solution 3: Recursive Approach
	- utilize the notation Kx:
		- K = the value of the node data
		- x = (which is either f or b) indicates whether we are referring to the front node with that value or the back node
"""

def is_palindrome_ctci_v3(head):
	pass
	# Will return to complete this function

