"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Move all nonzeros to front
        # Make last _ entries zeroes from counting
        nonzero_index = 0
        num_zero = 0
        for num in nums:
            if num != 0:
                # Place nonzeros in front
                nums[nonzero_index] = num
                nonzero_index += 1
            else:
                # Count number zeros
                num_zero += 1

        for i in range(num_zero):
            nums[len(nums) - 1 - i] = 0


    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Edge case: what if consecutive zeros? -> shift a zero and it will be stuck
        # Shift from certain indices, Change End to 0

        # Check if i + 1 is a zero?
        # Then shift again?
        for i, num in enumerate(nums):
            if num == 0:
                counter == 0
                idx = int(i)
                while nums[idx] == 0:
                    counter += 1
                    idx += 1
                    if idx >= len(nums):
                        break

                # Shift everything from right of it by one place
                # Replace last element with 0
                for _ in range(counter):
                    for j in range(i + 1, len(nums)):
                        nums[j - 1] = nums[j]
                    nums[len(nums) - 1] = 0
