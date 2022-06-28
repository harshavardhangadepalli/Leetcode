class Solution:
    def generate(self, numRows):
        # numrows is the number of rows to be generated for pascal's triangle
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        l = [[1], [1, 1]]

        currentRow = 2
        while currentRow <= numRows - 1:
            temp = []
            temp.append(1)
            for i in range(len(l[currentRow-1])-1):
                temp.append(l[currentRow-1][i]+l[currentRow-1][i+1])
            temp.append(1)
            l.append(temp)
            currentRow += 1
        print(l)

s = Solution()
s.generate(5)