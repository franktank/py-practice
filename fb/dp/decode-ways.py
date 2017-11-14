class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        if not str[0] == '0':
            dp[1] = 1
        else:
            return 0
        for i in range(2, len(dp)):
            if not s[i-1] == '0': # NOTE: index is -1 because len(dp) = len(s) + 1
                dp[i] += dp[i-1]
            substr = int(s[i-2] + s[i-1])
            if 10 <= substr <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]
