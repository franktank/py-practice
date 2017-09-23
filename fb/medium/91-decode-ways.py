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

"""
**** IMPORTANT CASES: 1212, 1232, 302, 102
Recurrence: -> good start, but weird case of 0s
if 10 <= int(s[i-1] + s[i]) >= 26
    dp[i] = dp[i-1] + dp[i-2]
else:
    dp[i] = dp[i-1]


if 10 <= int(s[i-2] + s[i-1]) >= 26 # SUBSTRING OF CURRENT AND LAST CHARACTER HAS AN ENCONDING -> between 10 and 26
    dp[i] += dp[i-2]
if not nums[i-1] == '0':   # CURRENT CHARACTER IS NOT 0
    dp[i] += dp[i-1]

dp size is len(nums) + 1

dp[0] = 1
if not s[0] == '0':
    dp[1] = 1
"""

"""
Decodings for
1212
1 -> 1 // 1
12 -> 1 2; 12 // 2
121 -> 1 2 1; 12 1; 1 21 // 3
1212 -> 1 2 1 2; 12 1 2; 1 21 2; 1 2 12; 12 12 // 5

1232
1 -> 1 // 1
12 -> 1 2; 12 // 2
123 -> 1 2 3; 12 3; 1 23 // 3
1232 -> 1 2 3 2; 12 3 2; 1 23 2 // 3

302
3 // 1
30 // 0
302 // 0

102
1 // 1
10 // 1
102 // 1
"""
# LIKE FIBONACCI BUT WITH CONDITIONALS IN GETTING PREVIOUS NUMBERS
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        if not s[0] == '0':
            dp[1] = 1

        # Iterate to end of dp
        for i in range(2, len(s) + 1):
            # NOTE: s[i - 1] is the current character!!!
            if not s[i - 1] == '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2] + s[i-1]) <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]


"""
Create DP array of len(s) + 1
Go through cases 1212, 1232, 302, 102 # Build up to it, ex. 1 12 121 1212
Question similar to fibonacci
Presolve dp[0] and dp[1]
dp[0] = 1, dp[1] = 1 if not s[0] == '0'
Iterete through rest of dp and note that s[i-1] is the *current* character
Conditions:
    Current character is not '0'
    int(current_char + prev_char) is in between 10 and 26 inclusive
"""
