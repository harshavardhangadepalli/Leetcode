class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        if n < 5:
            return 0
        else:
            while n > 0:
                n = n//5
                count += n
        return count
s = Solution()
print(s.trailingZeroes(152))