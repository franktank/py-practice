"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        start = 0
        end = 0
        cur_sum = 0
        min_len = sys.maxint
        for end in range(len(nums)):
            cur_sum += nums[end]
            while cur_sum >= s:
                min_len = min(min_len, end-start)
                cur_sum -= nums[start]
                start += 1
        if min_len == sys.maxint:
            return 0
        return min_len

# Equal to sum s
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        min_len = sys.maxint
        d = {}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == s:
                min_len = min(min_len, i + 1)
            elif prefix_sum - s in d:
                min_len = min(min_len, i - d[prefix_sum - s])
            if prefix_sum not in d:
                d[prefix_sum] = i
