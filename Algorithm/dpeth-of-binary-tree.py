# Depth of Binary Tree

class Tree:
	def __init__(self, root, leftValue = [], rightValue = []):
		self.root = root
		self.leftNode = leftValue
		self.rightNode = rightValue

	def depth(self,root):
		if root is None:
			return 0
		else:
			return max(self.depth(root.leftNode) , self.depth(root.rightNode)) + 1


# This is a recursive function to find the depth of the binary tree.
# It checks if the root is None, then that means there exists no tree and hence the depth is 0. 
# But, if the root has some value, then the left node and right nodes are checked recursively and then the number accounting to maximum depth is returned