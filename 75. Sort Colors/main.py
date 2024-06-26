class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        for i in range(zero, len(nums)):
            if nums[i] == 1:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1