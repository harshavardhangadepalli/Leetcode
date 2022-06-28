class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while(l < r):
            if l + 1 == r:
                if nums[l] > nums[r]:
                    return l
                else:
                    return r
            mid = l + (r-l)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return l