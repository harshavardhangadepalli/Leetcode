class Solution:
	def numDecodings(self,s):
		d = dict()
		def recursion(strs):
			if strs in d:
				return d[strs]
			if len(strs)==0:
				return 1
			ways = 0
			if 1<= int(strs[0]) <= 9:
				ways += recursion(strs[1:])
			if len(strs) > 1 and 10 <= int(strs[0] + strs[1]) <= 26:
				ways += recursion(strs[2:])
			d[strs] = ways
			return ways
		return recursion(s)