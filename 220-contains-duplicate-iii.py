"""
Given an array of integers, find out whether there are two distinct indices i and j
in the array such that the absolute difference between nums[i] and nums[j]
is at most t and the absolute difference between i and j is at most k.
"""
# Brute Force Solution
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        index_num = dict()
        for i, num in enumerate(nums):
            index_num[i] = num
            for key, value in index_num.items():
                if i == key:
                    continue
                else:
                    if abs(num - value) <= t:
                        if abs(i - key) <= k:
                            return True
        return False

# Optimized Solution
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Bucket sort
        # Bucket size -> difference between
        if t < 0:
            return False
        buckets = dict()
        for i in xrange(len(nums)):
            bucket_key = nums[i] / (t+1)
            if bucket_key in buckets:
                return True
            # check adjacent buckets
            if bucket_key - 1 in buckets and abs(nums[i] - buckets[bucket_key - 1]) <= t:
                return True
            if bucket_key + 1 in buckets and abs(nums[i] - buckets[bucket_key + 1]) <= t:
                return True
            buckets[bucket_key] = nums[i]
            if i >= k:
                del buckets[nums[i-k] / (t+1)]
        return False
