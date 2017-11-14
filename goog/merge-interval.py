"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
class Solution(object):
    def merge(intervals_list):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        for i in range(1, len(intervals_list)):
            if intervals_list[i][0] <= intervals_list[i-1][1]:
                low = min(intervals_list[i][0],intervals_list[i][1],intervals_list[i-1][0],intervals_list[i-1][1])
                high = max(intervals_list[i][0],intervals_list[i][1],intervals_list[i-1][0],intervals_list[i-1][1])
                intervals_list[i] = [low,high]
                intervals_list[i-1] = None
        intervals_list = [x for x in intervals_list if x]
        return intervals_list

def find_missing_range(intervals):
    merge(intervals)
    intervals = [x for x in intervals if x]
    res = []
    for i in range(1,len(intervals)):
        res.append([intervals[i-1][1] + 1, intervals[i][0]-1])
    return res
