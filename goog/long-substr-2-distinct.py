class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            if len(d.keys()) > 2:
                while len(d.keys()) > 2:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        del d[s[i]]
                    i += 1
            res = max(res, j-i+1)
        return res
