class Solution:
	def isValidSudoku(self, board):
		def is_unique(arr):
			if len(arr) == len(set(arr)):
				return True
			return False
		rows = {}
		cols = {}
		subgrids = {}
		for i in range(len(board)):
			rows[i] = list()
			cols[i] = list()
			subgrids[i] = list()
		#for rows
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] != '.':
					rows[i].append(board[i][j])
		#for columns
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] != '.':
					cols[j].append(board[i][j])
		#for sub-grids:
		for j in range(0,3):
			for i in range(len(board)):
				if board[i][j]!='.':
					if i < 3:
						subgrids[0].append(board[i][j])
					elif i < 6:
						subgrids[3].append(board[i][j])
					else:
						subgrids[6].append(board[i][j])
		for j in range(3,6):
			for i in range(len(board)):
				if board[i][j]!='.':
					if i < 3:
						subgrids[1].append(board[i][j])
					elif i < 6:
						subgrids[4].append(board[i][j])
					else:
						subgrids[7].append(board[i][j])
		for j in range(6,9):
			for i in range(len(board)):
				if board[i][j]!='.':
					if i < 3:
						subgrids[2].append(board[i][j])
					elif i < 6:
						subgrids[5].append(board[i][j])
					else:
						subgrids[8].append(board[i][j])
		#for validity
		for i in rows:
			if not is_unique(rows[i]) or not is_unique(cols[i]) or not is_unique(subgrids[i]):
				# print("false")
				return False
		return True


s = Solution()
s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])


