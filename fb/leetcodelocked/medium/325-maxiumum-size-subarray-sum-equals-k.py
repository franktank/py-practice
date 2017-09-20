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
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = {}
        max_len = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == k:
                # Summing from [0:i+1] gave sum k, so up to this point this is the max len
                max_len += 1
            if k - prefix_sum in s:
                max_len = max(max_len, i - s[k-prefix_sum])
            else:
                s[prefix_sum] = i
        return max_len


"""
# ARRAY
Write up:
Keep a running index tracking prefix_sum
Keep an index tracking max_length
Iterate through nums list
    Update prefix sum
    If prefix sum is equal to k, then thats the longest possible length that sums up to k at the given iteration
    Else if prefix sum is greater than k
        Explanation of prefix_sum - k:
        nums = [-2 -1 2 1], k = 1
        (-2 + -1 + 2) - (-2) = 1
        -2 + -1 + 2 = -1
        -1 - 1 = -2
        -2 was in s
        Basically, prefix_sum - k finds the location where the values after add up to j
        Find if we can subtract away a previous calculated prefix_sum to get k
        Max(max_len, i - s[prefix_sum - k])
    If prefix_sum is not in dictionary:
        Add to dictionary, key: prefix_sum, value: i
Return max_length
"""
