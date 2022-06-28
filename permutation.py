class Solution:
	def permute(self,nums):
		return self.recursion(nums)
	def recursion(self,nums):
		result=[]
		if len(nums) == 1:
			return [nums[:]]
		for i in range(len(nums)):
			n = nums.pop(0)
			perms = self.recursion(nums)
			for perm in perms:
				perm.append(n)
			print(perms)
			result.extend(perms)
			nums.append(n)
		return result
s = Solution()
print(s.permute([1,2,3]))