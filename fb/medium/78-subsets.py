"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
"""
 1    2    3    4
 234  3    4
 34   4
 4
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        return res

# Generate all cominbations of sets -> subsets!!
"""
First append an empty list to your results list
Iterate through nums:
  Iterate through res each time:
    Append a concatenation of res[j] + nums[i]
Return results
"""
