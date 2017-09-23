"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
"""
4,5,6,7,0,1,2
or
3,4,0,1
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end)/2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]: # we know its sorted from lo to mid
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else: # nums[lo] > nums[mid],we know from mid to hi it is sorted in ascending order
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        if nums[start] == target:
            return start
        else:
            return -1
"""
Binary search with extra conditions
Rotated array:
If nums[start] < nums[mid] , we know that from start to mid it is in ascending order
    If target is in range nums[start] to nums[mid], then we just set end to be mid - 1
    Otherwise its not in this range, we know we have to set start = mid + 1
If nums[start] > nums[mid], we know from mid to end, it is in ascending order
    If target is in range nums[mid] to nums[end], then we set start = mid + 1
    Otherwise, not in this range, end = mid - 1
"""
