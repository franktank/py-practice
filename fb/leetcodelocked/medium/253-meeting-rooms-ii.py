"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        s = []
        e = []
        for interval in intervals:
            s.append(interval.start)
            e.append(interval.end)
        s.sort()
        e.sort()
        s_idx = 0
        e_idx = 0
        rooms = 0
        available = 0
        while s_idx < len(s):
            if s[s_idx] < e[e_idx]:
                if available == 0:
                    rooms += 1
                else:
                    available -= 1
                s_idx += 1
            else:
                available += 1
                e_idx += 1
        return rooms

"""
Solution:
Store start and end times separately
Sort start and end times
Keep running index for start and end list
Keep running index for rooms and available rooms
Iterate until all start times have been accounted for
If a start time is less than an end time, either take an available room or add a room, increment start index
If a start time is greater than an end time, increment available rooms and end index,
    NOTE: this does not account for the fact that at that start index, a room is needed
"""
