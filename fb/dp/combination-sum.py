class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.dp = [0 for _ in range(target + 1)]
        self.helper(nums,target)
        return dp[target]

    def helper(self, nums, target):
        if target == 0:
            return 1
        if not dp[target] == 0:
            return dp[target]
            
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.combinationSum4(nums, target-nums[i])
        self.dp[target] = res
        return res
