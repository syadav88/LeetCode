class LinkedNode:
	def __init__(self, node):
		self.value = node
		self.next = None

	def reverseLinkedList(self, head):
		prev = None
	    while head:
	        curr = head
	        head = head.next
	        curr.next = prev
	        prev = curr
	    return prev

	def reverseList(self, head):
    return self._reverse(head)

	def _reverse(self, node, prev=None):
	    if not node:
	        return prev
	    n = node.next
	    node.next = prev
	    return self._reverse(n, node)
