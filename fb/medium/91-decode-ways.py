"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [None for _ in range(len(s) + 1)]
        dp[0] = 1 # Init for len >= 2 to work
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1):
            substr = int(s[i - 2] + s[i - 1])
            dp[i] = 0
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if substr >= 10 and substr <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
