class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        d = {}
        start = 0
        for char in p:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        i = 0
        count = len(p)
        for j in range(len(s)):
            if s[j] in d:
                if d[s[j]] >= 1:
                    count -= 1
                    d[s[j]] -= 1

            if count == 0:
                res.append(i)
            if j - i = len(p):
                if s[i] in d:
                    if d[s[i]] >= 0:
                        count += 1
                        d[s[i]] += 1
                        i += 1
        return res
