class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        # search for first number
        start = 0
        end = len(nums)-1
        res = [-1,-1]
        while start < end:
            mid = (start+end)/2
            if nums[mid] == target:
                if nums[mid-1] != target:
                    res[0] = mid
                    break
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid + 1
        if nums[start] == target and (start == 0 or nums[start-1] != target):
            res[0] = start

        start = 0
        end = len(nums)-1
        # search for last number
        while start < end:
            mid = (start+end)/2
            if nums[mid] == target:
                if nums[mid+1] != target:
                    res[1] = mid
                    break
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid + 1
        if nums[start] == target and (start == len(nums)-1 or nums[start+1] != target):
            res[1] = start
        return res

        
