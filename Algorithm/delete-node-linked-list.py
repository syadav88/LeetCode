# Delete node in a linked list

class Node:
	def __init__(self,node):
		self.value = node
		self.next = None

	def deleteNode(self, node):
		node.value = node.next.value
		node.next = node.next.next

