"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number_count = collections.defaultdict(lambda:0)
        for num in nums:
            number_count[num] += 1

        for key, value in number_count.items():
            if value != 2:
                return key
