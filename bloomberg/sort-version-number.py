"""
https://stackoverflow.com/questions/2574080/sorting-a-list-of-dot-separated-numbers-like-software-versions
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = version1.split(".")
        b = version2.split(".")
        a = [int(e) for e in a]
        b = [int(e) for e in b]
        if a == b:
            return 0
        return self.helper(a,b)

    def helper(self,a,b):
        for i in range(min(len(a), len(b))):
            ele_a = a[i]
            ele_b = b[i]
            if ele_a > ele_b:
                return 1
            elif ele_a < ele_b:
                return -1
        if len(a) > len(b):
            return 1
        else:
            return -1
