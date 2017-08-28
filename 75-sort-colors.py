"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
import collections

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # p 147 CLRS
        # Swap a 1 to len(nums) - 1
        is_sorted = True
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                is_sorted = False

        if is_sorted:
            return

        for index, num in enumerate(nums):
            if num == 1:
                temp = nums[len(nums)-1]
                nums[len(nums)-1] = num
                nums[index] = temp
                break
        # Partition
        partition_value = nums[len(nums)-1]
        i = -1
        j = 0

        while j < len(nums):
            if nums[j] < partition_value:
                i += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            j += 1
        temp = nums[j-1]
        nums[j-1] = nums[i+1]
        nums[i+1] = temp
        # Partition

        # Everything less than i + 1 is now a 0
        # Place a 2 at len(nums) - 1
        for i in range(i+1, j):
            if nums[i] == 2:
                temp = nums[len(nums)-1]
                nums[len(nums)-1] = nums[i]
                nums[index] = temp
                break

        partition_value = nums[len(nums)-1]
        j = i + 1
        while j < len(nums):
            if nums[j] < partition_value:
                i += 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            j += 1

        temp = nums[j-1]
        nums[j-1] = nums[i]
        nums[i+1] = temp

        # Count 0, 1, and 2; replace

        counts = collections.defaultdict(lambda:0)
        for num in nums:
            counts[num] += 1

        index = 0
        for i in range(counts[0]):
            nums[index] = 0
            index += 1

        for i in range(counts[1]):
            nums[index] = 1
            index += 1

        for i in range(counts[2]):
            nums[index] = 2
            index += 1
