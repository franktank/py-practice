"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = []
        for interval in intervals:
            l.append([interval.start, interval.end])

        l.sort()
        for i in range(1, len(l)):
            if l[i-1][1] >= l[i][0]:
                l[i][0] = min(l[i-1][0],l[i-1][1],l[i][0],l[i][1])
                l[i][1] = max(l[i-1][0],l[i-1][1],l[i][0],l[i][1])
                l[i-1] = None
        res = []
        for e in l:
            if e == None:
                continue
            res.append(Interval(e[0],e[1]))
        return res
