"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary search
        if not nums:
            return 0
        start = 0
        end = len(nums)-1
        while start < end:
            # Base case: 0 1 2 4 5 6 7
            if num[start] < num[end]:
                return num[start]

            # Now we know array is rotated
            mid = (start + end) / 2
            # 4 5 6 7 0 1 2
            if num[start] < num[mid]: # start to mid is sorted
                start = mid + 1
            # 6 7 0 1 2 4 5
            elif num[start] > num[mid]:
                end = mid
