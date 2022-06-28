class Solution:
    def myPow(self, x, n):
        return pow(x, n)
        if n < 0:
            return 1/self.recursion(x, abs(n))
        return self.recursion(x, n)

    def recursion(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        a = self.recursion(x, n//2)
        if n % 2 == 0:
            return a*a
        return a*a*x


s = Solution()
a = s.myPow(2, 30)
print(s.myPow(2, a))
