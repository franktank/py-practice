"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""

# What do I do if there are multiple duplicates -> have to check combinations
# Set of indices with same value
import collections
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: boolx`
        """
        num_indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            num_indices[num].append(i)
            if len(num_indices) >= 2:
                # Check all combinations of indices pairs s.t |i - j| <= k
                for j, ele in enumerate(num_indices[num]):
                    if i == ele:
                        continue
                    else:
                        if abs(i - ele) <= k:
                            return True
        return False
