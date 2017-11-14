class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums, [], 0)
        return self.res

    def helper(self, nums, cur_set, start):
        self.res.append(list(cur_set))
        for i in range(start, len(nums)):
            cur_set.append(nums[i])
            self.helper(nums, cur_set, i + 1) # i+1 because no duplicates
            cur_set.pop()
