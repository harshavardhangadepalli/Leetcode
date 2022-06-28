class Solution:
	def countAndSay(self,n):
		if n==1:
			return "1"
		if n==2:
			return "11"
		else:
			thing = self.recursion(n-1)
			l = list()
			#now we need to count thing
			for i in range(len(thing)):
				if i==0:
					count = 1
					letter = thing[0]
				else:
					if letter == thing[i]:
						count+=1
						if i == len(thing)-1:
							l.append([str(count),str(letter)])
					else:
						l.append([str(count),str(letter)])
						count=1
						letter = thing[i]
						if i == len(thing)-1:
							l.append([str(count),str(letter)])
			final_num = ''
			for item in l:
				final_num+= str(item[0])+str(item[1])
			return final_num

s = Solution()
print(s.countAndSay(5))