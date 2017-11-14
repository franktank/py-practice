class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        o = 0
        t = 0
        for num in range(len(nums)):
            if num == 0:
                z += 1
            elif num == 1:
                o += 1
            else:
                t += 1
        idx = 0
        while z > 0:
            num[idx] = 0
            z -= 1
            idx += 1

        while o > 0:
            num[idx] = 1
            o -= 1
            idx += 1

        while t > 0:
            num[idx] = 2
            t -= 1
            idx += 1

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

    def partition(self, nums, start, end):
        i = start
        for j in range(start, end):
            if nums[j] <= nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return nums, i
