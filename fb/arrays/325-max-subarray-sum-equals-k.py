"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
"""
"""
Brute force approach, N^2, start at each index i and add from j = i+1 to len(nums) - 1 and see if any equals the k
"""
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        d = {}
        max_len = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == k:
                max_len = i + 1
            elif prefix_sum - k in d:
                max_len = max(max_len, i - d[prefix_sum - k])
            if prefix_sum not in d:
                d[prefix_sum] = i
        return max_len
