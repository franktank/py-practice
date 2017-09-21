"""
Given two strings S and T, determine if they are both one edit distance apart.
"""
# not mismatch and string distance one apart?
# Insert, Delete, or Replace
# ac abc
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        min_range = min(len(s), len(t))
        s = list(s)
        t = list(t)
        for i in range(min_range):
            # 3 cases for length, s == t, s < t, t > s
            if not s[i] == t[i]:
                # t and s have same length
                if len(s) == len(t):
                    s[i] = t[i]
                    return s == t
                # t is longer than s
                elif len(s) < len(t):
                    # Remove a character from t
                    return s[i:] == t[i+1:]
                # s is longer than t
                else:
                    # Remove a character from s
                    return t[i:] == s[i+1:]
        # Iterated through s and t, no mismatch, check to see if one char apart, delete end char in longer string!
        return abs(len(s)-len(t)) == 1
