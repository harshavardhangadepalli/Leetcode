class Solution:
    def isHappy(self, n):
        d = set()
        x = n
        flag = False
        while True:
            if x in d:
                flag = True
                break
            summer = 0
            for char in str(x):
                summer += (int(char))**2
            if summer == 1:
                break
            d.add(x)
            x = int(summer)
        if not flag:
            return True
        return False

s = Solution()
if s.isHappy(19):
    print("yay")
else:
    print("nay")