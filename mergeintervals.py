class Solution:
	def merge(self,intervals):
		intervals.sort()
		i=0
		while i<len(intervals):
			if i+1 == len(intervals):
				break
			if self.overlap(intervals[i],intervals[i+1]):
				a = intervals[i]+intervals[i+1]
				intervals.pop(i)
				intervals.pop(i)
				intervals.insert(i,[min(a),max(a)])
				i-=1
			i+=1
		return intervals
	def overlap(self,a,b):
		if a[0] == b[0] or a[1] == b[1] or a[1]>b[0] or a[1]==b[0]:
			return True
		return False

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))