"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permutations = list()
        self.find_permute(nums, 0, len(nums)-1)

        return self.permutations

    def find_permute(self, num, start, end):
        if start == end:
            self.permutations.append(list(num))
        for i in range(start, end + 1):
            num[i], num[start] = num[start], num[i]
            self.find_permute(num, start + 1, end)
            num[i], num[start] = num[start], num[i]
