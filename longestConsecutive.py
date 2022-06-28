class Solution:
    def longestConsecutive(self, nums):
        def get_size(s,d,item):
            if item in d:
                return d[item]
            if item-1 not in s:
                return 1
            d[item] = 1 + get_size(s,d,item-1)
            return d[item]

        s = set(nums)
        d = dict()
        if len(s) == 1:
            return 1
        size = 0
        for item in s:
            curr_size = get_size(s,d,item)
            size = max(size,curr_size)
        return size


s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
