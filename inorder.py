class Solution:
	def inorderTraversal(self,root):
		l = list()
		def recursion(root):
			if root == None:
				return
			recursion(root.left)
			l.append(root.val)
			recursion(root.right)
		recursion(root)
		return l