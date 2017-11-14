import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Count number of elements
        # Two arrays?
        # Use a heap
        counts = []
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for key,value in d.items():
            counts.append((value,key))

        heapq.heapify(counts)
        k_freq = heapq.nlargest(k, counts)
        return [element[1] for element in k_freq]
