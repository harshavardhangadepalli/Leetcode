class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        d = [True] * n
        d[0] = d[1] = False
        for i in range(2,int(n**0.5)+1):
            if d[i] == True:
                # multiples of i should be marked as True
                # beginning from i*2 to the last number n, mark all multiples of i to be True.
                # the third parameter in the range() is used to jump steps
                for j in range(i*i,n,i):
                    d[j] = False
        # can also return sum(d)
        # slightly faster
        return d.count(True)

s = Solution()
print(s.countPrimes(5))