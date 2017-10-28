class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        # 2n-1 centers
        for i in range(2*len(s)-1):
            left = i / 2
            right = left + (i%2) # every other one will have a double center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                rigt += 1
        return count
