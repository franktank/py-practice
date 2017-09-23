"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
S.sort() = [-4, -1, -1, 0, 1, 2]

Prefix Sum = [-1, -1 ,0, 2, 1, -3]

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
# Brute force O(N^3)
# Optimizations -> Hashing and Sorting


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Reduce to two sum problem
        # target = 0 - list[i]
        # two sum target from range 0 to len(nums)
        # N^2 algorithm
        res = []
        nums.sort()
        for i in range(len(nums)):
            l = []
            target = 0 - nums[i]
            d = {}
            for j in range(i + 1, len(nums)): # Why this index? Don't want to reuse?
                if target - nums[j] in d:
                    l.append(nums[j])
                    l.append(target - nums[j])
                    l.append(nums[i])
                    res.append(l)
                    l = []
                else:
                    # What do about repeats?
                    d[nums[j]] = False
        return res

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # check i == 0 bc weird edge case where index are weird :()
            if (i == 0 or (i > 0 and not nums[i] == nums[i - 1])):
                target = 0 - nums[i]
                lo = i + 1
                hi = len(nums) - 1
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        l = [nums[i], nums[lo], nums[hi]]
                        res.append(l)
                        while (lo < hi and nums[lo] == nums[lo+1]):
                            lo += 1
                        while (lo < hi and nums[hi] == nums[hi-1]):
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < target:
                        lo += 1
                    else:
                        hi -= 1
        return res

"""
Talk about n^3 solution
Talk about hashing if duplicates
"""

"""
Sort array, this will get duplicates next to each other
Iterate from range 0 to len(nums) - 2 <--- think case where array size 3
Lo and Hi pointer for i+1 and len(nums) - 1 respectively
Target sum will be b + c = -a
Bidrectional sweep -> keep lo below hi
    Iterate while lo < hi
    if nums[lo] + nums[hi] is equal to -a, then 3 sum
        save 3 values
        increment lo and hi, but have to account for duplicates
            while lo < hi and nums[lo] == nums[lo+1] ; lo += 1
            while lo < hi and nums[hi] == nums[hi-1] ; hi -= 1
            lo += 1, hi += 1 ->> this will be the number after the dupes
    else if nums[lo] + nums[hi] < target:
        Here nums[lo] is too small, so increment it
        lo += 1
    else:
        nums[hi] is too big so decrement it
        hi -= 1
Return RESULTS
"""
