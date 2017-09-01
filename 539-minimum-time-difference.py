"""
Given a list of 24-hour clock time points in "Hour:Minutes" format,
find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""
# Convert to minutes
# Sort
# Check adjacent -> to left and right
import collections

class Solution(object):
    def convert_to_minutes(self, time_point):
        """
        :type time_point: str
        :rtype int
        """
        tp = time_point.split(":")
        time_in_minute = (int(tp[0])*60) + int(tp[1])
        return time_in_minute

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tp_min = list()
        for time_point in timePoints:
            tp_min.append(self.convert_to_minutes(time_point))

        tp_min.sort() # ascending order

        min_difference = 1440
        for i in range(len(tp_min)):
            if i == 0:
                continue
            min_difference = min(min_difference, tp_min[i] - tp_min[i - 1])

        min_difference = min(min_difference, 1440 - abs(tp_min[0] - tp_min[len(tp_min) - 1]))
        return min_difference
