class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        front = 0
        for num in nums:
            if not num == 0:
                nums[front] = num
                front += 1
        for i in range(front, len(nums)):
            nums[i] = 0
        
