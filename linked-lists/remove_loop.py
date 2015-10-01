"""
Given a linked list which contains a loop, return an uncycled linked list

http://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
"""

def remove_loop(ll):
	if ll is None:
		return None

	# detect loop using Floyd's Cycle detection algorithm
	slow = ll.head
	fast = ll.head

	while slow != fast:
		slow = slow.next
		fast = fast.next.next

	# count the number of nodes in loop (k)
	slow = slow.next
	k = 1

	while slow != fast:
		slow = slow.next
		k += 1

	# fix one pointer to the head and another to kth node from head
	head_pointer = ll.head
	k_pointer = ll.head

	while k > 0:
		k_pointer = k_pointer.next
		k -= 1

	# move both pointers at the same pace; they'll meet at the loop starting node
	previous_k_pointer = None

	while head_pointer != k_pointer:
		head_pointer = head_pointer.next
		previous_k_pointer = k_pointer
		k_pointer = k_pointer.next

	# get pointer to the last node of loop and make next of it as null
	previous_k_pointer.next = None
