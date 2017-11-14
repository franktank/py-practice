"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
"""
If a number is positive and dp[] is negative, take the positive!
dp[i] = A[i] + max(dp[i-1], 0)
res = max(dp[i], res)
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, nums):
            dp[i] = nums[i] + max(dp[i-1], 0)
            res = max(res, dp[i])
        return res
