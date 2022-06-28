class Solution:
    def numIslands(self, grid):
        visited = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited[i,j] = False
        #now we have all the unvisited nodes
        def recursion(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return
            if visited[i,j] == True:
                return
            if grid[i][j] == '0':
                visited[i,j] = True
                return
            visited[i,j] = True
            recursion(i,j+1)
            recursion(i+1,j)
            recursion(i,j-1)
            recursion(i-1,j)
            #visit right
            #visit down
            #visit left
            #visit up
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i,j] == False and grid[i][j] == '1':
                    count+=1
                    recursion(i,j)
        return(count)

s = Solution()
print(s.numIslands([
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
    ]))