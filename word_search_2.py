flag = False
class Solution:
	def exist(self,board,word):
		global flag
		def recursion(row=0,col=0,index=0,result='',hasher=dict()):
			global flag
			if row<0 or row>=len(board) or col<0 or col>=len(board[0]):
				return
			if result==word:
				flag = True
				return
			if hasher[row,col] == True:
				return
			if flag==True:
				return
			if len(result) == len(word):
				return
			if word[index]!=board[row][col]:
				return
			result+=board[row][col]
			index+=1
			hasher[row,col] = True
			#right,left,up,down
			recursion(row,col+1,index,result,hasher)
			recursion(row,col-1,index,result,hasher)
			recursion(row+1,col,index,result,hasher)
			recursion(row-1,col,index,result,hasher)
			hasher[row,col] = False
			return
		def get_hasher():
			d = dict()
			for x in range(len(board)):
				for  y in range(len(board[0])):
					d[x,y] = False
			return d

		flag=False
		if len(board)==1:
			if len(board[0])==1:
				if word==board[0][0]:
					return True
		for i in range(len(board)):
			for j in range(len(board[0])):
				d1 = get_hasher()
				recursion(row=i,col=j,result='',hasher=d1)
		return flag