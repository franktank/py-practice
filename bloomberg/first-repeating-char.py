class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = [0 for _ in range(256)]
        for char in s:
            c[ord(char)] += 1
        for i in range(len(s)):
            if c[ord(s[i])] == 1:
                return i
        return -1



    def firstRepeatingChar(s):
        c = [0 for _ in range(256)]
        for i in range(len(s)):
            if c[ord(s[i])] == 1:
                return i
            c[ord(s[i])] += 1
        return -1

    def index_first_repeating_char(s):
        c = [0 for _ in range(256)]
        for char in s:
            c[ord(char)] += 1
        for i in range(len(s)):
            if c[ord(s[i])] > 1:
                return i, s[i]
        return -1
