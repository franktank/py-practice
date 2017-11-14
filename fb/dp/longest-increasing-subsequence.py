class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            temp = dp[i]
            for j in range(0, i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[i] + dp[j])
            dp[i] = temp
        return max(dp)
