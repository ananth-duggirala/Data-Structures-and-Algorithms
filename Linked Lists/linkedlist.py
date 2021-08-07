class Node:
	def __init__(self, val = None):
		self.val = val
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None

ll = SinglyLinkedList()
ll.head = Node(1)
node2 = Node(2)
node3 = Node(3)

ll.head.next = node2
node2.next = node3