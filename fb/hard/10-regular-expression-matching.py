"""
HINT: http://shengshuyang.github.io/regular-expression-matching.html
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = '0' + s
        p = '0' + p
        dp = [[False for _ in range(len(p))] for _ in range(len(s))]
        dp[0][0] = True
        for i in range(len(s)):
            for j in range(1, len(p)):
                # Case 1: p[j] is a regular character or '.'
                # Edge case of '.' and ''
                if dp[i-1][j-1] and (s[i] == p[j] or (p[j] == '.' and not s[i] == '0')):
                    dp[i][j] = True
                if p[j] == '*':
                    # Case 2.1: 0 preceding matches, 'ab*' |= 'a', preceding char is 'a' and count is 0
                    # j > 1 because dependent on a regex 2 characters before *
                    if dp[i][j-2]:
                        dp[i][j] = True
                    # Case 2.2: 1 preceding match, 'ab*' |= 'ab', 'ab' covers 'ab'
                    elif dp[i][j-1]:
                        dp[i][j] = True
                    # Case 2.3: 2 or more preceding matches, 'ab*' |= 'abbbbbb'. We know if regex covers,
                    # the current char is the same as the previous char and s[:current_char] is covered by regex up to p[j]
                    # Induction like
                    # Check s[i] == p[j-1] case because ab*a and aaa
                    elif dp[i-1][j] and s[i] == s[i-1] and s[i] == p[j-1]:
                        dp[i][j] = True
                    # Case 2.4: '.*', '.*' covers 'abcdef'
                    elif p[j-1] == '.' and dp[i-1][j]:
                        dp[i][j] = True
        return dp[len(s)-1][len(p)-1]
