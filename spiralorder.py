class Solution:
	def spiralOrder(self,matrix):
		visited = dict()
		ordered = list()
		count = 0
		m = len(matrix)
		n = len(matrix[0])
		n_ele = m*n
		i=0
		j=0
		ordered.append(matrix[0][0])
		for x in range(m):
			for y in range(n):
				visited[x,y] = False
		visited[0,0] = True
		count = 1

		operation = 'right'
		while(count < n_ele):
			i,j,visited,ordered,count,operation = self.visitor(matrix,m,n,i,j,visited,ordered,count,operation)
		return ordered
	def visitor(self,matrix,m,n,i,j,visited,ordered,count,operation):
		
		#check if right exists:
		if(operation=='right'):
			if j+1 < n:
				if visited[i,j+1] == False:
					ordered.append(matrix[i][j+1])
					visited[i,j+1] = True
					count+=1
					j+=1
					return i,j,visited,ordered,count,operation
			operation = 'down'
			return i,j,visited,ordered,count,operation

		#check if down exists:
		if(operation == 'down'):
			if i+1 < m:
				if visited[i+1,j] == False:
					ordered.append(matrix[i+1][j])
					visited[i+1,j] = True
					count+=1
					i+=1
					return i,j,visited,ordered,count,operation
			operation = 'left'
			return i,j,visited,ordered,count,operation

		#check if left exits:
		if(operation == 'left'):
			if j-1 >= 0:
				if visited[i,j-1] == False:
					ordered.append(matrix[i][j-1])
					visited[i,j-1] = True
					count+=1
					j-=1
					return i,j,visited,ordered,count,operation
			operation = 'up'
			return i,j,visited,ordered,count,operation
		if(operation=='up'):
			if i-1 >= 0:
				if visited[i-1,j] == False:
					ordered.append(matrix[i-1][j])
					visited[i-1,j] = True
					count+=1
					i-=1
					return i,j,visited,ordered,count,operation
			operation='right'
			return i,j,visited,ordered,count,operation
		return i,j,visited,ordered,count,operation


s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
