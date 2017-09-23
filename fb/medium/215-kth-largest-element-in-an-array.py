"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
part = 4 # last element

[3, 5, 1, 2, 6, 4]
 ^^
[3, 5, 1, 2, 6, 4] # swap
    ^^
[3, 5, 1, 2, 6, 4]
    ^  ^
[3, 1, 5, 2, 6, 4]
       ^  ^
[3, 1, 2, 5, 6, 4]
          ^  ^
swap element at len(nums) - 1 with element at i
       ^  ^
[3, 1, 2, 4, 6, 5]

ith element is in place -> is this k? if not then either check left or check right until you get to the kth element!

# now compare
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while True:
            nums, pidx = self.partition(nums, start, end)
            if pidx == len(nums) - k:
                return nums[pidx]
            elif pidx < len(nums) - k:
                start = pidx + 1
            else: # pidx > len(nums) - k
                end = pidx - 1

    def partition(self, nums, start, end):
        """
        returns partitioned_nums, and index i at which element is in place
        """
        # end is where the partition number is
        i = start
        for j in range(start, end):
            if nums[j] <= nums[end]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
        temp = nums[i]
        nums[i] = nums[end]
        nums[end] = temp
        return nums, i

"""
Partition until the partition index is same as len(nums) - k
If index i returned is greater than len(nums) - k ; decrement end to i - 1
If index i returned is less than len(nums-k) ; increment start to i + 1
"""
