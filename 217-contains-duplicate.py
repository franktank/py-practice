"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

import collections
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_count = collections.defaultdict(lambda: 0)
        for num in nums:
            num_count[num] += 1
            if num_count[num] >= 2:
                return True

        return False
