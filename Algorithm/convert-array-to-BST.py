class BinarySearchTree:
	def __init__(self,root):
		self.value = root
		self.left = []
		self.right = []

	def convertArraytoBST(self, arr):
		arr = sorted(arr)
		if not root: return None

		mid = len(arr) // 2

        root = BinarySearchTree(arr[mid])
        root.left = self.convertArraytoBST(arr[:mid])
        root.right = self.convertArraytoBST(arr[mid+1:])

        return root