class Solution:
    def titleToNumber(self, columnTitle):
        i = 1
        d = dict()
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            d[letter] = i
            i+=1
        print(d)

s = Solution()
s.titleToNumber('av')