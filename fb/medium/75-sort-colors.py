"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
# Partition
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # partition with 0 and 1
        # put 0 at end
        if len(nums) == 1:
            return
        start = 0
        end = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = nums[len(nums)-1]
                nums[len(nums)-1] = 0
        nums, pidx = self.partition(nums, start, end)

        if pidx < len(nums) - 1: # potential for pidx to be len(nums) - 1 if only one kind in nums
            start = pidx + 1
        # put 1 at end
        for i in range(start, len(nums)):
            if nums[i] == 1:
                nums[i] = nums[len(nums)-1]
                nums[len(nums)-1] = 1
        nums, pidx = self.partition(nums, start, end)

    def partition(self, nums, start, end):
        i = start
        for j in range(start, end):
            if nums[j] <= nums[end]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
        temp = nums[i]
        nums[i] = nums[end]
        nums[end] = temp
        return nums, i

# Count
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zc = 0
        oc = 0
        tc = 0
        for num in nums:
            if num == 0:
                zc += 1
            elif num == 1:
                oc += 1
            else:
                tc += 1

        for i in range(zc):
            nums[i] = 0
        for i in range(zc, zc + oc):
            nums[i] = 1
        for i in range(zc + oc, zc + oc + tc):
            nums[i] = 2

"""
Two ways to solve:
Partition with 0 and partition with 1 or Count number 0s, 1s, and 2s
"""
