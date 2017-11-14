class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = {}
        num_keys = 0
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in counter:
                counter[s[j]] = 1
                num_keys += 1
            else:
                counter[s[j]] += 1
            while num_keys > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                    num_keys -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
