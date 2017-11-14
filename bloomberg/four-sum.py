class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            # OPTIONAL: if first number is too big, that means there's no hope
            if nums[i] + nums[i+1] + nums[i+2] + num[i+3] > target:
                break
            # OPTIONAL: first num too small if adding it with three largest number is less than target
            if nums[i] + nums[len(nums)-3] + nums[len(nums)-2] + nums[len(nums)-1] < target:
                continue
            # OPTIONAL: duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                # OPTIONAL: second candidate too large
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # OPTIONAL: second candidate too small
                if nums[i] + nums[j] + nums[len(nums)-2] + nums[len(nums)-1] < target:
                    continue
                # duplicates
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                low = j+1
                end = len(nums)-1
                # bidirectional sweep
                while low < end:
                    s = nums[i] + nums[j] + nums[low] + nums[end]
                    if s == target:
                        res.append([nums[i],nums[j],nums[low],nums[end]])
                        # handle dupes
                        while low < end and nums[low] == nums[low+1]:
                            low += 1
                        low += 1
                        # handle dupes
                        while low < end and nums[end] == nums[end-1]:
                            end -=1
                        end -= 1

                    elif s > target:
                        end -= 1
                    else:
                        low += 1
        return res
