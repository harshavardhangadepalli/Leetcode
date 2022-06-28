dp =dict()
dp[1] = 1
dp[0] = 1
class Solution(object):
	def uniquePaths(self, m, n):
		return int(self.fact(m+n-2) / (self.fact(m-1) * self.fact(n-1)))
	def fact(self,x):
		global dp
		if x in dp:
			return dp[x]
		dp[x] = x*self.fact(x-1)
		return dp[x]

s = Solution()
print(s.uniquePaths(3,3))