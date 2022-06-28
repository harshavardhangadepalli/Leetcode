class Solution:
    def maxProfit(self, prices):
        # d contains maximum till the index 'i' ( to the right)

        d = dict()
        d[len(prices)-1] = prices[-1]
        curr_max = prices[-1]
        for i in reversed(range(len(prices)-1)):
            if curr_max > prices[i]:
                d[i] = curr_max
            else:
                d[i] = prices[i]
                curr_max = prices[i]

        curr_max = d[0] - prices[0]
        for i in range(len(prices)):
            if d[i] - prices[i] >= curr_max:
                curr_max = d[i] - prices[i]
        if curr_max <= 0:
            return 0
        return curr_max

s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
