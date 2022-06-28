class Solution:
	def isSymmetric(self,root):
		q = list()
		def recursion(node1,node2):
			if node1 == None or if node2 == None:
				return
			if node1.val != node2.val:
				return False
			
