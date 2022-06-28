class Solution:
	def search(self,nums,target):
		start = 0
		end = len(nums)-1
		d = dict()
		print(self.recursion(nums,start,end,target,d))
	def recursion(self,nums,start,end,target,d):
		print(str(start)+","+str(end))
		if start>= end:
			return d
		mid = start+end//2
		if nums[mid] == target:
			d[0] = mid
		else:
			flag = True
		if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
			d[1] = mid
		else:
			flag = True
		if 0 in d and 1 in d:
			return d
		else:
			self.recursion(nums,start=start,end=mid,target=target,d=d)
			self.recursion(nums,start=mid+1,end=end,target=target,d=d)
		print(d)
		exit()
s = Solution()
s.search([4,5,6,7,0,1,2],2)