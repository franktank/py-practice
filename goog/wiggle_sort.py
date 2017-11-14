class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Find median
        k = 0
        while k != len(nums/2):
            nums, k = self.random_partition
        # To the left of k is smaller or equal, to right of k is larger
        # M L S L S L S ...
        less_idx = 0
        large_idx = 4

    def random_partition(self, nums, start, end):
        r = random.randint(start, end) # for partition
        nums[r], nums[end] = nums[end], nums[r] # nums[end] is now partition element
        i = start
        for j in range(start, end):
            if nums[j] <= nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return nums, i
