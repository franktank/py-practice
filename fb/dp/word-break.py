class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.memo = {}
        self.word_break(s, wordDict)
        return self.memo[s]

    def word_break(self,s, wordDict)
        if s in wordDict:
            self.memo[s] = True
            return True

        if s in self.memo:
            return self.memo[s]

        for i in range(len(s)):
            if s[:i+1] in wordDict:
                if word_break(s[i:]):
                    return True
        self.memo[s] = False
        return False

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                if s[i-len(word)+1:i+1] == word and (dp[i-len(word)] or i-len(word) == -1):
                    dp[i] = True

        return dp[len(s)-1]
