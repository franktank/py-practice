"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # alphanum = {}
        # alphanum['A']
        # ...
        return self.helper(s)

    def helper(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        if not s[0].isalnum():
            return self.helper(s[1:])
        if not s[len(s)-1].isalnum():
            return self.helper(s[:len(s)-1])
        if s[0] == s[len(s)-1]:
            return helper(s[1:len(s)-1])
        else:
            return False

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            if i == j:
                return True
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

"""
Iterative palindrome
i and j index
"""
