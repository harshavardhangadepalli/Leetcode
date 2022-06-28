class Solution:
	def isSymmetric(self,root):
		def recursion(node1,node2):
			if not node1 and not node2:
				return True
			if not node1 or not node2:
				return False
			if node1.val!=node2.val:
				return False
			return recursion(node1.left,node2.right) and recursion(node1.right,node2.left)
		return recursion(root.left,root.right)
