"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
"""
# Brute Force
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original_nums = list(nums)
        for idx,value in enumerate(nums):
            if idx == 0:
                continue
            nums[idx] += nums[idx - 1]
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.original_nums[i] = val
        numbs = list(self.original_nums)
        for idx,value in enumerate(numbs):
            if idx == 0:
                continue
            numbs[idx] += numbs[idx - 1]
        self.nums = numbs


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        return self.nums[j] - self.nums[i - 1]

# Optimized
# only recomputer for what happens after?
    class NumArray(object):

        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.original_nums = list(nums)
            for idx,value in enumerate(nums):
                if idx == 0:
                    continue
                nums[idx] += nums[idx - 1]
            self.nums = nums

        def update(self, i, val):
            """
            :type i: int
            :type val: int
            :rtype: void
            """

            self.original_nums[i] = val
            print(self.original_nums[i])
            print(val)
            new_nums = list(self.original_nums)
            if i != 0:
                new_nums[0:i-1] = list(self.nums[0:i-1])
            for idx in range(i,len(new_nums)):
                if idx == 0:
                    continue
                new_nums[idx] += new_nums[idx - 1]
            self.nums = list(new_nums)


        def sumRange(self, i, j):
            """
            :type i: int
            :type j: int
            :rtype: int
            """
            if i == 0:
                return self.nums[j]
            return self.nums[j] - self.nums[i - 1]
