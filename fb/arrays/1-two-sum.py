"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        d[nums[0]] = 0
        res = []
        for i in range(1,len(nums)):
            if target - nums[i] in d:
                res.append(i)
                res.append(d[target-nums[i]])
            d[nums[i]] = i
        return res
