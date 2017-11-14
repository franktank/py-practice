"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # get duplicates next to each other
        res = []
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if start == 0 or not nums[start] == nums[start - 1]:
                    if start + end == target:
                        res.append([nums[i], nums[start], nums[end]])
                        while (start < end and not nums[start] == nums[start + 1]):
                            start += 1
                        while (start < end and not nums[end] == nums[end-1]):
                            end -= 1
                        start += 1
                        end -= 1
                    elif start + end < target:
                        start += 1
                    else:
                        end -= 1
        return res
