class Solution:
    def maxProduct(self, nums):
        d = dict()
        for i in range(len(nums)):
            d[i,i] = nums[i]

        for i in range(2,len(nums)+1):
            # i will denote the size
            j = 0
            while j+i-1 < len(nums):
                d[j,j+i-1] = d[j,j+i-2] * d[j+i-1,j+i-1]
                j+=1
        return max(d)

s = Solution()
print(s.maxProduct([-2,0,-1]))