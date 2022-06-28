class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        remainder = k % len(nums)
        remainder = len(nums) - remainder
        l = nums[remainder::] + nums[0:remainder]
        for i in range(len(l)):
            nums[i] = l[i]