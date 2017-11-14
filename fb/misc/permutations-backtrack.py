class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(nums, [])
        return self.res

    def helper(self, nums, cur_per):
        if len(cur_per) == len(nums):
            self.res.append(cur_per)
        for i in range(len(nums)):
            if nums[i] in cur_per:
                continue
            cur_per.append(nums[i])
            self.helper(nums, cur_per, i + 1)
            cur_per.pop()
