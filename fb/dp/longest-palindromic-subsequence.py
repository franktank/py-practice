class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.helper(s, 0, len(s)-1)

    def helper(self, s, left, right):
        if left == right: # odd number string, so both on same
            return 1
        if left > right: # passed, so like done
            return 0
        if s[left] == s[right]:
            return 2 + self.helper(s, left+1, right-1)
        else:
            return max(self.helper(s,left+1,right), self.helper(s,left,right-1))

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dp = [[-1 for _ in range(len(s))] for _  in range(len(s))]
        return self.dp[0][len(s)-1]


    def helper(self, s, left, right):
        if not self.dp[left][right] == -1:
            return self.dp[left][right]
        if left == right:
            self.dp[left][right] = 1
            return 1
        if left > right:
            self.dp[left][right] = 0
            return 0
        if s[left] == s[right]:
            self.dp[left][right] = 2 + self.helper(s, left+1, right-1)
            return self.dp[left][right]
        else:
            self.dp[left][right] = max(self.helper(s,left+1,right), self.helper(s,left,right-1))
            return self.dp[left][right]
