# sliding window
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        for j in range(len(s)):
            if self.is_palindrome(s[i:j+1]):
                res += 1
            else:
                i += 1
        return res

    def is_palindrome(self, s):
        if len(s) <= 1:
            return True
        if not s[0] == s[len(s)-1]:
            return False
        else:
            return is_palindrome(s[1:len(s)-1])
