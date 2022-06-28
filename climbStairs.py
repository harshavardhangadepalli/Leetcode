class Solution:
	def climbStairs(self,n):
		dp = dict()
		dp[1] = 1
		dp[2] = 2
		dp[0] = 0
		return(self.recursion(n,dp))
	def recursion(self,n,dp):
		if n in dp:
			return dp[n]
		dp[n] = self.recursion(n-1,dp) + self.recursion(n-2,dp)
		return dp[n]
s = Solution()
s.climbStairs(5)