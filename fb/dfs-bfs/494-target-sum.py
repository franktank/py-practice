class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.s = S
        self.count = 0
        self.helper(nums, 0)
        return self.count

    def helper(self, nums, cur_sum):
        if not nums and cur_sum == self.s:
             self.count += 1
        self.helper(nums[1:], cur_sum += nums[0])
        self.helper(nums[1:], cur_sum -= nums[0])

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.memo = [[-1001 for _ in range(len(nums))] for _ in range(2001)]
        self.s = S
        self.count = 0
        self.helper(nums, 0)
        return self.count

    def helper(self, nums, cur_sum):
        if not nums:
            if cur_sum == self.s:
                self.count += 1
                return 1
            return 0
        if self.memo[len(nums)-1][cur_sum + 1000] > -1001:
            # We've done this calculation!
            if self.memo[len(nums)-1][cur_sum + 1000] == self.s:
                self.count += 1
                return 1
            return 0
        else:
            add = self.helper(nums[1:], cur_sum + nums[0])
            sub = self.helper(nums[1:], cur_sum - nums[0])
            self.memo[len(nums)-1][cur_sum + 1000] = add + sub
            return self.memo[len(nums)-1]

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.target = S
        self.memo = [[-1001 for _ in range(2001)] for _ in range(len(nums))]
        return self.helper(nums, 0, 0)

    def helper(self, nums, nidx, cur_sum):
        if nidx == len(nums):
            if cur_sum == self.target:
                return 1
            return 0
        else:
            if not self.memo[nidx][cur_sum + 1000] == -1001:
                return self.memo[nidx][cur_sum + 1000]
            add = self.helper(nums, nidx + 1, cur_sum + nums[nidx])
            sub = self.helper(nums, nidx + 1, cur_sum - nums[nidx])
            self.memo[nidx][cur_sum + 1000] = add + sub
            return self.memo[nidx][cur_sum + 1000]
