"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# Brute Force
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i] + nums[j] == target:
                    res.add(i)
                    res.add(j)
        return list(res)

# Use Hash Map!
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_val = {}
        res = [None] * 2
        for i in range(len(nums)):
            if target-nums[i] in prev_val:
                res[0] = i
                res[1] = prev_val[target-nums[i]]
            else:
                prev_val[nums[i]] = i
        return res

# Bidirection Sweep
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
