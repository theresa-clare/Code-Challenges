""" 
Cracking the Coding Interview v5: Exercise 2.3

Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node.

Input: the node c from the linked list a -> b -> c -> d -> e
Output: nothing is returned, but the new linked list looks like a -> b -> d -> e
"""

def delete_middle(node):
	if node.next != None: # Copy data from next node to current node, then delete next node
		node.data = node.next.data
		node.next = node.next.next
	else: # Node at the end; ask interviewer how to handle this case
		node.data = None