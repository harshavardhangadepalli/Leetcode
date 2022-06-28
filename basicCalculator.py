class Solution:
    def calculate(self, s):
        s = s.replace(" ","")
        stack = list()
        l = list()
        for i in s:
            if not i.isnumeric():
                temp = ''
                for item in stack:
                    temp+=item
                l.append(temp)
                stack = list()
                l.append(i)
            else:
                stack.append(i)
        tmp = ''
        for item in stack:
            tmp+=item
        l.append(tmp)

        while '/' in l:
            i = l.index('/')
            op1 = i-1
            op2 = i+1
            o = int(int(l[i-1])/int(l[i+1]))
            l = l[:i-1]+[str(o)]+l[i+2:]
        while '*' in l:
            i = l.index('*')
            op1 = i-1
            op2 = i+1
            o = int(int(l[i-1])*int(l[i+1]))
            l = l[:i-1]+[str(o)]+l[i+2:]
        while '-' in l:
            i = l.index('-')
            op1 = i-1
            op2 = i+1
            o = int(int(l[i-1])-int(l[i+1]))
            l = l[:i-1]+[str(o)]+l[i+2:]
        while '+' in l:
            i = l.index('+')
            op1 = i-1
            op2 = i+1
            o = int(int(l[i-1])+int(l[i+1]))
            l = l[:i-1]+[str(o)]+l[i+2:]
        return int(l[0])
s = Solution()
print(s.calculate("1+1+1"))