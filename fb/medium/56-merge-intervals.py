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
        res = []
        for i in range(1, len(l)):
            # Compare and find intersects
            if l[i-1][1] >= l[i][0]:
                bottom = min(l[i][0],l[i][1],l[i-1][0],l[i-1][1])
                top = max(l[i][0],l[i][1],l[i-1][0],l[i-1][1])
                l[i][0] = bottom
                l[i][1] = top
                l[i-1] = None
        res = []
        for ele in l:
            if ele:
                res.append(Interval(ele[0], ele[1]))
        return res

"""
Interval into list of lists
Iterate through lists, see if intervals overlap
If overlap, merge interval by getting max and min of prev and current interval start / end
Make previous interval None
Iterate through intervals, and turn the ones that aren't None into an Interval object
"""
