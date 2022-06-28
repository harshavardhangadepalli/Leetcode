class Solution:
	def subsets(self,nums):
		subsets_list = []
		def recursion(subset=[],index=0):
			if index == len(nums):
				subsets_list.append(subset)
				return
			recursion(subset+[nums[index]],index+1)
			recursion(subset,index+1)
		recursion()
		return subsets_list


s = Solution()
print(s.subsets([1,2,3]))
