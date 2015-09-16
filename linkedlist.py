class Node(object):
	""" Singly linked list node representation """
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class LinkedList(object):
	""" Singly linked list implementation """

	def __init__(self, head=None):
		self.head = head

	# adds new node at the head of the linked list
	def insert(self, data):
		new = Node(data)
		new.next = self.head
		self.head = new

	def size(self):
		current = self.head
		count = 0

		while current != None:
			count += 1
			current = current.next

		return count

	def search(self, data):
		current = self.head

		while current != None:
			if current.data == data:
				return True

		return False

	def delete(self, data):
		current = self.head
		previous = None

		while current != None:
			if current.data == data:
				if previous == None: # at head of linked list
					self.head = current.next
				else:
					previous.next = current.next
				current.next = None # detatch node from linked list
			else:
				previous = current
				current = current.next

		raise ValueError("Data was not found in list")