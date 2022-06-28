class Solution:
	def isValid(self,strs):
		stack = list()
		if strs=="":
			return False
		for c in strs:
			if len(stack)==0:
				if c ==')':
					return False
				else:
					stack.append(c)
			else:
				if stack[-1] == '(':
					if c == ')':
						stack.pop()
					else:
						stack.append(c)
				else:
					stack.append(c)
		if len(stack)==0:
			return True
		else:
			return False

	def dotProduct(self,a1,a2):
		l = list()
		if a2 == 1:
			return a1
		for item in a1:
			for thing in a2:
				element = item+thing
				l.append(element)
		return l

	def recursion(self,n1,n2,d):
		p = str(n1)+','+str(n2)
		if p in d:
			return d[p]
		#else, we return whatever
		#we need to add the two arrays that come from 1 opening and 1 closing brace
		if n1==0 and n2!=0:
			d[p] = self.dotProduct([')'],self.recursion(n1,n2-1,d))
			return d[p]
		if n1!=0 and n2==0:
			d[p] = self.dotProduct([')'],self.recursion(n1-1,n2,d))
			return d[p]
		#if both are not zero
		a = self.dotProduct(['('],self.recursion(n1-1,n2,d))
		b = self.dotProduct([')'],self.recursion(n1,n2-1,d))
		d[p] = a+b
		return a+b

	def generateParenthesis(self,n):
		d = dict()
		d[str(0)+','+str(0)] = []
		d[str(1)+','+str(0)] = ['(']
		d[str(0)+','+str(1)] = [')']
		d = self.recursion(n,n,d)
		#print(d)
		return d


sol = Solution()
l = sol.generateParenthesis(3)
l_new = list()
for i in l:
	if sol.isValid(i):
		l_new.append(i)
print(l_new)

#print(sol.dotProduct(['('],['())']))