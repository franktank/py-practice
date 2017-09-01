"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
"""


# Brute Force
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_length = 0
        for i in range(0,len(nums)):
            curr_length = 0
            curr_sum = 0
            for j in range(i,len(nums)):
                curr_sum += nums[j]
                curr_length += 1
                if curr_sum > k:
                    break
                if curr_sum == k:
                    if curr_length > max_length:
                        max_length = curr_length
        return max_length

# DP-ish method of saving prefix sum
# Check prefix sum at j and then subtract prefix_sum at some index i
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Calculate the prefix sum
        prefix_sum = 0
        max_sub_len = -1
        prefix_sum_idx = dict()
        prefix_sum_idx[0] = -1 # for when prefix sum equals k
        for i, num in enumerate(nums):
            prefix_sum += num
            if ((prefix_sum - k) in prefix_sum_idx):
                max_sub_len = max(max_sub_len, i - map.get(prefix_sum - k))
            if (prefix_sum not in prefix_sum_idx):
                prefix_sum_idx[prefix_sum] = i

        return max_sub_len
