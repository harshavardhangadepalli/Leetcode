class Solution:
	def exist(self,board,word):
		l = list()
		d = dict()
		for i in range(len(board)):
			for j in range(len(board[0])):
				d[i,j] = False
				if board[i][j]==word[0]:
					l.append([i,j])
		for occurance in l:
			if self.recursion(occurance[0],occurance[1],0,board,word,hasher=d):
				return True
		return False

	def recursion(self,row,col,index,board,word,hasher):
		if index==len(word):
			return True
		if row>=len(board) or col>=len(board[0]) or row<0 or col<0:
			return False
		if hasher[row,col]==True:
			return False
		if board[row][col]!=word[index]:
			return False

		hasher[row,col] = True
		if(self.recursion(row+1,col,index+1,board,word,hasher) or self.recursion(row,col+1,index+1,board,word,hasher) or self.recursion(row-1,col,index+1,board,word,hasher) or self.recursion(row,col-1,index+1,board,word,hasher)):
			return True
		hasher[row,col]=False
		return False
s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))