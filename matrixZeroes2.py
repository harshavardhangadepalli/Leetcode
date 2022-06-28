class Solution:
    def setZeroes(self, matrix):
        flag_row = 0
        # check whether first column must be made zero:
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                flag = 1
                break
        # now check if there are any columns in the row that are zero
        # if there is a zero in that row, we set the row[0] as 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    break

        # setting all columns as zero if there is a zero
        for j in range(1, len(matrix[0])):
            for i in range(len(matrix)):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        matrix[k][j] = 0

        # setting all rows as zero if there is a zero
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        # if flag is 1, set first column as 0
        if flag == 1:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        print(matrix)


s = Solution()
s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
