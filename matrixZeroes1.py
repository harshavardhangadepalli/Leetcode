class Solution:
	def setZeroes(self,matrix):
		rows = dict()
		cols = dict()
		for i in range(len(matrix)):
			for  j in  range(len(matrix[i])):
				if matrix[i][j] == 0:
					rows[i] = True
					cols[j] = True
		for row in rows:
			for j in range(len(matrix[row])):
				matrix[row][j] = 0

		for col in cols:
			for i in range(len(matrix)):
				matrix[i][col] = 0
		#print(matrix)
s = Solution()
s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])