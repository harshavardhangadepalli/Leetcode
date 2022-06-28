class Solution:
	def sortColors(self,nums):
		c1 = 0
		c2 = 0
		c3 = 0
		for i in nums:
			if i==0:
				c1+=1
			if i==1:
				c2+=1
			if i==2:
				c3+=1
		for i in range(len(nums)):-
			if c1!=0:
				nums[i] = 0
				c1-=1
			else:
				if c2!=0:
					nums[i] = 1
					c2-=1
				else:
					if c3!=0:
						nums[i] = 2
						c3-=1
		print(nums)
s = Solution()
s.sortColors([2,0,2,1,1,0])