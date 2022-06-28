class Solution:
	def merge(self,nums1,m,nums2,n):
		i=0
		while i<m and len(nums2)>0:
			if nums1[i]>nums2[0]:
				i+=1
			else:
				nums1[i+1:] = nums1[i:len(nums1)-1]
				nums1[i] = nums2.pop(0)
				m+=1
		if m!=m+n:
			nums1[m:] = nums2
		nums1.sort()