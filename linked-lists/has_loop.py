"""
Given a linked list, check to see if the list contains a loop.
Returns True if there is a loop; returns False otherwise
"""

def has_loop(ll):
	if ll is None:
		return False

	slow = ll.head
	fast = ll.head

	while slow != None or fast != None:
		slow = slow.next

		if fast.next != None:
			fast = fast.next.next
		else:
			return False

		if slow == fast:
			return True

	return False