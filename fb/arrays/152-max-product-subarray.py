"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        cur_min = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            # negative numbers flip
            if nums[i] < 0:
                cur_min, cur_max = cur_max, cur_min

            cur_max = max(nums[i], nums[i] * cur_max)
            cur_min = min(nums[i], nums[i] * cur_min)

            res = max(res, cur_max)
        return res
