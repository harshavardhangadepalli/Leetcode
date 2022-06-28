class Solution:
	def groupAnagrams(self,strs):
		 l = list()
		 d = dict()
		 l1 = list()
		 for item in strs:
		 	l.append(''.join(sorted(item)))
		 for i in range(len(l)):
		 	if l[i] in d:
		 		d[l[i]].append(i)
		 	else:
		 		d[l[i]] = [i]
		 for item in d:
		 	tmp = []
		 	for place in d[item]:
		 		tmp.append(strs[place])
		 	l1.append(tmp)
		 return l1


s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])