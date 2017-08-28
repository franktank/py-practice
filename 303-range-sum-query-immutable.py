"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
"""
# Brute Force
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = 0
        for idx in range(i, j+1):
            sum += nums[idx]
        return sum


# Optimized using DP
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for index,num in enumerate(nums):
            if index == 0:
                continue
            nums[index] += nums[index - 1]
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]
